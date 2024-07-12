class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        
    def get_name(self):
        my_name_upper = self.name.upper()
        return my_name_upper
    
    def age(self, current_year):
        my_age = current_year - self.birthyear
        return my_age
    
    
if __name__ == "__main__":
    user = User(name="John", birthyear=1999)
    user_age = user.age(current_year=2024)
    print(user_age)
    user_name = user.get_name()
    print(user_name)