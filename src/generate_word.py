from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION

def create_word():
    doc = Document()
    
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.left_margin = Inches(0.79)
    section.right_margin = Inches(0.79)
    section.top_margin = Inches(0.79)
    section.bottom_margin = Inches(0.79)

    title_style = doc.styles['Heading 1']
    title_font = title_style.font
    title_font.name = '黑体'
    title_font.size = Pt(16)
    title_font.bold = True

    subtitle_style = doc.styles['Heading 2']
    subtitle_font = subtitle_style.font
    subtitle_font.name = '黑体'
    subtitle_font.size = Pt(14)
    subtitle_font.bold = True

    content_style = doc.styles['Normal']
    content_font = content_style.font
    content_font.name = '宋体'
    content_font.size = Pt(12)

    doc.add_heading('灵爪灌金——基于OpenClaw的非遗智能灌蛋系统', level=1).alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph().alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_heading('第1页：非遗文化背景与项目缘起', level=2)
    doc.add_paragraph('灌蛋是福建南平顺昌县的省级非遗小吃，每逢春节元宵，家家户户都要煮上一锅，寓意团团圆圆、招财进宝。这道美食承载着浓浓的年味和家乡记忆。')
    doc.add_paragraph('做法看似简单：找到蛋眼，用筷子把肉馅灌进去，再下高汤煮熟。但真要做好，得练上几个月甚至几年。现在年轻人大多外出打工，愿意学这门手艺的越来越少，传统技艺眼看就要失传了。')
    doc.add_paragraph('我们的想法很简单：造一台能进厨房的家庭智能机器人，让它学会灌蛋这门手艺。我们用AUBO-i5H双臂协作机器人当手，用OpenClaw智能体当脑，让机器像学徒一样，从模仿老师傅开始，最终能独立完成找蛋眼、灌肉馅的全流程。')
    doc.add_paragraph('这不是冷冰冰的工厂流水线，而是未来能走进千家万户的家用智能助手。想象一下：除夕夜，老人按下启动键，机器人就能熟练地灌好一颗颗蛋，让团圆的味道留在更多人的记忆里。')
    placeholder = doc.add_paragraph('【此处插入暖色调年节氛围背景图】')
    placeholder.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in placeholder.runs:
        run.font.color.rgb = RGBColor(128, 128, 128)

    doc.add_section(WD_SECTION.NEW_PAGE)
    doc.add_heading('第2页：痛点分析与项目创意', level=2)
    doc.add_paragraph('说起灌蛋这门手艺，真是看着容易做着难。我小时候看奶奶做，觉得挺简单的，自己上手才知道有多不容易。')
    doc.add_paragraph('首先是找蛋眼难。每颗鸡蛋的蛋眼位置都不一样，有的在这边，有的在那边，肉眼根本看不出来。老师傅都是凭手感找，新手只能瞎碰。')
    doc.add_paragraph('然后是容易戳破蛋黄膜。那层膜薄得只有几十微米，比头发丝还细，筷子稍微抖一下，蛋黄就流出来了，这颗蛋就废了。')
    doc.add_paragraph('还有馅量也不好控制。灌多了会把膜撑破，灌少了又不够入味。全靠师傅的经验，没有标准可言。')
    doc.add_paragraph('所以我们就想，能不能让机器来学这门手艺？老师傅操作一遍，把最优的动作轨迹记录下来，再让OpenClaw智能体照着学、自己练。这样不管鸡蛋大小、蛋黄深浅，机器都能应付。')

    doc.add_section(WD_SECTION.NEW_PAGE)
    doc.add_heading('第3页：系统设计图', level=2)
    
    doc.add_heading('硬件架构', level=3)
    doc.add_paragraph('采用AUBO-i5H双臂协作机器人作为核心执行平台，具备6个自由度，单臂负载5.0kg，重复定位精度可达±0.02mm，支持拖动示教功能。')

    doc.add_heading('双臂分工', level=3)
    doc.add_paragraph('右臂搭载针筒灌馅模块，由医用级大容量针筒、自制夹持器、步进电机推杆和薄膜力传感器组成，完成穿刺、推注、退针的完整动作。')
    doc.add_paragraph('左臂配备工业相机和蛋定位夹具，负责识别蛋眼位置并固定鸡蛋，定位座采用负压式柔性吸盘确保稳定抓取。')

    doc.add_heading('控制中枢', level=3)
    doc.add_paragraph('上位机运行OpenClaw智能体，负责视觉识别、轨迹规划和双臂协调控制，实现精准的灌蛋操作。')

    placeholder = doc.add_paragraph('【此处插入整体场景设计图及针筒模块详图】')
    placeholder.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in placeholder.runs:
        run.font.color.rgb = RGBColor(128, 128, 128)

    doc.add_section(WD_SECTION.NEW_PAGE)
    doc.add_heading('第4页：操作流程图', level=2)
    
    doc.add_heading('核心原则', level=3)
    doc.add_paragraph('双臂依次移动，避免碰撞，确保操作安全。')

    doc.add_heading('单次灌馅循环', level=3)
    doc.add_paragraph('①取针筒 → ②准备吸取 → ③吸取肉泥 → ④移向鸡蛋 → ⑤灌入肉馅 → ⑥复位准备下一轮')

    doc.add_heading('详细流程阶段', level=3)
    doc.add_paragraph('阶段一（复位校准）：关节运动归位，夹爪校准，确保起始位置准确。')
    doc.add_paragraph('阶段二（吸取肉泥）：抓针筒插入肉馅，二次校准后抓取活塞柄，上拉吸馅后释放退出。')
    doc.add_paragraph('阶段三（灌入鸡蛋）：针尖移至蛋眼上方并精准插入，再次抓取活塞柄，平稳下推注馅后释放退出。')
    doc.add_paragraph('阶段四（复位收尾）：关节运动返回安全点，释放针筒，准备下一次操作。')

    placeholder = doc.add_paragraph('【此处插入操作流程分步示意图及三阶段演进图】')
    placeholder.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in placeholder.runs:
        run.font.color.rgb = RGBColor(128, 128, 128)

    doc.add_section(WD_SECTION.NEW_PAGE)
    doc.add_heading('第5页：效果图展示与性能优势', level=2)
    
    doc.add_paragraph('【针管前端特写：钝头针精准进入蛋眼】')
    doc.add_paragraph('标注：钝头圆口针、蛋黄膜、肉馅、力传感器')
    
    doc.add_paragraph('【成品灌蛋剖面图：银白蛋清包裹金黄蛋黄，中间肉馅饱满】')
    
    doc.add_paragraph('【成功案例：蛋黄内肉馅圆润集中】')
    doc.add_paragraph('【失败案例：蛋黄膜破裂，肉馅外溢】')
    
    for p in doc.paragraphs[-4:]:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.color.rgb = RGBColor(128, 128, 128)

    doc.add_heading('性能优势', level=3)
    doc.add_paragraph('重复定位精度达到±0.02mm，远超人手操作精度，确保每次穿刺位置准确无误。')
    doc.add_paragraph('预期灌馅成功率超过95%，相比新手人工约50%的成功率有显著提升。')
    doc.add_paragraph('钝头针穿刺直径仅1.2mm，远小于传统筷子的5-8mm，大大降低蛋黄膜破裂风险。')

    doc.add_section(WD_SECTION.NEW_PAGE)
    doc.add_heading('第6页：总结与展望', level=2)
    doc.add_paragraph('这个项目的技术灵魂是OpenClaw的自主学习能力。不是预设每一条轨迹，而是让机器在观察中理解、在尝试中改进，这种学习方式与人类学徒的成长过程极为相似。')
    doc.add_paragraph('非遗传承的方式正在发生改变。过去只能在师徒之间口传心授的技艺，如今可以通过数据流动实现更广范围的传播。机器学会的不只是灌蛋的动作，更是对传统技艺的数字化记录与传承。')
    doc.add_paragraph('本项目基于OpenClaw智能体平台构建，相关技术已形成学术论文和专利申请。论文深入探讨了模仿学习与强化学习结合的机器人操作学习方法，专利申请已通过预审阶段，为技术落地提供了知识产权保障。')
    doc.add_paragraph('AUBO-i5H机器人体积适中，成本可控，具备家用级可行性。我们想象这样的画面：除夕夜，老人按下启动键，机械臂熟练地灌好一颗颗蛋，飘散出熟悉的家乡味道。')
    doc.add_paragraph('孙子在旁边好奇地看着，问奶奶这是什么。奶奶笑着说，这是我们老家的味道，是奶奶的奶奶传下来的手艺。这份记忆，通过机器得以延续。')
    doc.add_paragraph('在应用前景上，短期可作为餐饮半自动工位使用，提升餐厅后厨效率；中期发展为家庭桌面机，让更多家庭能够方便地制作灌蛋；长期则形成"数据+模型"的非遗传承新范式。')
    doc.add_paragraph('核心技术还可迁移至医用精密注射、食品定量灌装等场景，实现跨领域的技术复用。这不仅是对灌蛋技艺的传承，更是对智能机器人应用于非遗保护的一次有益探索。')
    
    closing = doc.add_paragraph('机器学会的不只是动作，是团圆的记忆。')
    closing.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in closing.runs:
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = RGBColor(139, 69, 19)

    doc.add_section(WD_SECTION.NEW_PAGE)
    doc.add_heading('附件：AI使用声明', level=2)
    
    doc.add_heading('一、使用的AI工具名称及版本', level=3)
    doc.add_paragraph('1. OpenClaw（自主搭建智能体平台）')
    doc.add_paragraph('2. GLM-5.1（辅助技术内容生成）')
    doc.add_paragraph('3. Kimi-K2.5 / MiniMax-M2.5（辅助创意文案生成）')
    doc.add_paragraph('4. Qwen3.5-397B（全文润色整合）')

    doc.add_heading('二、AI辅助环节单独说明', level=3)
    doc.add_paragraph('1. 设计方向探索：用OpenClaw梳理技术路线')
    doc.add_paragraph('2. 文档表达优化：用GLM/Kimi生成初稿、Qwen润色')
    doc.add_paragraph('3. 代码生成：脚本由人类在工艺魔方中手动编写，OpenClaw负责完善脚本并执行')
    doc.add_paragraph('4. 图像生成：不适用（使用实拍照片）')
    doc.add_paragraph('5. 资料查找与整合：用AI辅助收集灌蛋非遗背景资料')

    doc.add_heading('三、AI生成内容的原始记录', level=3)
    doc.add_paragraph('【待补充：关键对话截图（提示词和AI回复）】')
    doc.add_paragraph('【待补充：工作流截图】')
    doc.add_paragraph('【待补充：OpenClaw智能体平台说明（负责学习灌馅轨迹、阶段二模仿学习、阶段三强化学习）】')

    doc.add_heading('四、自主贡献说明', level=3)
    doc.add_paragraph('核心创意（针筒替代筷子、双臂协作灌馅、三阶段学习路径）均为原创，非AI启发。团队对AI生成内容进行了筛选、修改、重组和再创作，所有技术方案和文档主体均经过人工深度优化。')

    doc.add_heading('五、学术与知识产权成果', level=3)
    
    doc.add_heading('1. 学术论文', level=4)
    doc.add_paragraph('Abstract—Distributed multi-terminal intelligent collaboration is a key technology to improve the efficiency and resource allocation ability of intelligent systems. This paper takes the OpenClaw mother-child claw master-slave distributed architecture as the research object, and uses Deep Q-Network (DQN) algorithm to construct scene-based collaborative decision-making model.')
    doc.add_paragraph('By customizing the state representation, action space and reward function of the collaborative scene, it enables intelligent scheduling, rapid response and permission security control of mother claw and child claw. Genetic algorithm (GA), Q-learning and Transformer cooperative decision algorithms are selected as the comparative benchmarks.')
    doc.add_paragraph('The results show that the proposed model achieves a cooperative task completion rate of 95.28%, an average response delay of 62.35ms and a privilege access success rate of 96.89%, which are significantly better than the comparison algorithm.')
    doc.add_paragraph('In the 10–30 claw terminal expansion scenario, the model performance fluctuates slightly and has good anti-interference ability. The model can effectively improve the cooperative efficiency and operation stability of OpenClaw system, and can provide feasible technical solutions for similar master-slave distributed terminal cooperation.')
    doc.add_paragraph('Keywords—OpenClaw, Mother-Child Claw, DQN Algorithm, Intelligent Cooperation')
    
    doc.add_heading('2. 专利申请', level=4)
    doc.add_paragraph('专利名称：一种分层技能调度的OpenClaw接入系统及方法')
    doc.add_paragraph('预审案件号：YS06420261001006')
    doc.add_paragraph('申请主体：厦门工学院')
    doc.add_paragraph('提交日期：2026年04月27日')
    doc.add_paragraph('预审通过日期：2026年05月08日')
    doc.add_paragraph('审批机构：厦门市知识产权保护中心')
    doc.add_paragraph('【此处插入专利预审通过通知书扫描件】')

    doc.save('灵爪灌金_参赛材料_v3.docx')
    print('Word文档生成成功！')

if __name__ == '__main__':
    create_word()