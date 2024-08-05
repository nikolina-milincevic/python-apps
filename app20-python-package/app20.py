from invoicing import invoice

invoice.generate("app20-python-package/invoices", "app20-python-package/output", 
                 image_path="app20-python-package/pythonhow.png",
                 product_id="product_id", product_name="product_name",
                 amount_purchased="amount_purchased", price_per_unit="price_per_unit",
                 total_price="total_price")