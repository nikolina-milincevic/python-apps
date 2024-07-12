import pandas
from fpdf import FPDF

df = pandas.read_csv("app11/articles.csv", dtype={"id": str})


class Object:
    def __init__(self, object_id):
        self.object_id = object_id
        self.name = df.loc[df["id"] == self.object_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.object_id, "price"].squeeze()
    
    def available(self):
        in_stock = df.loc[df["id"] == self.object_id, "in stock"].squeeze()
        return in_stock
    
    def buy(self):
        in_stock = df.loc[df["id"] == self.object_id, "in stock"].squeeze()
        in_stock = in_stock - 1
        df.loc[df["id"] == self.object_id, "in stock"] = in_stock
        df.to_csv("app11/articles.csv", index=False)
    

class Receipt:
    def __init__(self, object_bought):
        self.object_bought = object_bought
    
    def make_pdf(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt for object with id {self.object_bought.object_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.object_bought.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.object_bought.price}", ln=1)

        pdf.output("app11/receipt.pdf")

    

print(df)
my_object_id = input("Enter id of the object: ")
my_object = Object(my_object_id)

if my_object.available():
    my_object.buy()

    my_receipt = Receipt(my_object)
    my_receipt.make_pdf()
else:
    print("Not available")