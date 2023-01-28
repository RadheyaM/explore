from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from products.models import Books, Posters, Category, Genre
from django.contrib import messages


def manage(request):
    """
    render the manage products index page
    """
    books = Books.objects.all()
    posters = Posters.objects.all()
    genres = Genre.objects.all()
    categories = Category.objects.all()

    context = {
        'books': books,
        'posters': posters,
        'genres': genres,
        'categories': categories,
    }

    template = 'crud/manage.html'
    return render(request, template, context)

# ====================================================================================
#                                   CREATE VIEWS
# ====================================================================================


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
            self.request,
            messages.SUCCESS, 
            "You successfully added a new Book product"
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
            self.request, 
            messages.SUCCESS, 
            "You successfully added a new Poster product"
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
            self.request,
            messages.SUCCESS,
            "You successfully added a new Category"
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
            self.request, 
            messages.SUCCESS, 
            "You successfully added a new Genre"
        )

        return super().form_valid(form)

# ====================================================================================
#                                   UPDATE VIEWS
# ====================================================================================


class UpdateBookView(UpdateView):
    """
    View for Admin to update a book product
    """
    model = Books
    fields = '__all__'
    template_name = 'crud/update/update-book.html'
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "You successfully updated the Book product"
        )

        return super().form_valid(form)


class UpdatePosterView(UpdateView):
    """
    View for Admin to update a book product
    """
    model = Posters
    fields = '__all__'
    template_name = 'crud/update/update-poster.html'
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "You successfully updated the Poster product"
        )

        return super().form_valid(form)


class UpdateCategoryView(UpdateView):
    """
    View for Admin to update a book product
    """
    model = Category
    fields = '__all__'
    template_name = 'crud/update/update-category.html'
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "You successfully updated the Category"
        )

        return super().form_valid(form)


class UpdateGenreView(UpdateView):
    """
    View for Admin to update a book product
    """
    model = Genre
    fields = '__all__'
    template_name = 'crud/update/update-genre.html'
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "You successfully updated the Genre"
        )

        return super().form_valid(form)

# ====================================================================================
#                                   DELETE VIEWS
# ====================================================================================


class DeleteBookView(DeleteView):
    """
    View for Admin to create a book product
    """
    model = Books
    fields = '__all__'
    template_name = 'crud/delete/delete-book.html'
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "You successfully deleted the Book product"
        )

        return super().form_valid(form)


class DeletePosterView(DeleteView):
    """
    View for Admin to create a book product
    """
    model = Posters
    fields = '__all__'
    template_name = 'crud/delete/delete-poster.html'
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "You successfully deleted the Poster product"
        )

        return super().form_valid(form)


class DeleteCategoryView(DeleteView):
    """
    View for Admin to delete a book product
    """
    model = Category
    fields = '__all__'
    template_name = 'crud/delete/delete-category.html'
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request, messages.SUCCESS,
            "You successfully deleted the Category"
        )

        return super().form_valid(form)


class DeleteGenreView(DeleteView):
    """
    View for Admin to delete a book product
    """
    model = Genre
    fields = '__all__'
    template_name = 'crud/delete/delete-genre.html'
    success_url = reverse_lazy('manage_products')

    def form_valid(self, form):
        """
        Custom form_valid function adding a success message for display.
        """
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "You successfully deleted the Genre"
        )

        return super().form_valid(form)
