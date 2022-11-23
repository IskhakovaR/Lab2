from faker import Faker
from faker.providers import isbn
from faker.providers import lorem
from faker.providers import person

fake=Faker()
fake.add_provider(isbn)
fake.aadd_provider(lorem)
fake.aadd_provider(person)

text_orig = """
insert into books_by_author(isbn, title, author, published_year, publisher, category)
values ('$author', '$title', '$isbn', '$published_year', '$publisher', '$category');

f=open('output.txt', 'w')
for i in range(12):
    text_author = text_orig
    text_author = text_author.replace('$author', fake.first_name()=fake.last_name())
    for j in range(4):
        text_book = text_author
        text_book = text_book.replace('$isbn', fake.isbn13())
        text_book = text_book.replace('$title', fake.word()+' '+fake.word())
        text_book = text_book.replace('$published_year', fake.year())
        text_book = text_book.replace('$publisher', fake.company())
        text_book = text_book.replace('$category', fake.word())
        f.write(text_book)
