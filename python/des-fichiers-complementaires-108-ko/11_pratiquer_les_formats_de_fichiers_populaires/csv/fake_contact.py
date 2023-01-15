from faker import Faker
fake = Faker('fr_FR')

def fake_contact(nb=1):
    for _ in range(nb):
        n = fake.name()
        d = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=75)
        a = fake.address()
        a = a.replace('\n', ' ')
        t = fake.phone_number()
        c = fake.sentences(nb=1, ext_word_list=None)
    return n,d,a,t," ".join(c)

def fake_contact_asdict():
    n,d,a,t,c = fake_contact()
    return {
            'nom' : n,
            'date_naissance' : d,
            'adresse' : a,
            'telephone' : t,
            'commentaire' : c
            }

if __name__ == "__main__":
    print(fake_contact())
    print(fake_contact_asdict())



