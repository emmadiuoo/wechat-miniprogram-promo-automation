#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公众号文章生成模块
自动生成朗读训练相关的公众号文章
"""

import logging
from datetime import datetime
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


class ArticleGenerator:
    """公众号文章生成器"""
    
    def __init__(self, config: Dict[str, Any]):
        """
        初始化文章生成器
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.api_key = config.get("api", {}).get("openai_key", "")
        self.model = config.get("api", {}).get("model", "gpt-4")
    
    def generate(self, date: str = None, topic: str = None) -> Dict[str, str]:
        """
        生成公众号文章
        
        Args:
            date: 日期，格式 YYYY-MM-DD
            topic: 主题（可选）
            
        Returns:
            包含标题和内容的字典
        """
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        # 如果没有指定主题，根据日期生成默认主题
        if not topic:
            topic = self._get_default_topic(date)
        
        logger.info(f"生成文章 - 日期：{date}, 主题：{topic}")
        
        # 构建文章结构
        title = self._generate_title(topic, date)
        content = self._generate_content(topic, date)
        
        return {
            "title": title,
            "content": content,
            "topic": topic,
            "date": date
  }
    
    def _get_default_topic(self, date: str) -> str:
        """根据日期获取默认主题"""
        # 可以基于日期、节日、季节等生成主题
        topics = [
            "口才训练基础",
            "朗读技巧提升",
            "演讲表达能力",
            "沟通艺术",
            "声音魅力培养"
        ]
        
        # 简单轮询主题
        day_of_year = datetime.strptime(date, "%Y-%m-%d").timetuple().tm_yday
        return topics[day_of_year % len(topics)]
    
    def _generate_title(self, topic: str, date: str) -> str:
        """生成文章标题"""
        titles = {
            "口才训练基础": f"【Day {date}】口才训练从基础开始，每天进步一点点",
            "朗读技巧提升": f"【Day {date}】掌握这些朗读技巧，让你的声音更有感染力",
            "演讲表达能力": f"【Day {date}】演讲表达能力提升指南，告别紧张怯场",
            "沟通艺术": f"【Day {date}】高效沟通的艺术，让你更受欢迎",
            "声音魅力培养": f"【Day {date}】如何培养迷人的声音魅力？"
              }
        
        return titles.get(topic, f"【Day {date}】{topic}训练")
    
    def _generate_content(self, topic: str, date: str) -> str:
        """生成文章内容（Markdown 格式）"""
        
        content_templates = {
            "口才训练基础": self._generate_basic_content,
            "朗读技巧提升": self._generate_reading_skills_content,
            "演讲表达能力": self._generate_speech_content,
            "沟通艺术": self._generate_communication_content,
            "声音魅力培养": self._generate_voice_charm_content
              }
        
        generator = content_templates.get(topic, self._generate_basic_content)
        return generator(date)
    
    def _generate_basic_content(self, date: str) -> str:
        """生成口才训练基础内容"""
        return f"""# 口才训练从基础开始

##  训练日期：{date}

### 今日金句
> "口才是可以通过练习不断提升的技能，每天坚持，必有收获。"

### 一、口才训练的重要性

在现代社会，良好的口才能力是成功的关键因素之一。无论是在职场汇报、商务谈判，还是日常社交中，清晰的表达都能让我们脱颖而出。

### 二、今日训练内容

#### 1. 发音练习（5 分钟）
- 绕口令：四是四，十是十，十四是十四，四十是四十
- 练习要点：注意平翘舌音的区分，语速由慢到快

#### 2. 朗读训练（10 分钟）
**材料：**《春》朱自清（节选）
> 盼望着，盼望着，东风来了，春天的脚步近了。一切都像刚睡醒的样子，欣欣然张开了眼...

**要求：**
- 声音洪亮，吐字清晰
- 注意停顿和重音
- 带着感情朗读

#### 3. 即兴表达（5 分钟）
**话题：** "我最近读过的一本书"
- 思考 30 秒
- 连续说 2 分钟
- 录音回听，找出改进点

### 三、训练小贴士

✅ **保持微笑**：微笑能让你的声音更温暖
✅ **深呼吸**：说话前深呼吸，缓解紧张
✅ **眼神交流**：与人交谈时保持适当的眼神接触
✅ **语速适中**：不要太快，给听众理解的时间

### 四、打卡任务

完成以上训练后，请在小程序中打卡记录：
1. 上传朗读录音
2. 写下今日收获
3. 给自己打分（1-10 分）

---

**明日预告：** 朗读技巧提升——如何让声音更有感染力

💪 坚持就是胜利，明天继续加油！
"""
    
    def _generate_reading_skills_content(self, date: str) -> str:
        """生成朗读技巧内容"""
        return f"""# 掌握朗读技巧，让声音更有感染力

## 📅 训练日期：{date}

### 今日金句
> "好的朗读不是念文字，而是用声音传递情感。"

### 一、朗读的三大要素

#### 1. 停顿
停顿是朗读中的"标点符号"，恰当的停顿能：
- 给听众思考的时间
- 强调重点内容
- 营造节奏感

**练习方法：** 在逗号处停 0.5 秒，句号处停 1 秒，段落间停 2 秒

#### 2. 重音
重音是表达情感和强调重点的关键。

**示例：**
- "**我**爱你"（强调是我，不是别人）
- "我**爱**你"（强调情感强烈）
- "我爱**你**"（强调对象是你）

#### 3. 语调
语调的变化能让朗读更生动：
- 陈述句：平稳下降
- 疑问句：尾音上扬
- 感叹句：起伏明显

### 二、今日训练材料

**《将进酒》李白（节选）**
> 君不见黄河之水天上来，奔流到海不复回。
> 君不见高堂明镜悲白发，朝如青丝暮成雪。
> 人生得意须尽欢，莫使金樽空对月...

**朗读指导：**
1. 第一句气势磅礴，声音要洪亮
2. "君不见"要有呼唤感
3. "悲白发"语调下沉，表达感慨
4. "须尽欢"要读出豪迈之情

### 三、实战练习

🎯 **练习步骤：**
1. 默读全文，理解情感基调
2. 标记停顿和重音位置
3. 小声跟读 3 遍
4. 大声朗读并录音
5. 回听分析，找出不足

### 四、进阶技巧

🔥 **情感代入法：** 想象自己就是作者，体会当时的心境
🔥 **画面联想法：** 边读边想象诗中描绘的画面
🔥 **角色演绎法：** 把自己当成朗诵者，进行表演式朗读

---

**打卡任务：** 上传朗读录音，标注出你处理的停顿和重音位置

 记住：朗读的最高境界是"声情并茂"！
"""
    
    def _generate_speech_content(self, date: str) -> str:
        """

























































































































































































