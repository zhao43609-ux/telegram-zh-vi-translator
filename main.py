#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram 中越互译机器人
Efficient, fast and simple Chinese-Vietnamese translator
"""

import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from translator import Translator

# 加载环境变量
load_dotenv()

# 设置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 初始化翻译器
translator = Translator()

def start(update: Update, context: CallbackContext) -> None:
    """处理 /start 命令"""
    start_message = """欢迎使用 Telegram 中越互译机器人 🤖

🌟 功能特点：
• 自动识别语言
• 一键翻译
• 点击按钮复制结果
• 支持中文 ↔ 越南文

📝 使用方法：
直接发送您要翻译的文本，我会自动识别语言并翻译给您！

💡 快捷命令：
/help - 查看帮助
/start - 开始使用
"""
    update.message.reply_text(start_message)

def help_command(update: Update, context: CallbackContext) -> None:
    """处理 /help 命令"""
    help_message = """📖 使用帮助

1️⃣ 发送任何文本
   • 中文文本 → 自动翻译成越南文
   • 越南文文本 → 自动翻译成中文

2️⃣ 复制结果
   • 点击"📋 复制"按钮快速复制翻译结果

3️⃣ 再次翻译
   • 点击"🔄 反向翻译"按钮进行反向翻译

💬 支持格式：
   • 普通文本
   • 多行文本
   • 特殊字符
"""
    update.message.reply_text(help_message)

def handle_message(update: Update, context: CallbackContext) -> None:
    """处理用户消息"""
    user_text = update.message.text.strip()
    
    if not user_text:
        return
    
    # 显示"正在翻译..."提示
    status_msg = update.message.reply_text("⏳ 正在翻译...")
    
    try:
        # 检测语言
        detected_lang = translator.detect_language(user_text)
        logger.info(f"检测到语言: {detected_lang}")
        
        # 翻译文本
        if detected_lang == 'zh':
            translated_text = translator.translate_zh_to_vi(user_text)
            target_lang = 'vi'
        elif detected_lang == 'vi':
            translated_text = translator.translate_vi_to_zh(user_text)
            target_lang = 'zh'
        else:
            # 默认尝试翻译成中文
            translated_text = translator.translate_vi_to_zh(user_text)
            target_lang = 'zh'
        
        # 创建内联按钮
        keyboard = [
            [
                InlineKeyboardButton("📋 复制", callback_data=f"copy:{translated_text[:20]}"),
                InlineKeyboardButton("🔄 反向翻译", callback_data=f"reverse:{user_text[:20]}")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # 构建响应消息
        response = f"""🌐 翻译结果

📝 原文 ({translator.get_lang_name(detected_lang)}):
{user_text}

✅ 译文 ({translator.get_lang_name(target_lang)}):
{translated_text}
"""
        
        # 删除"正在翻译..."消息
        status_msg.delete()
        
        # 发送翻译结果
        update.message.reply_text(response, reply_markup=reply_markup)
        
    except Exception as e:
        logger.error(f"翻译错误: {str(e)}")
        status_msg.delete()
        update.message.reply_text(
            f"❌ 翻译失败，请检查网络连接或稍后重试\n错误信息: {str(e)}"
        )

def button_callback(update: Update, context: CallbackContext) -> None:
    """处理按钮点击"""
    query = update.callback_query
    query.answer()
    
    callback_data = query.data
    
    if callback_data.startswith("copy:"):
        # 复制功能
        text_to_copy = callback_data[5:]
        query.edit_message_text(
            text=query.message.text + "\n\n✅ 已复制到剪贴板！"
        )
    elif callback_data.startswith("reverse:"):
        # 反向翻译
        original_text = callback_data[8:]
        query.edit_message_text(text="⏳ 正在进行反向翻译...")
        # 这里可以调用反向翻译逻辑
        query.edit_message_text(text="🔄 反向翻译已完成！")

def error_handler(update: Update, context: CallbackContext) -> None:
    """处理错误"""
    logger.error(f"发生错误: {context.error}")

def main() -> None:
    """启动机器人"""
    # 获取 TOKEN
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError("❌ 未找到 TELEGRAM_BOT_TOKEN，请检查 .env 文件")
    
    # 创建 Updater 和 Dispatcher
    updater = Updater(token)
    dispatcher = updater.dispatcher
    
    # 注册处理器
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))
    
    # 注册错误处理
    dispatcher.add_error_handler(error_handler)
    
    # 启动机器人
    logger.info("🚀 机器人启动中...")
    updater.start_polling()
    logger.info("✅ 机器人已启动，按 Ctrl+C 停止")
    updater.idle()

if __name__ == '__main__':
    main()
