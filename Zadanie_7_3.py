import logging
import sys
from faker import Faker
fake_data = Faker()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

#Zdefiniowanie klasy BaseContact
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
        return f"LIczba liter w imieniu: {imie}, liczba liter w nazwisku: {nazwisko}"

#Zdefiniowanie sub-klasy BusinessContact
class BusinessContact(BaseContact):
    def __init__(self, job, company, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_number = business_number
    
    def __str__(self):
        return f"{self.name} {self.last_name} {self.phone_number} {self.e_mail} {self.job} {self.company} {self.business_number}"

    def contact(self):
        return f"Wybieram numer +48 {self.business_number} i dzwonię do {self.name} {self.last_name}"

#Zdefiniowanie list do tworzenia list wizytówek
base_cards = []
business_cards = []

#Tworzenie listy kontaktów do list wizytówek
def create_contacts(choice, quantity):
    
    for a in range(quantity):
        i = fake_data.name()
        j = fake_data.safe_email()
        k = i.split()
        m = fake_data.msisdn()
        if choice == BaseContact:
            base_cards.append(BaseContact(name = k[0], last_name = k[1], phone_number = m, e_mail = j))
        elif choice == BusinessContact:
            n = fake_data.job()
            p = fake_data.company()
            r = fake_data.phone_number()
            business_cards.append(BusinessContact(name = k[0], last_name = k[1], phone_number = m, e_mail = j, job = n, company = p, business_number = r))

#Funkcja pomagająca okreslić co można wykonać
def print_help():
    print("""Poniżej lista czynności, które możesz wykonać wpisując odpowiednią komendę:
    stwórz base cards - tworzenie wizytówek z podstawowymi danymi
    stwórz business cards - tworzenie wizytówek biznesowych
    pokaż - wylistowanie wszystkich wizytówek danej grupy wizytówek
    zadzwoń - wybranie telefonu do wybranej osoby
    długość - sprawdzenie długości imienia i nazwiska danej osoby
    zamknij - zamknięcie programu""")

#Funkcja przedstawiająca listę wizytówek
def show(a):
    if a == "base cards":
        for i in base_cards:
            print(i)
        
    elif a == "business cards":
        for i in business_cards:
            print(i)

#Funkcja wywołująca funkcję klasy "contact" z określonej listy izytówek        
def call():
    a = input("Z której listy wizytówek chcesz zadzownić? \n base cards \n business cards \n")
    show(a)
    b = input("Wpisz imię osoby, do której chcesz zadzownić ")
    if a == "base cards":
        for i in base_cards:
            if b == str(i.name):
                print(i.contact())
        
    elif a == "business cards":
        for i in business_cards:
            if b == str(i.name):
                print(i.contact())

#Funkcja wywołująca funkcję klasy "label_length" z określonej listy wizytówek
def length():
    a = input("Z której listy wizytówek chcesz sprawdzić długość imienia i nazwiska? \n base cards \n business cards \n")
    show(a)
    b = input("Wpisz imię osoby, której chcesz sprawdzić długość imienia i nazwiska ")
    if a == "base cards":
        for i in base_cards:
            if b == str(i.name):
                print(i.label_length)
        
    elif a == "business cards":
        for i in business_cards:
            if b == str(i.name):
                print(i.label_length)


#Dostępne komendy do wywołania
def task():
    task1 = input("Co chcesz wykonać?")
    if task1 == "pomoc":
        print_help()
    elif task1 == "stwórz base cards":
        a = int(input("Ile randomowych wizytówek chcesz stworzyć? "))
        create_contacts(BaseContact, a)
    elif task1 == "stwórz business cards":
        a = int(input("Ile randomowych wizytówek chcesz stworzyć? "))
        create_contacts(BusinessContact, a)
    elif task1 == "pokaż":
        a = input("Które wizytówki chciałbyś zobaczyć? \n base cards \n business cards \n")
        show(a)
    elif task1 == "zadzwoń":
        call()
    elif task1 == "długość":
        length()  
    elif task1 == "zamknij":
        print("Narazie")
    else:
        print("Nie ma takiego polecenia. Sprawdz za pomocą komendy 'pomoc' co możesz zrobić")
        
#Uruchomienie programu
if __name__ == "__main__":
    print("Witam w moim programie! Chcesz się dowiedzieć co potrafię? Wpisz 'pomoc', aby dowiedzieć się więcej")
    while True:
        task()

