from fpdf import FPDF
from fpdf.fonts import FontFace

class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_margins(20, 20, 20)
        self.add_font('SimHei', '', r'C:\Windows\Fonts\simhei.ttf')
        self.alias_nb_pages()
    
    def header(self):
        self.set_font('SimHei', '', 10)
        self.cell(0, 10, '灵爪灌金——基于OpenClaw的非遗智能灌蛋系统', 0, 1, 'C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font('SimHei', '', 8)
        self.cell(0, 10, f'第 {self.page_no()} 页 / 共 {{nb}} 页', 0, 0, 'C')

def create_pdf():
    pdf = PDF()
    
    pdf.add_page()
    pdf.set_font('SimHei', '', 16)
    pdf.set_fill_color(255, 248, 220)
    pdf.cell(0, 20, '非遗文化背景与项目缘起', 0, 1, 'C', fill=True)
    pdf.ln(10)
    pdf.set_font('SimHei', '', 12)
    content = """灌蛋是福建南平顺昌县的省级非遗小吃。每逢春节元宵，家家户户都要煮上一锅——寓意团团圆圆、招财进宝。做法看似简单：找到蛋眼，用筷子把肉馅灌进去，再下高汤煮熟。但真要做好，得练上几个月甚至几年。年轻人大多外出打工，愿意学这门手艺的越来越少。

我们想做点什么。不是拍纪录片，也不是建数据库。我们想造一台能真正“学会”灌蛋的机器人。用AUBO-i5H双臂协作机器人当手，用OpenClaw智能体当脑，让机器从模仿开始，最终能独立完成找蛋眼、灌肉馅的全流程。

这不仅是自动化。如果机器能学会，意味着这门手艺可以被记录、被复制、被传播。师徒之间的口传心授，或许可以变成人机之间的数据流动。我们想让灌蛋的味道，留在更多人的记忆里。"""
    pdf.multi_cell(0, 10, content)
    pdf.set_fill_color(211, 211, 211)
    pdf.cell(0, 60, '【此处插入暖色调年节氛围背景图】', 1, 1, 'C', fill=True)

    pdf.add_page()
    pdf.set_font('SimHei', '', 16)
    pdf.set_fill_color(255, 248, 220)
    pdf.cell(0, 20, '痛点分析与项目创意', 0, 1, 'C', fill=True)
    pdf.ln(5)
    pdf.set_font('SimHei', '', 14)
    pdf.cell(0, 12, '三大痛点', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    pain_points = [
        '找眼难：每颗蛋的蛋眼位置都不同，肉眼很难一眼找准，筷子定位全凭老师傅的手感。',
        '易破膜：蛋黄膜薄至50-80微米，筷子稍微抖一下就会戳破，蛋黄流出则蛋废。',
        '馅量不稳：馅量多少没有标准，全靠经验，新手易灌太多撑破膜或灌太少影响口感。'
    ]
    for i, point in enumerate(pain_points, 1):
        pdf.cell(0, 10, f'{i}. {point}', 0, 1, 'L')
    
    pdf.ln(5)
    pdf.set_font('SimHei', '', 14)
    pdf.cell(0, 12, '三大亮点', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    highlights = [
        'OpenClaw模仿学习：先让人类师傅操作一遍，记录最优轨迹，再让智能体照着学、自己练。鸡蛋大小、蛋黄深浅变化，固定程序应付不了，但学习型智能体可以。',
        '传承新范式：师傅带一个徒弟要几个月，徒弟还不一定学得会。机器学会后，一人一机即可复现整套流程，传承不再受限于师资。',
        '家用定位：从一开始就瞄准家用场景，用针筒简化操作，搭配轻量型机械臂，安全简单，不是工厂流水线的庞然大物。'
    ]
    for i, highlight in enumerate(highlights, 1):
        pdf.cell(0, 10, f'{i}. {highlight}', 0, 1, 'L')

    pdf.add_page()
    pdf.set_font('SimHei', '', 16)
    pdf.set_fill_color(255, 248, 220)
    pdf.cell(0, 20, '系统设计图', 0, 1, 'C', fill=True)
    pdf.ln(10)
    pdf.set_font('SimHei', '', 13)
    pdf.cell(0, 12, '硬件架构', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    pdf.cell(0, 10, '采用AUBO-i5H双臂协作机器人作为核心执行平台。6个自由度，单臂负载5.0kg，重复定位精度±0.02mm，支持拖动示教。', 0, 1, 'L')
    
    pdf.ln(3)
    pdf.set_font('SimHei', '', 13)
    pdf.cell(0, 12, '双臂分工', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    pdf.cell(0, 10, '右臂：搭载针筒灌馅模块，由医用级大容量针筒、自制夹持器、步进电机推杆和薄膜力传感器组成，完成穿刺→推注→退针。', 0, 1, 'L')
    pdf.cell(0, 10, '左臂：配备工业相机和蛋定位夹具，识别蛋眼位置并固定鸡蛋。定位座采用负压式柔性吸盘。', 0, 1, 'L')
    
    pdf.ln(3)
    pdf.set_font('SimHei', '', 13)
    pdf.cell(0, 12, '控制中枢', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    pdf.cell(0, 10, '上位机运行OpenClaw智能体，负责视觉识别、轨迹规划和双臂协调。', 0, 1, 'L')
    
    pdf.ln(10)
    pdf.set_fill_color(211, 211, 211)
    pdf.cell(0, 80, '【此处插入整体场景设计图及针筒模块详图】', 1, 1, 'C', fill=True)

    pdf.add_page()
    pdf.set_font('SimHei', '', 16)
    pdf.set_fill_color(255, 248, 220)
    pdf.cell(0, 20, '操作流程图', 0, 1, 'C', fill=True)
    pdf.ln(10)
    pdf.set_font('SimHei', '', 13)
    pdf.cell(0, 12, '核心原则', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    pdf.cell(0, 10, '双臂依次移动，避免碰撞。', 0, 1, 'L')
    
    pdf.ln(3)
    pdf.set_font('SimHei', '', 13)
    pdf.cell(0, 12, '单次灌馅循环（6步）', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    steps = ['①取针筒', '②准备吸取', '③吸取肉泥', '④移向鸡蛋', '⑤灌入', '⑥复位准备下一轮']
    pdf.cell(0, 10, ' → '.join(steps), 0, 1, 'L')
    
    pdf.ln(3)
    pdf.set_font('SimHei', '', 13)
    pdf.cell(0, 12, '详细27步脚本流程', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    phases = [
        '阶段一（复位校准）：关节运动归位，夹爪校准。',
        '阶段二（吸取肉泥）：抓针筒插入肉馅，二次校准后抓取活塞柄，上拉吸馅后释放退出。',
        '阶段三（灌入鸡蛋）：针尖移至蛋眼上方并插入，再次抓取活塞柄，下推注馅后释放退出。',
        '阶段四（复位收尾）：关节运动返回安全点，释放针筒。'
    ]
    for phase in phases:
        pdf.cell(0, 10, phase, 0, 1, 'L')
    
    pdf.ln(3)
    pdf.set_font('SimHei', '', 13)
    pdf.cell(0, 12, '三阶段技术路线', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    pdf.cell(0, 10, '人类拖动示教 → OpenClaw模仿学习 → 强化学习泛化', 0, 1, 'L')
    
    pdf.ln(10)
    pdf.set_fill_color(211, 211, 211)
    pdf.cell(0, 60, '【此处插入操作流程分步示意图及三阶段演进图】', 1, 1, 'C', fill=True)

    pdf.add_page()
    pdf.set_font('SimHei', '', 16)
    pdf.set_fill_color(255, 248, 220)
    pdf.cell(0, 20, '效果图展示与性能优势', 0, 1, 'C', fill=True)
    pdf.ln(10)
    
    pdf.set_fill_color(211, 211, 211)
    pdf.cell(85, 40, '【针管前端特写：钝头针精准进入蛋眼】\n标注：钝头圆口针、蛋黄膜、肉馅、力传感器', 1, 0, 'C', fill=True)
    pdf.cell(5, 40, '', 0, 0)
    pdf.cell(85, 40, '【成品灌蛋剖面图：银白蛋清包裹金黄蛋黄】', 1, 1, 'C', fill=True)
    
    pdf.ln(5)
    pdf.cell(85, 40, '【成功案例：蛋黄内肉馅圆润集中】', 1, 0, 'C', fill=True)
    pdf.cell(5, 40, '', 0, 0)
    pdf.cell(85, 40, '【失败案例：蛋黄膜破裂，肉馅外溢】', 1, 1, 'C', fill=True)
    
    pdf.ln(10)
    pdf.set_font('SimHei', '', 13)
    pdf.cell(0, 12, '性能优势', 0, 1, 'L')
    pdf.set_font('SimHei', '', 11)
    specs = [
        '重复定位精度：±0.02mm（远超人手）',
        '预期灌馅成功率：> 95%（新手人工约50%）',
        '单次灌馅全流程：约15-20秒',
        '钝头针穿刺直径：仅1.2mm（传统筷子5-8mm）'
    ]
    for spec in specs:
        pdf.cell(0, 10, spec, 0, 1, 'L')

    pdf.add_page()
    pdf.set_font('SimHei', '', 16)
    pdf.set_fill_color(255, 248, 220)
    pdf.cell(0, 20, '总结与展望', 0, 1, 'C', fill=True)
    pdf.ln(10)
    pdf.set_font('SimHei', '', 12)
    content = """这个项目的技术灵魂是OpenClaw的自主学习能力。不是预设每一条轨迹，而是让机器在观察中理解、在尝试中改进。非遗传承从师徒之间，走向了人机之间。

AUBO-i5H体积适中，成本可控，具备家用级可行性。我们想象这样的画面：除夕夜，老人按下启动键，机械臂熟练地灌好一颗颗蛋。孙子在旁边看，问奶奶这是什么。奶奶说，这是我们老家的味道。

应用前景上，短期可做餐饮半自动工位，中期发展家庭桌面机，长期形成“数据+模型”的非遗传承新范式。核心技术还可迁移至医用精密注射、食品定量灌装等场景。"""
    pdf.multi_cell(0, 10, content)
    pdf.ln(20)
    pdf.set_font('SimHei', '', 18)
    pdf.set_text_color(139, 69, 19)
    pdf.cell(0, 20, '机器学会的不只是动作，是团圆的记忆。', 0, 1, 'C')

    pdf.add_page()
    pdf.set_font('SimHei', '', 16)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 20, '附件：AI使用声明', 0, 1, 'C', fill=True)
    pdf.ln(10)
    
    pdf.set_font('SimHei', '', 12)
    ai_declaration = """一、使用的AI工具名称及版本
1. OpenClaw（自主搭建智能体平台）
2. GLM-5.1（辅助技术内容生成）
3. Kimi-K2.5 / MiniMax-M2.5（辅助创意文案生成）
4. Qwen3.5-397B（全文润色整合）

二、AI辅助环节单独说明
1. 设计方向探索：用OpenClaw梳理技术路线
2. 文档表达优化：用GLM/Kimi生成初稿、Qwen润色
3. 代码生成：不适用（脚本由人类在工艺魔方中手动编写）
4. 图像生成：不适用（使用实拍照片）
5. 资料查找与整合：用AI辅助收集灌蛋非遗背景资料

三、AI生成内容的原始记录
【待补充：关键对话截图（提示词和AI回复）】
【待补充：工作流截图】
【待补充：OpenClaw智能体平台说明（负责学习灌馅轨迹、阶段二模仿学习、阶段三强化学习）】

四、自主贡献说明
核心创意（针筒替代筷子、双臂协作灌馅、三阶段学习路径）均为原创，非AI启发。团队对AI生成内容进行了筛选、修改、重组和再创作，所有技术方案和文档主体均经过人工深度优化。"""
    pdf.multi_cell(0, 10, ai_declaration)

    pdf.output('灵爪灌金_参赛材料.pdf')
    print('PDF生成成功！')

if __name__ == '__main__':
    create_pdf()