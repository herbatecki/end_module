from faker import Faker

from sqlalchemy import Boolean
from blog.models import Entry, db
import datetime

fake = Faker(['pl'])

class CardB:
    def __init__(self, name, surname, company, occupation, email):
        self.name= fake.name()
        self.surname = None
        self.company = None
        self.occupation = None
        self.email = fake.email()

def fake_person():
    # fake_list = []
    for _ in range(5):
        fake_data = CardB(name=fake.name(), surname = None, company=None, occupation= None, email=fake.email())
        # fake_list.append(fake_data)
        print('{:{align}{width}}'.format(fake_data.name,align='>', width='24'),'{:{align}{width}}'.format(fake_data.email,align='>', width='30'))
        # return fake_person() # dam ten return bez nawiasów - wtedy mam jeden wynik zwrotny. Dam z nawiasem to leci z danymi, aż do wywalenia. Ad: jeśli dajemy return to nie powinno być w funkcji "print" i na odwrót. 
        # return fake_list
fake_person() # taki zapis dobry bez returna, z wbudowanym "print" w funkcji


def fake_posts():
    # fake_list = []
    for _ in range(10):
        fake_post = Entry(title=fake.sentence(), body='\n'.join(fake.paragraphs()), is_published = True)
        # fake_list.append(fake_post)
        # return fake_list
        return fake_post.title

revelation = fake_posts()
print(revelation)

def generate_entries(how_many=10):
    
    for i in range(how_many):
       post = Entry(
           title=fake.sentence(),
           body='\n'.join(fake.paragraphs(15)),
           is_published=True
       )
    return post.title

revelation = generate_entries()
print(revelation)