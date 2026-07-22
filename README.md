# 微信小程序推广自动化工具

## 项目简介
这是一个自动化生成微信小程序推广素材并分发的工具，专为"每天朗读提高口才"小程序设计。

## 核心功能

### 1. 内容生成模块
- **公众号推文生成**: 自动生成 Markdown 格式的朗读训练文案
- **短视频脚本生成**: 生成适合视频号/抖音的短视频文案和标题
- **小红书图文生成**: 生成精美的朗读金句卡片文案

### 2. 排版优化模块
- 集成 wechat-formatter 能力，支持 Markdown 转微信排版
- 内置 72 套精美模板
- AI 一键优化排版结构

### 3. 多平台分发模块
- 微信公众号自动发布
- 视频号/抖音自动上传
- 小红书图文自动发布
- 朋友圈素材自动生成

## 技术栈
- Python 3.9+
- Node.js 18+
- OpenAI API / 国产大模型兼容

## 快速开始

```bash
# 克隆项目
git clone https://github.com/emmadiuoo/wechat-miniprogram-promo-automation.git

# 安装依赖
pip install -r requirements.txt
npm install

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入 API Key 等配置

# 运行工具
python main.py
```

## 目录结构
```
wechat-miniprogram-promo-automation/
├── content_generator/      # 内容生成模块
│   ├── article_gen.py     # 公众号文章生成
│   ├── video_script_gen.py # 短视频脚本生成
│   └── social_card_gen.py  # 社交卡片生成
├── formatter/             # 排版优化模块
│   └── wechat_formatter.py
├── distributor/           # 分发模块
│   ├── wechat_publisher.py
│   ├── video_uploader.py
│   └── xiaohongshu_publisher.py
├── config/               # 配置文件
├── templates/            # 模板文件
── main.py              # 主入口
└── requirements.txt     # Python 依赖
```

## 使用说明

### 生成每日朗读素材
```bash
python main.py --generate-daily-content --date=2026-07-22
```

### 自动分发到各平台
```bash
python main.py --distribute --platforms=wechat,video,xiaohongshu
```

## 许可证
MIT License





























































