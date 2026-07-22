#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
短视频脚本生成模块
自动生成适合视频号/抖音的朗读训练短视频脚本
"""

import logging
from datetime import datetime
from typing import Dict, Any, List
import random

  logger = logging.getLogger(__name__)


class VideoScriptGenerator:
    """短视频脚本生成器"""
    
  def __init__(self, config: Dict[str, Any]):
        """
        初始化脚本生成器
        
        Args:
            config: 配置字典
        """
        self.config = config
          self.api_key = config.get("api", {}).get("openai_key", "")
            self.model = config.get("api", {}).get("model", "gpt-4")
    
              def generate(self, date: str = None, topic: str = None) -> Dict[str, Any]:
        """
        生成短视频脚本
        
        Args:
            date: 日期，格式 YYYY-MM-DD
            topic: 主题（可选）
            
        Returns:
            包含标题、文案、标签等信息的字典
        """
        if not date:
          date = datetime.now().strftime("%Y-%m-%d")
        
        if not topic:
          topic = self._get_default_topic(date)
        
          logger.info(f"生成视频脚本 - 日期：{date}, 主题：{topic}")
        
        # 生成脚本各部分
          title = self._generate_title(topic, date)
          hook = self._generate_hook(topic)
          content = self._generate_content(topic, date)
          call_to_action = self._generate_cta()
          hashtags = self._generate_hashtags(topic)
        
          return {
            "title": title,
            "hook": hook,
            "content": content,
            "call_to_action": call_to_action,
            "hashtags": hashtags,
            "topic": topic,
            "date": date,
            "duration": "30-60 秒"
          }
    
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
    
          def _generate_title(self, topic: str, date: str) -> str:
        """生成视频标题"""
          titles = {
            "口才训练基础": f"每天 5 分钟，口才变好了！Day{date}",
            "朗读技巧提升": f"这样朗读，声音超有感染力！Day{date}",
            "演讲表达能力": f"告别紧张怯场，演讲超自信！Day{date}",
            "沟通艺术": f"高情商沟通技巧，太实用了！Day{date}",
            "声音魅力培养": f"如何拥有迷人嗓音？试试这个方法！Day{date}"
          }
          return titles.get(topic, f"口才训练打卡 Day{date}")
    
          def _generate_hook(self, topic: str) -> str:
        """生成视频开头钩子（前 3 秒吸引注意力）"""
          hooks = {
            "口才训练基础": [
                "你是不是说话总是没底气？",
                "为什么别人说话那么有说服力？",
                "3 个方法，让你的表达更清晰！"
            ],
            "朗读技巧提升": [
                "这样朗读，声音好听到停不下来！",
                "90% 的人都忽略的朗读技巧！",
                "学会这招，你的声音更有磁性！"
            ],
            "演讲表达能力": [
                "上台就紧张？这个方法亲测有效！",
                "演讲高手从不告诉你的秘密！",
                "3 步克服演讲紧张，超简单！"
            ],
            "沟通艺术": [
                "这样说话，没人会拒绝你！",
                "高情商的人都是这样沟通的！",
                "一句话让人对你好感倍增！"
            ],
            "声音魅力培养": [
                "声音不好听？坚持这个练习！",
                "每天 1 分钟，声音越来越好听！",
                "揭秘好声音的养成秘诀！"
            ]
          }
          return random.choice(hooks.get(topic, ["今天来聊聊口才训练"]))
    
          def _generate_content(self, topic: str, date: str) -> str:
        """生成视频主体内容"""
          contents = {
            "口才训练基础": f"""【镜头 1】主播面对镜头
            👤 "大家好，今天是口才训练的第{date}天！"

【镜头 2】展示练习内容
📝 "今天的训练内容很简单："
"第一，绕口令练习 - 四是四，十是十"
"第二，朗读一段文字，注意停顿和重音"
"第三，即兴表达 2 分钟"

【镜头 3】示范朗读
🎙️ "跟我一起读：盼望着，盼望着..."
（配上优美的背景音乐）

【镜头 4】回到主播
💡 "记住，口才是练出来的，不是看出来的！"
"每天坚持，你也能成为表达高手！""",
            
            "朗读技巧提升": f"""【镜头 1】吸引注意
👤 "为什么你的朗读没有感情？"
"因为你忽略了这 3 个要素！"

【镜头 2】讲解停顿
⏸️ "第一是停顿"
"逗号停半秒，句号停一秒"
"给听众思考和消化的时间"

【镜头 3】讲解重音
🔊 "第二是重音"
"'我爱你'，重音不同，意思完全不同"
（示范 3 种读法）

【镜头 4】讲解语调
 "第三是语调"
"陈述句下降，疑问句上扬"
"让声音有起伏，才动听"

【镜头 5】总结
✨ "今天就到这，快去试试吧！"
"记得在评论区交作业哦～""",
            
            "演讲表达能力": f"""【镜头 1】痛点切入
😰 "一上台就大脑空白？"
"手心出汗，心跳加速？"

【镜头 2】给出方案
💪 "分享 3 个我亲测有效的方法！"

【镜头 3】方法一
1️⃣ "深呼吸：吸气 4 秒，呼气 6 秒"
"立刻缓解紧张"

【镜头 4】方法二
2️⃣ "转变思维：不是'我要表现完美'"
"而是'我要分享价值'"

【镜头 5】方法三
3️⃣ "提前准备万能框架"
"开场 - 主体 - 结尾，三段式搞定"

【镜头 6】鼓励
🔥 "演讲是技能，不是天赋！"
"多练几次，你也能侃侃而谈！""",
            
            "沟通艺术": f"""【镜头 1】场景引入
💬 "为什么有些人说话让人如沐春风？"

【镜头 2】核心观点
🎯 "因为他们掌握了这个公式！"
"PREP 表达法"

【镜头 3】详细讲解
P "Point - 先说结论"
R "Reason - 再说原因"
E "Example - 举个例子"
P "Point - 重申结论"

【镜头 4】示范应用
🗣️ "比如推荐方案 A:"
'我认为应该选 A（结论）'
'因为它成本低效率高（原因）'
'上次类似项目...（例子）'
'所以 A 是最优选择（重申）'

【镜头 5】结尾
✅ "学会 PREP，表达更清晰！"
"点赞收藏，用起来！""",
            
            "声音魅力培养": f"""【镜头 1】引起兴趣
🎤 "想拥有迷人的声音吗？"
"其实很简单！"

【镜头 2】气息练习
💨 "第一步：腹式呼吸"
"手放腹部，吸气鼓起，呼气收缩"
"每天 5 分钟，气息更稳"

【镜头 3】共鸣练习
🔔 "第二步：哼鸣练习"
"闭嘴发'嗯——'音"
"感受鼻腔震动"

【镜头 4】综合训练
📖 "第三步：边朗读边运用"
"用气息支撑，找到共鸣"
"声音立马饱满起来"

【镜头 5】鼓励坚持
🌟 "声音是练出来的！"
"坚持一周，效果惊人！"
"评论区打卡，一起进步！""",
          }
        
          return contents.get(topic, f"【镜头 1】开场\n \"今天是口才训练 Day{date}\"\n\n【镜头 2】内容讲解\n📝 讲解训练要点\n\n【镜头 3】示范\n🎙️ 示范朗读或表达\n\n【镜头 4】总结\n✨ \"坚持练习，必有收获！\"")
    
          def _generate_cta(self) -> str:
        """生成行动号召"""
          ctas = [
            "点击左下角，加入朗读训练营！",
            "关注我，每天提升一点点！",
            "评论区打卡，见证你的成长！",
            "转发给需要的朋友，一起进步！",
            "私信我，领取更多训练资料！"
          ]
          return random.choice(ctas)
    
          def _generate_hashtags(self, topic: str) -> List[str]:
        """生成话题标签"""
          base_tags = ["#口才训练", "#朗读", "#表达力", "#自我提升", "#学习打卡"]
        
          topic_tags = {
            "口才训练基础": ["#演讲", "#沟通技巧", "#职场技能"],
            "朗读技巧提升": ["#朗诵", "#声音美化", "#配音"],
            "演讲表达能力": ["#公开演讲", "#克服紧张", "#自信心"],
            "沟通艺术": ["#高情商", "#人际关系", "#社交技巧"],
            "声音魅力培养": ["#声音训练", "#播音主持", "#嗓音美化"]
          }
        
          return base_tags + topic_tags.get(topic, [])











































































































































































































































