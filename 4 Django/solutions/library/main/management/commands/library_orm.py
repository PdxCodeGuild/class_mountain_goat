
from django.core.management.base import BaseCommand

from main.models import Book, Author

class Command(BaseCommand):
    def handle(self, *args, **options):
        book = Book.objects.get(title='Good Omens')
        print(book.title)
        print(book.year_published)

        print(book.authors.all())
        for author in book.authors.all():
            print(author.name)

        author = Author.objects.get(name='Terry Pratchett')
        print(author.books.all())
        for book in author.books.all():
            print(book.title)
        



        # book = Book(title='Tiny Pretty Things', year_published=2019)
        # book.save()
        
        # author1 = Author(name='Sona Charaipotra')
        # author1.save()

        # author2 = Author(name='Dhonielle Clayton')
        # author2.save()

        # book.authors.add(author1)
        # book.authors.add(author2)

        # book.authors.set([author1, author2])

        # book.authors.clear()


        books_data = [{
            'title': 'Hogfather',
            'year_published': 1996,
            'authors': ['Terry Pratchett']
        },{
            'title': 'Wyrd Sisters',
            'year_published': 1988,
            'authors': ['Terry Pratchett']
        }]

        for book_data in books_data:
            title = book_data['title']
            year_published = book_data['year_published']

            book = Book(title=title, year_published=year_published)
            book.save()

            for author_name in book_data['authors']:
                
                # author = author.objects.get(name=author_name)
                
                # author = Author(name=author_name)
                # author.save()

                author, created = Author.objects.get_or_create(name=author_name)
            
                book.authors.add(author)
            












