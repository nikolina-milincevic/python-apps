from fpdf import FPDF

# orientation P stands for portrait, L for landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello there!", align="L", ln=1, border=1)
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="Hi there!", align="L", ln=1, border=1)
# border=1 means that the border of the cell is set to true
# and will be displayed
# w=0 set the cell all over the screen in width
# if we set w=10, then the border would be showing a small
# rectangle of width 10
# ln=1 means that the next cell will be displayed in next line
# so if w=10 and ln=0, the next cell would be right next to
# the existing one, text could even overlap
# the height is recommended to be the same as font size,
# that is actually the height of the sell, see the border

pdf.output("./app3/output.pdf")