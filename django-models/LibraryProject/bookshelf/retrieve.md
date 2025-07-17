To retrieve the book attributes run below command in interactive shell

> > > book = Book.objects.get(id=1)
> > > book = Book.objects.get(title="1984")
> > > book = Book.objects.get(author="George Orwell")
> > > book = Book.objects.get(publication_year="1949")
> > > To display id

> > > book.id

To display the title

> > > book.title

To display the author

> > > book.author

To display the publication year

> > > book.publication_year
