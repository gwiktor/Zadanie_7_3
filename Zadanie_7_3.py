import sys
from faker import Faker
fake_data = Faker()

class BaseContact:
    def __init__(self, name, last_name, phone_number, e_mail):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.e_mail = e_mail

    def __str__(self):
        return f"{self.name} {self.last_name} {self.phone_number} {self.e_mail}"

    def contact(self):
        for self in base_cards:
            return f"Wybieram numer +48 {self.phone_number} i dzwonię do {self.name} {self.last_name}"
        for self in business_cards:
            return f"Wybieram numer +48 {self.business_number} i dzwonię do {self.name} {self.last_name}"
    
    @property
    def label_length(self):
        imie = len(self.name)
        nazwisko = len(self.last_name)
        return f"{imie} {nazwisko}"

class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone

    base_cards = []
    business_cards = []

    def create_contacts(quantity, choice):
        base_cards = []
        business_cards = []
        for a in range(quantity):
            i = fake_data.name()
            j = fake_data.safe_email()
            k = i.split()
            m = fake_data.msisdn()
            n = fake_data.job()
            p = fake_data.company()
            r = fake_data.msisdn()
            if choice == 1:
                base_cards.append(BaseContact(k[0], k[1], m, j))
                print(base_cards)
            elif choice == 2:
                business_cards.append(BusinessContact(k[0], k[1], m, j, n, p, r))
                print(business_cards)
quantity = int(input("Ile chcesz wizytówek?"))
choice = int(input("Jakie chcesz wizytówki?"))


'''
base_cards.append(BaseContact(k[0], k[1], m, j))
business_cards.append(BusinessContact(k[0], k[1], m, j, n, p, r))
'''

