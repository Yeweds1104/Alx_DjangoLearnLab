from django.shortcuts import render, get_object_or_404
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
def list_books(request):
    # retrieves all books and renders a template displaying the list of books
    books = Book.objects.all() # Fetch all book instances from the database
    context = {'books': books} #Create a context dictionary with the book list
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    # A class based view for displaying details of a specific library
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    # def get_context_data(self, **kwargs):
    #     # Add additional context data specific to the library detail view
    #     context = super().get_context_data(**kwargs) # get the default context data
    #     library = self.get_object() # retrieve the current library instance
    #     context['library'] = library # add the library instance to the context

  