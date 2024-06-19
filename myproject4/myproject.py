import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

my_files = glob.glob("./myproject4/files/*.txt")
pdf = FPDF(orientation="P", format="A4", unit="mm")

for filename in my_files:
    my_filename = Path(filename).stem.title()
    with open(filename, "r") as file:
        content = file.read()
        
    pdf.set_font(family="Times", style="B", size=16)
    pdf.add_page()
    pdf.cell(w=50, h=8, txt=my_filename, ln=1)
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=8, txt=content)
    
pdf.output("./myproject4/output.pdf")