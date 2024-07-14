import pandas
from abc import ABC, abstractmethod
# this latter row is for abstract classes

df = pandas.read_csv("app11/hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "The Real Estate Company"
    
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
        
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)
    
    # equal operator "a == b" can be writen as "a.__eq__(b)"
    # equal operator on hotels works differently than on strings
    # even if we make different instances of hotel with the same id,
    # it will not recognise it as equal instances. 
    # That is why we want to redefine this operator on Hotel classes.
    # This is called the magic method.
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

# when inheriting methods from parent class to child class, we can rewrite
# existing methods and that works. However, the recommendation is to
# make an abstract class and then both the parent and the child would
# inherit the method from this abract class rather than from each other.
# In this case, every class that inherits an abstract class HAS TO have
# a generate method implemented
class Ticket(ABC):
    
    @abstractmethod
    def generate(self):
        pass
    

class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content
    
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name
    
    @staticmethod
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):
    def generate(self):
        return "This is your digital ticket"


hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")
hotel3 = Hotel(hotel_id="134")

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)
print(Hotel.watermark)

print(Hotel.get_hotel_count(df))
print(hotel1.get_hotel_count(df))

ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())

converted = ReservationTicket.convert(10)
print(converted)

print(hotel2 == hotel3)