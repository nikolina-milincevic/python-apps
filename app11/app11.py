import pandas

df = pandas.read_csv("app11/hotels.csv", dtype={"id": str})


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


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available")