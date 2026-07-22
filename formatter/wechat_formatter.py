#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号排版格式化模块
将 Markdown 格式转换为适合微信公众号的 HTML 排版
参考 wechat-formatter 项目实现
"""

import logging
from typing import Dict, Any, Optional
import re

logger = logging.getLogger(__name__)


class WechatFormatter:
    """微信公众号排版格式化器"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        初始化格式化器
        
        Args:
            config: 配置字典（可选）
        """
        self.config = config or {}
        self.template_id = self.config.get("template_id", "default")
        
        # 定义样式模板
        self.templates = self._load_templates()
        
        logger.info(f"微信排版格式化器初始化完成，使用模板：{self.template_id}")
    
    def _load_templates(self) -> Dict[str, Dict[str, str]]:
        """加载排版模板"""
        return {
            "default": {
                "h1": '<section style="font-size: 20px; font-weight: bold; color: #333; border-left: 4px solid #4CAF50; padding-left: 12px; margin: 20px 0;">{content}</section>',
                "h2": '<section style="font-size: 18px; font-weight: bold; color: #555; margin: 16px 0;">{content}</section>',
                "h3": '<section style="font-size: 16px; font-weight: bold; color: #666; margin: 14px 0;">{content}</section>',
                "p": '<section style="font-size: 15px; line-height: 1.8; color: #333; margin: 12px 0;">{content}</section>',
                "quote": '<section style="background-color: #f5f5f5; padding: 12px 16px; border-left: 3px solid #ddd; margin: 16px 0; color: #666; font-style: italic;">{content}</section>',
                "strong": '<span style="font-weight: bold; color: #4CAF50;">{content}</span>',
                "list_item": '<section style="margin: 8px 0; padding-left: 20px; position: relative;">• {content}</section>',
            },
            "文艺风": {
                "h1": '<section style="font-size: 22px; font-weight: bold; color: #2c3e50; text-align: center; margin: 24px 0; letter-spacing: 2px;">{content}</section>',
                "h2": '<section style="font-size: 18px; font-weight: bold; color: #34495e; border-bottom: 1px dashed #bdc3c7; padding-bottom: 8px; margin: 18px 0;">{content}</section>',
                "h3": '<section style="font-size: 16px; font-weight: bold; color: #7f8c8d; margin: 14px 0;">{content}</section>',
                "p": '<section style="font-size: 15px; line-height: 2; color: #2c3e50; margin: 14px 0; text-indent: 2em;">{content}</section>',
                "quote": '<section style="background-color: #ecf0f1; padding: 16px 20px; border-radius: 4px; margin: 18px 0; color: #7f8c8d; font-style: italic; text-align: center;">"{content}"</section>',
                "strong": '<span style="font-weight: bold; color: #e74c3c;">{content}</span>',
                "list_item": '<section style="margin: 10px 0; padding-left: 24px; position: relative;"> {content}</section>',
            },
            "商务风": {
                "h1": '<section style="font-size: 20px; font-weight: bold; color: #1a73e8; background: linear-gradient(to right, #1a73e8, #4285f4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 20px 0;">{content}</section>',
                "h2": '<section style="font-size: 17px; font-weight: bold; color: #1a73e8; margin: 16px 0;">▌ {content}</section>',
                "h3": '<section style="font-size: 15px; font-weight: bold; color: #5f6368; margin: 14px 0;">{content}</section>',
                "p": '<section style="font-size: 14px; line-height: 1.75; color: #3c4043; margin: 12px 0;">{content}</section>',
                "quote": '<section style="border: 1px solid #dadce0; padding: 12px 16px; margin: 16px 0; color: #5f6368; background-color: #f8f9fa;">{content}</section>',
                "strong": '<span style="font-weight: bold; color: #1a73e8;">{content}</span>',
                "list_item": '<section style="margin: 8px 0; padding-left: 20px; position: relative;">✓ {content}</section>',
            }
        }
    
    def format(self, markdown_content: str, template_name: str = None) -> str:
        """
        将 Markdown 格式转换为微信公众号 HTML
        
        Args:
            markdown_content: Markdown 格式的文本
            template_name: 模板名称（默认使用初始化的模板）
            
        Returns:
            HTML 格式的文本
        """
        if template_name:
            template = self.templates.get(template_name, self.templates["default"])
        else:
            template = self.templates.get(self.template_id, self.templates["default"])
        
        logger.info(f"开始格式化内容，使用模板：{template_name or self.template_id}")
        
        # 处理各级标题
        html = self._process_headings(markdown_content, template)
        
        # 处理引用
        html = self._process_quotes(html, template)
        
        # 处理粗体
        html = self._process_bold(html, template)
        
        # 处理列表
        html = self._process_lists(html, template)
        
        # 处理段落
        html = self._process_paragraphs(html, template)
        
        # 处理分隔线
        html = self._process_dividers(html)
        
        # 处理 emoji 和特殊符号
        html = self._preserve_emojis(html)
        
        logger.info("格式化完成")
        return html
    
    def _process_headings(self, content: str, template: Dict) -> str:
        """处理标题"""
        # H1
        content = re.sub(
            r'^# (.+)$',
            lambda m: template["h1"].format(content=m.group(1).strip()),
            content,
            flags=re.MULTILINE
        )
        # H2
        content = re.sub(
            r'^## (.+)$',
            lambda m: template["h2"].format(content=m.group(1).strip()),
            content,
            flags=re.MULTILINE
        )
        # H3
        content = re.sub(
            r'^### (.+)$',
            lambda m: template["h3"].format(content=m.group(1).strip()),
            content,
            flags=re.MULTILINE
        )
        return content
    
    def _process_quotes(self, content: str, template: Dict) -> str:
        """处理引用"""
        def replace_quote(match):
            quote_text = match.group(1).strip()
            # 移除引用符号 >
            quote_text = re.sub(r'^>\s*', '', quote_text, flags=re.MULTILINE)
            return template["quote"].format(content=quote_text)
        
        content = re.sub(
            r'> (.+?)(?=\n\n|\Z)',
            replace_quote,
            content,
            flags=re.DOTALL
        )
        return content
    
    def _process_bold(self, content: str, template: Dict) -> str:
        """处理粗体"""
        content = re.sub(
            r'\*\*(.+?)\*\*',
            lambda m: template["strong"].format(content=m.group(1)),
            content
        )
        return content
    
    def _process_lists(self, content: str, template: Di
























































































































































