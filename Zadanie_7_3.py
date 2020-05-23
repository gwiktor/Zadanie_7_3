import logging
import sys
from faker import Faker
fake_data = Faker()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

class BaseContact:
    def __init__(self, name, last_name, phone_number, e_mail):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.e_mail = e_mail

    def __str__(self):
        return f"{self.name} {self.last_name} {self.phone_number} {self.e_mail}"

    def contact(self):
        return f"Wybieram numer +48 {self.phone_number} i dzwonię do {self.name} {self.last_name}"

    @property
    def label_length(self):
        imie = len(self.name)
        nazwisko = len(self.last_name)
        return f"{imie} {nazwisko}"

class BusinessContact(BaseContact):
    def __init__(self, job, company, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_number = business_number
    
    def contact(self):
        return f"Wybieram numer +48 {self.business_number} i dzwonię do {self.name} {self.last_name}"

base_cards = []
business_cards = []

def create_contacts(choice, quantity):
    for a in range(quantity):
        i = fake_data.name()
        j = fake_data.safe_email()
        k = i.split()
        m = fake_data.msisdn()
        if choice == "BaseContact":
            base_cards.append(BaseContact(name = k[0], last_name = k[1], phone_number = m, e_mail = j))
            for i in base_cards:
                return(f"Lista kontaktów: {i}")
        elif choice == "BusinessContact":
            n = fake_data.job()
            p = fake_data.company()
            r = fake_data.phone_number()
            business_cards.append(BusinessContact(name = k[0], last_name = k[1], phone_number = m, e_mail = j, job = n, company = p, business_number = r))
            return(f"Lista kontaktów: {business_cards}")

#Sprawdzenie
if __name__ == "__main__":
    print("*** WITAJ W KSIĄŻCE ADRESOWEJ ***")
    choice = input("Napisz jaką książkę adresową chcesz stworzyć, posługjąc się odpowiednim określeniem: \n1 - BaseContact \n2 - BusinessContact")
    quantity = int(input("Podaj liczbę kontaktów, które chcesz utworzyć: "))
    logging.debug(f"Została wybrana książka adresowa {choice} z {quantity} kontaktami")
    logging.debug(create_contacts(choice, quantity))
'''
create_contacts("BaseContact", 10)
for i in base_cards:
    print(i)

create_contacts("BusinessContact", 3)
for i in business_cards:
    print(i)

print(base_cards[5].contact())
print(base_cards[5].label_length)

print(business_cards[1].contact())
print(business_cards[1].label_length)
'''