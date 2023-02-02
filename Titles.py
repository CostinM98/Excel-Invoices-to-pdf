from fpdf import FPDF

from pathlib import Path
import glob

filepaths = glob.glob('Text_files/*.txt')

pdf = FPDF(orientation="P", unit='mm', format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()


    pdf.set_font(family='times', size=20, style='B')
    pdf.cell(w=50, h=8, txt=name, ln=1)
    with open(filepath,'r') as file:
        content=file.read()
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=0, h=6, txt=content)



        pdf.cell(w=50, h=10, txt=name, ln=1)


pdf.output('output.pdf')
