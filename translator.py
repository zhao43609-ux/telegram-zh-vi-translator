#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
翻译模块 - 支持中文和越南文互译
"""

import os
import logging
from typing import Tuple
import requests
from google.cloud import translate_v2
from langdetect import detect, LangDetectException

logger = logging.getLogger(__name__)

class Translator:
    """翻译器类"""
    
    def __init__(self):
        """初始化翻译器"""
        self.api_key = os.getenv('GOOGLE_TRANSLATE_API_KEY')
        # 尝试使用 Google Cloud Translation API
        if self.api_key:
            try:
                self.client = translate_v2.Client(credentials=self.api_key)
            except Exception as e:
                logger.warning(f"无法连接 Google Cloud API: {e}")
                self.client = None
        else:
            self.client = None
            logger.info("未配置 Google Cloud API，使用免费翻译服务")
    
    def detect_language(self, text: str) -> str:
        """检测文本语言
        
        Args:
            text: 输入文本
            
        Returns:
            语言代码 ('zh' 或 'vi')
        """
        try:
            lang = detect(text)
            if lang.startswith('zh'):
                return 'zh'
            elif lang.startswith('vi'):
                return 'vi'
            else:
                return lang
        except LangDetectException:
            logger.warning("无法检测语言，默认返回中文")
            return 'zh'
    
    def translate_zh_to_vi(self, text: str) -> str:
        """中文翻译成越南文
        
        Args:
            text: 中文文本
            
        Returns:
            越南文翻译
        """
        return self._translate(text, 'zh', 'vi')
    
    def translate_vi_to_zh(self, text: str) -> str:
        """越南文翻译成中文
        
        Args:
            text: 越南文文本
            
        Returns:
            中文翻译
        """
        return self._translate(text, 'vi', 'zh')
    
    def _translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """通用翻译方法
        
        Args:
            text: 要翻译的文本
            source_lang: 源语言代码
            target_lang: 目标语言代码
            
        Returns:
            翻译后的文本
        """
        try:
            # 首先尝试使用 Google Cloud API
            if self.client:
                result = self.client.translate_text(
                    text,
                    source_language=source_lang,
                    target_language=target_lang
                )
                return result['translatedText']
            
            # 如果 API 不可用，使用免费的翻译服务
            return self._translate_free(text, source_lang, target_lang)
            
        except Exception as e:
            logger.error(f"翻译错误: {e}")
            raise Exception(f"翻译失败: {str(e)}")
    
    def _translate_free(self, text: str, source_lang: str, target_lang: str) -> str:
        """使用免费翻译 API
        
        Args:
            text: 要翻译的文本
            source_lang: 源语言代码
            target_lang: 目标语言代码
            
        Returns:
            翻译后的文本
        """
        try:
            # 使用 MyMemory 翻译 API (免费)
            url = "https://api.mymemory.translated.net/get"
            
            # 映射语言代码
            source_code = self._map_lang_code(source_lang)
            target_code = self._map_lang_code(target_lang)
            
            params = {
                'q': text,
                'langpair': f'{source_code}|{target_code}'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if data['responseStatus'] == 200:
                return data['responseData']['translatedText']
            else:
                raise Exception(f"翻译 API 返回错误: {data.get('responseDetails')}")
                
        except Exception as e:
            logger.error(f"免费翻译失败: {e}")
            raise Exception(f"翻译服务暂时不可用")
    
    def _map_lang_code(self, lang_code: str) -> str:
        """将语言代码映射为翻译 API 支持的格式
        
        Args:
            lang_code: 原始语言代码
            
        Returns:
            映射后的语言代码
        """
        lang_map = {
            'zh': 'zh-CN',  # 中文简体
            'vi': 'vi',     # 越南文
        }
        return lang_map.get(lang_code, lang_code)
    
    def get_lang_name(self, lang_code: str) -> str:
        """获取语言名称
        
        Args:
            lang_code: 语言代码
            
        Returns:
            语言名称
        """
        lang_names = {
            'zh': '中文',
            'vi': '越南文',
        }
        return lang_names.get(lang_code, lang_code)
