#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信小程序推广自动化工具 - 主入口
自动生成推广素材并分发到多个平台
"""

import argparse
import logging
from datetime import datetime
from pathlib import Path

# 导入各功能模块
from content_generator.article_gen import ArticleGenerator
from content_generator.video_script_gen import VideoScriptGenerator
from content_generator.social_card_gen import SocialCardGenerator
from formatter.wechat_formatter import WechatFormatter
from distributor.wechat_publisher import WechatPublisher
from distributor.video_uploader import VideoUploader
from distributor.xiaohongshu_publisher import XiaohongshuPublisher

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PromoAutomationTool:
    """推广自动化工具主类"""
    
    def __init__(self, config_path: str = "config/config.yaml"):
        """
        初始化工具
        
        Args:
            config_path: 配置文件路径
        """
        self.config_path = Path(config_path)
        self.load_config()
        
        # 初始化各模块
        self.article_gen = ArticleGenerator(self.config)
        self.video_script_gen = VideoScriptGenerator(self.config)
        self.social_card_gen = SocialCardGenerator(self.config)
        self.formatter = WechatFormatter()
        self.wechat_pub = WechatPublisher(self.config)
        self.video_uploader = VideoUploader(self.config)
        self.xiaohongshu_pub = XiaohongshuPublisher(self.config)
        
        logger.info("推广自动化工具初始化完成")
    
    def load_config(self):
        """加载配置文件"""
        import yaml
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
        else:
            logger.warning(f"配置文件 {self.config_path} 不存在，使用默认配置")
            self.config = self.get_default_config()
    
    def get_default_config(self):
        """获取默认配置"""
        return {
            "api": {
                "openai_key": "",
                "model": "gpt-4",
            },
            "wechat": {
                "app_id": "",
                "app_secret": "",
            },
            "video_platforms": ["douyin", "video_account"],
            "output_dir": "./output",
        }
    
    def generate_daily_content(self, date: str = None, topic: str = None):
        """
        生成每日朗读素材
        
        Args:
            date: 日期，格式 YYYY-MM-DD
            topic: 主题（可选）
        """
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        logger.info(f"开始生成 {date} 的朗读素材...")
        
        # 生成公众号文章
        article = self.article_gen.generate(date=date, topic=topic)
        logger.info(f"✓ 公众号文章生成完成：{article['title']}")
        
        # 生成短视频脚本
        video_script = self.video_script_gen.generate(date=date, topic=topic)
        logger.info(f"✓ 短视频脚本生成完成：{video_script['title']}")
        
        # 生成社交卡片文案
        social_cards = self.social_card_gen.generate(date=date, topic=topic)
        logger.info(f"✓ 社交卡片生成完成：共 {len(social_cards)} 张")
        
        # 格式化公众号文章
        formatted_article = self.formatter.format(article['content'])
        logger.info("✓ 公众号文章排版完成")
        
        # 保存结果
        output_dir = Path(self.config.get("output_dir", "./output")) / date
        output_dir.mkdir(parents=True, exist_ok=True)
        
        import json
        with open(output_dir / "article.md", "w", encoding="utf-8") as f:
            f.write(article['content'])
        with open(output_dir / "article_formatted.html", "w", encoding="utf-8") as f:
            f.write(formatted_article)
        with open(output_dir / "video_script.json", "w", encoding="utf-8") as f:
            json.dump(video_script, f, ensure_ascii=False, indent=2)
        with open(output_dir / "social_cards.json", "w", encoding="utf-8") as f:
            json.dump(social_cards, f, ensure_ascii=False, indent=2)
        
        logger.info(f"✓ 所有素材已保存到 {output_dir}")
        
        return {
            "article": article,
            "video_script": video_script,
            "social_cards": social_cards,
            "formatted_article": formatted_article,
        }
    
    def distribute(self, platforms: list = None, date: str = None):
        """
        分发素材到各平台
        
        Args:
            platforms: 平台列表 ['wechat', 'video', 'xiaohongshu']
            date: 日期，格式 YYYY-MM-DD
        """
        if not platforms:
            platforms = ['wechat', 'video', 'xiaohongshu']
        
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        output_dir = Path(self.config.get("output_dir", "./output")) / date
        
        logger.info(f"开始分发 {date} 的素材到平台：{platforms}")
        
        results = {}
        
        # 分发到微信公众号
        if 'wechat' in platforms:
            try:
                article_path = output_dir / "article_formatted.html"
                result = self.wechat_pub.publish(article_path)
                results['wechat'] = result
                logger.info(f"✓ 微信公众号发布完成：{result}")
            except Exception as e:
                logger.error(f"微信公众号发布失败：{e}")
                results['wechat'] = {"success": False, "error": str(e)}
        
        # 分发到视频平台
        if 'video' in platforms:
            try:
                script_path = output_dir / "video_script.json"
                result = self.video_uploader.upload(script_path)
                results['video'] = result
                logger.info(f"✓ 视频上传完成：{result}")
            except Exception as e:
                logger.error(f"视频上传失败：{e}")
                results['video'] = {"success": False, "error": str(e)}
        
        # 分发到小红书
        if 'xiaohongshu' in platforms:
            try:
                cards_path = output_dir / "social_cards.json"
                result 










































































































































































