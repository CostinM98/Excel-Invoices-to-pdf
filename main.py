import pandas as pd
from fpdf import FPDF

from pathlib import Path
import glob

filepaths = glob.glob('invoices/*.xlsx')


for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name='Sheet 1')
    pdf=FPDF(orientation='p',unit='mm',format='A4')
    pdf.add_page()

    filename=Path(filepath).stem
    invoiceNR=filename.split("-")[0]
    pdf.set_font(family='times',size=20,style='B')

    pdf.cell(w=50,h=10,txt=f'Invoice no.{invoiceNR}')

    pdf.output(f'PDFs/{filename}.pdf')
