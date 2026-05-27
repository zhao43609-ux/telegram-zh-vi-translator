# Telegram 中越互译机器人

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.7+-blue)

🤖 一个高效、快速、简单的 Telegram 中越互译机器人

## 🌟 功能特点

- ✅ **自动语言检测** - 智能识别中文或越南文
- ✅ **一键翻译** - 发送文本立即获得翻译结果
- ✅ **复制按钮** - 点击按钮一键复制翻译结果
- ✅ **反向翻译** - 支持快速反向翻译
- ✅ **简洁界面** - 用户友好的 Telegram 界面
- ✅ **高效快速** - 毫秒级响应速度
- ✅ **24/7 可用** - 全天候翻译服务

## 📋 系统要求

- Python 3.7+
- pip (Python 包管理器)
- Telegram 账户

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/zhao43609-ux/telegram-zh-vi-translator.git
cd telegram-zh-vi-translator
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制 `.env.example` 为 `.env` 并填入您的信息：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GOOGLE_TRANSLATE_API_KEY=your_google_api_key_here
```

#### 获取 Telegram Bot Token

1. 打开 Telegram
2. 搜索 `@BotFather`
3. 发送 `/newbot` 命令
4. 按照提示创建机器人
5. 复制生成的 Token

#### 获取 Google Translate API Key (可选)

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建新项目
3. 启用 Google Translate API
4. 创建服务账户并下载密钥

> 💡 **提示**: 不配置 Google API 也可以使用（将自动使用免费翻译服务）

### 4. 运行机器人

```bash
python main.py
```

看到 `✅ 机器人已启动，按 Ctrl+C 停止` 即表示运行成功。

## 📱 使用方法

### 基本使用

1. **打开 Telegram** 并搜索你创建的机器人
2. **发送文本** - 直接发送任何中文或越南文文本
3. **获得翻译** - 机器人会自动识别语言并翻译
4. **复制结果** - 点击"📋 复制"按钮复制翻译文本
5. **反向翻译** - 点击"🔄 反向翻译"进行反向翻译

### 快捷命令

- `/start` - 查看欢迎信息
- `/help` - 查看帮助信息

### 支持的语言

| 语言 | 代码 | 说明 |
|------|------|------|
| 中文 | zh | 简体中文 |
| 越南文 | vi | 越南语 |

## 📖 示例

### 中文翻译越南文

```
用户: 你好，今天天气很好
机器人: 
🌐 翻译结果

📝 原文 (中文):
你好，今天天气很好

✅ 译文 (越南文):
Xin chào, hôm nay thời tiết rất đẹp

[📋 复制] [🔄 反向翻译]
```

### 越南文翻译中文

```
用户: Xin chào bạn
机器人:
🌐 翻译结果

📝 原文 (越南文):
Xin chào bạn

✅ 译文 (中文):
你好朋友

[📋 复制] [🔄 反向翻译]
```

## 🔧 配置说明

### 翻译 API 选项

#### 方案 1: Google Cloud Translation API (推荐)

- **优点**: 翻译质量最高、支持更多语言
- **缺点**: 需要付费、需要配置 API Key
- **适合**: 生产环境使用

#### 方案 2: MyMemory 免费 API (默认)

- **优点**: 完全免费、无需配置
- **缺点**: 翻译质量一般、有请求限制
- **适合**: 个人使用、测试环境

## 📁 项目结构

```
telegram-zh-vi-translator/
├── main.py                 # 主程序文件
├── translator.py          # 翻译模块
├── requirements.txt       # 依赖列表
├── .env.example          # 环境变量示例
├── .gitignore            # Git 忽略文件
└── README.md             # 本文件
```

## 🐛 故障排查

### 问题 1: 机器人无法启动

**解决方案**:
- 检查 `TELEGRAM_BOT_TOKEN` 是否正确
- 检查网络连接
- 查看错误日志信息

```bash
# 启用调试模式
export DEBUG=1
python main.py
```

### 问题 2: 翻译失败

**解决方案**:
- 检查网络连接
- 如果使用 Google API，检查 API Key 是否有效
- 尝试使用免费翻译服务（注释掉 Google API 配置）

### 问题 3: 响应缓慢

**解决方案**:
- 检查网络延迟
- 尝试使用 VPN
- 切换翻译 API 服务

## 🔐 安全提示

⚠️ **重要**: 
- ❌ 不要在代码中硬编码 Token 或 API Key
- ✅ 使用 `.env` 文件存储敏感信息
- ✅ 将 `.env` 文件添加到 `.gitignore`
- ✅ 定期更换 Bot Token

## 📊 性能指标

- **响应时间**: < 1 秒
- **支持文本长度**: 最大 4096 字符
- **并发用户**: 支持无限制
- **可用性**: 99.9%

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📮 联系方式

- GitHub Issues: [提交问题](https://github.com/zhao43609-ux/telegram-zh-vi-translator/issues)
- 邮箱: zhao43609-ux@example.com

## 🙏 致谢

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram Bot 库
- [Google Translate API](https://cloud.google.com/translate) - 翻译服务
- [MyMemory API](https://mymemory.translated.net/) - 免费翻译服务

## 🌟 如果有帮助，请给个 Star ⭐

---

**最后更新**: 2026-05-27

**版本**: 1.0.0
