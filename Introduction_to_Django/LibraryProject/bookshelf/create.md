To get InteractiveConsole (Interactive python shell) run below command

> > > py manage.py shell
> > > Import Book model in interactive shell from bookshelf app
> > > from bookshelf.models import Book

Create a new book object and save it to the database

> > > book = Book(title="1984", author="George Orwell", publication_year="1949")
> > > book.save()
