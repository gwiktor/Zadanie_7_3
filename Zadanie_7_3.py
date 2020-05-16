from faker import Faker
fake_data = Faker()

class BaseContact:
    def __init__(self, name, last_name, number, e_mail):
        self.name = name
        self.last_name = last_name
        self.number = number
        self.e_mail = e_mail

    def __str__(self):
        return f"{self.name} {self.last_name} {self.e_mail}"

    def contact(self):
        return f"Wybieram numer +48 {self.number} i dzwonię do {self.name} {self.last_name}"
    
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

for m in range(5):
    i = fake_data.name()
    j = fake_data.safe_email()
    k = i.split()
    m = fake_data.phone_number
    n = fake_data.job
    p = fake_data.company
    r = fake_data.phone_number

    base_cards.append(BaseContact(k[0], k[1], m, j))
    business_cards.append(BusinessContact(k[0], k[1], m, j, n, p, r))

'''
by_name = sorted(base_cards, key=lambda BaseContact: BaseContact.name)
by_last_name = sorted(base_cards, key=lambda BaseContact: BaseContact.last_name)
by_e_mail = sorted(base_cards, key=lambda BaseContact: BaseContact.e_mail)

print("Cards sorted by name:")
for i in by_name:
    print(i)

print("Cards sorted by last name:")
for i in by_last_name:
    print(i)

print("Cards sorted by e-mail:")
for i in by_e_mail:
    print(i)

print(base_cards[1].contact())
print(base_cards[1].label_length)
'''