#!/bin/bash

# Telegram 中越互译机器人 - 安装脚本

echo "🚀 Telegram 中越互译机器人 - 安装向导"
echo ""

# 检查 Python 版本
echo "📝 检查 Python 版本..."
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到 Python 3，请先安装 Python 3.7+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python 版本: $PYTHON_VERSION"
echo ""

# 创建虚拟环境
echo "📦 创建虚拟环境..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ 虚拟环境已创建"
else
    echo "✅ 虚拟环境已存在"
fi
echo ""

# 激活虚拟环境
echo "🔌 激活虚拟环境..."
source venv/bin/activate
echo "✅ 虚拟环境已激活"
echo ""

# 升级 pip
echo "📦 升级 pip..."
pip install --upgrade pip
echo "✅ pip 已升级"
echo ""

# 安装依赖
echo "📦 安装依赖..."
pip install -r requirements.txt
echo "✅ 依赖已安装"
echo ""

# 创建 .env 文件
echo "⚙️  配置环境变量..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ .env 文件已创建，请编辑填入您的信息"
    echo ""
    echo "📝 需要填入以下信息:"
    echo "  - TELEGRAM_BOT_TOKEN: Telegram 机器人 Token"
    echo "  - GOOGLE_TRANSLATE_API_KEY (可选): Google 翻译 API Key"
    echo ""
    echo "📖 详细说明请参考 README.md"
else
    echo "✅ .env 文件已存在"
fi
echo ""

# 完成
echo "🎉 安装完成！"
echo ""
echo "📌 后续步骤:"
echo "1. 编辑 .env 文件，填入 Telegram Bot Token"
echo "2. 运行: python main.py"
echo ""
echo "💡 更多帮助请查看 README.md"
