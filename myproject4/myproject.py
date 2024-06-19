import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

my_files = glob.glob("./myproject4/files/*.txt")
pdf = FPDF(orientation="P", format="A4", unit="mm")

for filename in my_files:
    filename = Path(filename).stem.title()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.add_page()
    pdf.cell(w=50, h=8, txt=filename, ln=1)
    
pdf.output("./myproject4/output.pdf")