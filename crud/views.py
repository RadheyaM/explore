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

#====================================================================================
#                                   CREATE VIEWS
#====================================================================================

class CreateBookView(CreateView):
    """
    View for Admin to create a book product
    """
    model = Books
    fields = '__all__'
    template_name = 'crud/create/create-book.html'
    
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "You successfully added a new Book product"
        )

        return super().form_valid(form)

class CreatePosterView(CreateView):
    """
    View for Admin to create a book product
    """
    model = Posters
    fields = '__all__'
    template_name = 'crud/create/create-poster.html'
    
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "You successfully added a new Poster product"
        )

        return super().form_valid(form)

class CreateCategoryView(CreateView):
    """
    View for Admin to create a book product
    """
    model = Category
    fields = '__all__'
    template_name = 'crud/create/create-category.html'
    
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "You successfully added a new Category"
        )

        return super().form_valid(form)

class CreateGenreView(CreateView):
    """
    View for Admin to create a book product
    """
    model = Genre
    fields = '__all__'
    template_name = 'crud/create/create-genre.html'
    
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS, "You successfully added a new Genre"
        )

        return super().form_valid(form)