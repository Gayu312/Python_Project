from abc import ABC, abstractmethod

class TravelAnywhere(ABC):
    @abstractmethod
    def get_user_input(self):
        pass
    @abstractmethod
    def calculate_price_with_gst(self):
        pass
    @abstractmethod
    def confirm_ticket(self):
        pass
    @abstractmethod
    def yourTicket(self):
        pass
    @abstractmethod
    def ticketId(self):
        pass
import random
class SeatsNow(TravelAnywhere):
   
    def __init__(self):
            self.name=""
            self.destination_from = ""
            self.destination_to = ""
            self.date_of_journey = ""
            self.seater_or_sleeper = ""
            self.ac_or_non_ac = ""
            self.gender = ""
            self.age = 0
            self.price = 0.0
            self.gst = 0.08
            self.ticketId = random.randint(10100, 20100)
            self.seat_number = random.randint(1, 20)
        

    def get_user_input(self):
        print("\nWelcome to TravelAnywhere!")
        self.name = input("Enter your name: ")
        self.destination_from = input("Enter your destination from: ")
        self.destination_to = input("Enter your destination to: ")
        print("Select date of journey:")
        print("1. Today")
        print("2. Tomorrow")
        print("3. Other (please enter date)")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.date_of_journey = "Today"
        elif choice == 2:
            self.date_of_journey = "Tomorrow"
        else:
            self.date_of_journey = input("Enter your date of journey: ")
        
        print("Select Seater or Sleeper:")
        print("1. Seater")
        print("2. Sleeper")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.seater_or_sleeper = "Seater"
        else:
            self.seater_or_sleeper = "Sleeper"
        
        print("Select AC or Non-AC:")
        print("1. AC")
        print("2. Non-AC")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.ac_or_non_ac = "AC"
        else:
            self.ac_or_non_ac = "Non-AC"
        
        print("Enter your gender (Male/Female): ")
        self.gender = input()

        
        print("Enter your age: ")
        self.age = int(input())
        print("Enter your price: ")
        self.price = float(input())

    def calculate_price_with_gst(self):
        self.price_with_gst = self.price * (1 + self.gst)
    
    
    def ticketId(self):
        return self.ticketId   
    
    def seat_number(self):
        return self.seat_number

    
    def confirm_ticket(self):
        print("\nConfirming your ticket...")
       
       
    
    def yourTicket(self):
        print("\nHere your Ticket Information")
        print("Name: ", self.name.title())
        print("Your Ticket Id:", self.ticketId)
        print("Your seat number is ", self.seat_number)
        print("Destination from:", self.destination_from.title())
        print("Destination to:", self.destination_to.title())
        print("Date of journey:", self.date_of_journey)
        print("Seater or Sleeper:", self.seater_or_sleeper)
        print("AC or Non-AC:", self.ac_or_non_ac)
        print("Gender:", self.gender.title())
        print("Age:", self.age)
        print("Price with GST:", self.price_with_gst)
        print("Thank You, for travelling with us!")
       

def main():
    travel_anywhere = SeatsNow()
    travel_anywhere.get_user_input()
    travel_anywhere.calculate_price_with_gst()
    travel_anywhere.confirm_ticket()
    travel_anywhere.yourTicket()

if __name__ == "__main__":
    main()     