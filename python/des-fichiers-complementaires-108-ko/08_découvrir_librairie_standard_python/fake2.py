from faker import Faker
fake = Faker('fr_FR')
for _ in range(10):
    print(fake.name())
