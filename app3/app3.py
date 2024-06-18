from fpdf import FPDF
import pandas as pd

# orientation P stands for portrait, L for landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("./app3/topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    
    for i in range(20, 280, 10):
        pdf.line(10, i, 200, i)
    pdf.ln(246)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=8, txt=row["Topic"], align="R")
    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for i in range(31, 270, 10):
            pdf.line(10, i, 200, i)
        pdf.ln(250)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=8, txt=row["Topic"], align="R")

pdf.output("./app3/output.pdf")