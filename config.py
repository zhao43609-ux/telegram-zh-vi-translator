#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置文件
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# Telegram 配置
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ 缺少必要的环境变量: TELEGRAM_BOT_TOKEN")

# Google Translate 配置
GOOGLE_TRANSLATE_API_KEY = os.getenv('GOOGLE_TRANSLATE_API_KEY')

# 应用配置
APP_NAME = "Telegram 中越互译机器人"
APP_VERSION = "1.0.0"
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# 翻译配置
SOURCE_LANGUAGES = ['zh', 'vi']
TARGET_LANGUAGES = ['zh', 'vi']
TRANSLATE_TIMEOUT = 10  # 翻译超时时间（秒）

# 消息配置
MAX_MESSAGE_LENGTH = 4096
MAX_TRANSLATION_LENGTH = 1000

# 日志配置
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'

if __name__ == '__main__':
    print(f"🔧 配置信息:")
    print(f"  应用名: {APP_NAME}")
    print(f"  版本: {APP_VERSION}")
    print(f"  调试模式: {DEBUG}")
    print(f"  支持语言: {', '.join(SOURCE_LANGUAGES)}")
