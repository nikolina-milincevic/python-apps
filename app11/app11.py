import pandas

df = pandas.read_csv("app11/hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("app11/cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("app11/card_security.csv", dtype=str)


class Hotel:
    def __init__(self, my_hotel_id):
        self.my_hotel_id = my_hotel_id
        self.name = df.loc[df["id"] == self.my_hotel_id, "name"].squeeze()
    
    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.my_hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
    
    def book(self):
        """Books a hotel by changing its availability to yes"""
        df.loc[df["id"] == self.my_hotel_id, "available"] = "no"
        df.to_csv("app11/hotels.csv", index=False)
    
    def view_hotels(self):
        pass


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class ReservationTicket:
    def __init__(self, my_customer_name, my_hotel_object):
        self.my_customer_name = my_customer_name
        self.my_hotel_object = my_hotel_object
    
    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name of the customer: {self.my_customer_name}
        Hotel: {self.my_hotel_object.name}
        """
        return content


class SpaReservationTicket:
    def __init__(self, my_customer_name, my_hotel_object):
        self.my_customer_name = my_customer_name
        self.my_hotel_object = my_hotel_object
    
    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here are your SPA booking data:
        Name of the customer: {self.my_customer_name}
        Hotel: {self.my_hotel_object.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number
        
    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, 
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False
        

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False
    


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = SpaHotel(hotel_id)
if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate("mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
            spa = input("Do you want to book a spa package? ")
            if spa == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaReservationTicket(name, hotel)
                print(spa_ticket.generate())
        else:
            print("Credit card authentication failed")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not available")