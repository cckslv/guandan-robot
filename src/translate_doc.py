from docx import Document

doc = Document()
doc.add_heading('FP 401 Course Interview Report Template', 0)
doc.add_paragraph('FP401 Life and Career Planning - Experiential Learning')
doc.add_paragraph('Cook University (USA) Four-Year Comprehensive Course: Career Life Planning - Experiential Learning')

doc.add_heading('2023-2027 Junior Year FP 401 Interview Photos, Records', level=1)
doc.add_heading('and Post-Interview Reflection Report', level=1)

p = doc.add_paragraph()
p.add_run('Chinese Name: ').bold = True
p.add_run('郑心颖')
p = doc.add_paragraph()
p.add_run('Pinyin Name: ').bold = True
p.add_run('Zheng Xinying')

p = doc.add_paragraph()
p.add_run('Keuka ID: ').bold = True
p.add_run('0458091')
p = doc.add_paragraph()
p.add_run('Class: ').bold = True
p.add_run('2320')
p = doc.add_paragraph()
p.add_run('Phone: ').bold = True
p.add_run('19157678516')

p = doc.add_paragraph()
p.add_run('Email/QQ: ').bold = True
p.add_run('zxy20050519@qq.com')

p = doc.add_paragraph()
p.add_run('Chinese Partner University: ').bold = True
p.add_run('Jimei University')
p = doc.add_paragraph()
p.add_run('Enrollment Date: ').bold = True
p.add_run('2023.9')
p = doc.add_paragraph()
p.add_run('Expected Graduation: ').bold = True
p.add_run('2027.6')
p = doc.add_paragraph()
p.add_run('Submission Date: ').bold = True
p.add_run('2026.5.10')

doc.add_heading('1. My Interview Record (within 200 words)', level=1)
doc.add_paragraph(
    'During the interview, I introduced my experience of studying finance courses at school '
    'and developing rigorous work habits through practice. I also shared my plan to join '
    'Zhejiang Haibo Door Industry as an assistant to the Finance Director after graduation '
    'and grow into a professional finance professional. The professor suggested that my '
    'career plan should be practical, and advised me to adjust my long-term goals into '
    'specific plans within five years, avoiding empty talk. At the same time, the professor '
    'reminded me to pay attention to workplace etiquette and interpersonal communication '
    'after joining the company, and to proactively express gratitude to colleagues who helped me.')

doc.add_heading('2. My Post-Interview Reflection Report (within 300 words)', level=1)
doc.add_paragraph(
    "This interview made me deeply realize that career planning needs to be grounded and "
    "avoid being vague. Previously, my goals lacked phased breakdowns and were easily "
    "seen as impractical. The professor's advice awakened me - in the workplace, "
    "practical action plans and good interpersonal communication are equally important. "
    "I will refine my career goals into executable plans within five years, while also "
    "valuing the development of workplace etiquette and interpersonal skills. I will "
    "prepare for job hunting with a more rigorous and practical attitude, and steadily "
    "walk my career path.")

doc.add_heading('3. After the Interview, I Still Want to Say to Professor Tian (optional, within 200 words)', level=1)
doc.add_paragraph(
    'Thank you for your patient guidance and constructive suggestions, which helped me '
    'clearly recognize the shortcomings in my career planning. I will seriously take '
    'your advice, make my goals more specific and phased, while also valuing workplace '
    'etiquette and interpersonal communication. Thank you for your continuous help. '
    'I will carry the gains from this interview and prepare for job hunting with a more '
    'practical attitude, live up to your expectations.')

doc.save(r'D:\0458091 Zheng Xinying English Version.docx')
print('English version saved successfully!')
