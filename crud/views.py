from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from products.models import Books, Posters, Category, Genre
from django.contrib import messages

def manage(request):
    """
    render the manage products index page
    """
    template = 'crud/manage.html'
    return render(request, template)

class CreateBookView(CreateView):
    """
    View for Admin to create a book product
    """
    model = Books
    fields = '__all__'
    template_name = 'crud/create-book.html'
    
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "You successfully added a new Book product"
        )

        return super().form_valid(form)