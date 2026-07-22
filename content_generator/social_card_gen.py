#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
社交卡片生成模块
自动生成适合小红书/朋友圈的朗读训练图文卡片文案
"""

import logging
from datetime import datetime
from typing import Dict, Any, List
import random

logger = logging.getLogger(__name__)


class SocialCardGenerator:
    """社交卡片生成器"""
    
    def __init__(self, config: Dict[str, Any]):
        """
        初始化卡片生成器
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.api_key = config.get("api", {}).get("openai_key", "")
        self.model = config.get("api", {}).get("model", "gpt-4")
    
    def generate(self, date: str = None, topic: str = None) -> List[Dict[str, Any]]:
        """
        生成社交卡片
        
        Args:
            date: 日期，格式 YYYY-MM-DD
            topic: 主题（可选）
            
        Returns:
            包含多个卡片的列表，每个卡片包含标题、文案、标签等
        """
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        if not topic:
            topic = self._get_default_topic(date)
        
        logger.info(f"生成社交卡片 - 日期：{date}, 主题：{topic}")
        
        # 生成 3 张卡片
        cards = []
        
        # 卡片 1：金句卡片
        card1 = self._generate_quote_card(topic, date)
        cards.append(card1)
        
        # 卡片 2：方法卡片
        card2 = self._generate_method_card(topic, date)
        cards.append(card2)
        
        # 卡片 3：打卡卡片
        card3 = self._generate_checkin_card(topic, date)
        cards.append(card3)
        
        return cards
    
    def _get_default_topic(self, date: str) -> str:
        """根据日期获取默认主题"""
        topics = [
            "口才训练基础",
            "朗读技巧提升",
            "演讲表达能力",
            "沟通艺术",
            "声音魅力培养"
        ]
        day_of_year = datetime.strptime(date, "%Y-%m-%d").timetuple().tm_yday
        return topics[day_of_year % len(topics)]
    
    def _generate_quote_card(self, topic: str, date: str) -> Dict[str, Any]:
        """生成金句卡片"""
        quotes = {
            "口才训练基础": [
                "口才是可以通过练习不断提升的技能",
                "每天坚持朗读，遇见更好的自己",
                "表达力，是一个人的核心竞争力"
            ],
            "朗读技巧提升": [
                "好的朗读不是念文字，而是用声音传递情感",
                "声音是有温度的，你的声音有多温暖？",
                "朗读的最高境界是声情并茂"
            ],
            "演讲表达能力": [
                "演讲不是表演，而是真诚地分享",
                "每一次开口，都是展示自己的机会",
                "自信的表达，从接纳紧张开始"
            ],
            "沟通艺术": [
                "沟通的目的不是说服，而是理解",
                "会说话的人，走到哪里都受欢迎",
                "好的沟通让彼此都舒服"
            ],
            "声音魅力培养": [
                "声音是你的第二张脸，值得精心雕琢",
                "迷人的嗓音，是送给自己最好的礼物",
                "好声音需要日积月累，坚持必有回响"
            ]
        }
        
        quote_list = quotes.get(topic, ["坚持练习，必有收获"])
        
        return {
            "type": "quote",
            "title": f"Day {date} · 今日金句",
            "content": random.choice(quote_list),
            "image_text": f"""╔═══════════════════════╗
    Day {date}
   
   {random.choice(quote_list)}
   
   💪 坚持练习，遇见更好的自己
╚═══════════════════════╝""",
            "hashtags": ["#每日金句", "#口才训练", "#自我成长", "#朗读打卡"],
            "platforms": ["xiaohongshu", "wechat_moments"]
        }
    
    def _generate_method_card(self, topic: str, date: str) -> Dict[str, Any]:
        """生成方法卡片"""
        methods = {
            "口才训练基础": {
                "title": "3 个基础练习法",
                "content": """1️⃣ 绕口令练习
   四是四，十是十
   练平翘舌音
   
2️⃣ 朗读训练
   选一篇喜欢的文章
   注意停顿和重音
   
3️⃣ 即兴表达
   随机话题说 2 分钟
   录音回听找不足"""
            },
            "朗读技巧提升": {
                "title": "朗读三要素",
                "content": """️ 停顿
   逗号 0.5 秒，句号 1 秒
   给听众思考时间
   
🔊 重音
   强调关键词
   表达情感重点
   
🎵 语调
   陈述句下降
   疑问句上扬"""
            },
            "演讲表达能力": {
                "title": "克服紧张 3 招",
                "content": """1️⃣ 深呼吸
   吸气 4 秒→呼气 6 秒
   立刻缓解紧张
   
2️ 转变思维
   不是"我要完美"
   而是"我要分享"
   
3️⃣ 提前准备
   万能三段式框架
   开场 - 主体 - 结尾"""
            },
            "沟通艺术": {
                "title": "PREP 表达法",
                "content": """P Point 观点
   先说结论
   
R Reason 理由
   说明原因
   
E Example 例子
   举例佐证
   
P Point 重申
   再次强调"""
            },
            "声音魅力培养": {
                "title": "气息训练法",
                "content": """ 腹式呼吸
   手放腹部
   吸气鼓起呼气收缩
   
🔢 数数练习
   一口气数到 30+
   锻炼气息控制
   
 哼鸣练习
   闭嘴发"嗯"音
   找共鸣位置"""
            }
        }
        
        method = methods.get(topic, {
            "title": "今日训练",
            "content": "坚持练习\n每天进步一点点\n加油！"
        })
        
        return {
            "type": "method",
            "title": f"Day {date} · {method['title']}",
            "content": method["content"],
            "image_text": f"""╔═══════════════════════╗
   📚 Day {date}
   
   {method['title']}
   
{method['content']}
   
   💡 收藏起来，马上练习！
═══════════════════════╝""",
            "hashtags": ["#口才训练", "#学习方法", "#自我提升", "#干货分享"],
            "platforms": ["xiaohongshu", "wechat_moments"]
        }
    
    def _generate_checkin_card(self, topic: str, date: str) -> Dict[str, Any]:
        """生成打卡卡片"""
        checkin_templates = {
            "口才训练基础": """📝 今日打卡
✅ 绕口令练习
✅ 朗读训练
✅ 即兴表达
⭐ 自评：__/10 分""",
            "朗读技巧提升": """📝 今日打卡
✅ 停顿练习
✅ 重音练习
✅ 语调练习
⭐ 自评：__/10 分""",
            "演讲表达能力": """ 今日打卡
✅ 深呼吸放松
✅ 2 分钟演讲
✅ 录音回听
⭐ 自评：__/10 分""",
            "沟通艺术": """📝 今日打卡
✅ 倾听练习
✅ PREP 表达
✅ 记录反思
⭐ 自评：__/10 分""",
            "声音魅力培养": """📝 今日打卡
✅ 腹式呼吸
✅ 哼鸣练习
✅ 诗歌朗诵
⭐ 自评：__/10 分"""
        }
        
        checkin_content = checkin_templates.get(topic, f"""📝 今日打卡
✅ 完成训练
✅ 录音上传
✅ 写下收获
⭐ 自评：__/10 分""")
        
        return {
            "type": "checkin",
            "title": f"Day {date} · 打卡记录",
            "content": checkin_content,
            "image_text": f"""╔═══════════════════════╗
   ️ Day {date} 打卡
   
{checkin_content}
   
   💬 评论区交作业
   👇 一起进步！
╚═══════════════════════╝""",
            "hashtags": ["#学习打卡", "#自律", "#口才训练", "#成长记录"],
            "platforms": ["xiaohongshu", "wechat_moments"]
        }










































































































































































































































































