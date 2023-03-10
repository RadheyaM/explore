from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from products.models import Books, Posters, Category, Genre
from django.contrib import messages


class SuperuserRequiredMixin(UserPassesTestMixin):
    """Limit certain class views to superuser only"""
    def test_func(self):
        return self.request.user.is_superuser

@login_required
@permission_required('products.can_change_books')
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


class CreateBookView(SuperuserRequiredMixin, CreateView):
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


class CreatePosterView(SuperuserRequiredMixin, CreateView):
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


class CreateCategoryView(SuperuserRequiredMixin, CreateView):
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


class CreateGenreView(SuperuserRequiredMixin, CreateView):
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


class UpdateBookView(SuperuserRequiredMixin, UpdateView):
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


class UpdatePosterView(SuperuserRequiredMixin, UpdateView):
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


class UpdateCategoryView(SuperuserRequiredMixin, UpdateView):
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


class UpdateGenreView(SuperuserRequiredMixin, UpdateView):
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


class DeleteBookView(SuperuserRequiredMixin, DeleteView):
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


class DeletePosterView(SuperuserRequiredMixin, DeleteView):
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


class DeleteCategoryView(SuperuserRequiredMixin, DeleteView):
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


class DeleteGenreView(SuperuserRequiredMixin, DeleteView):
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
