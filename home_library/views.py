from django.shortcuts import render,redirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView, FormView
from home_library.models import Book, Author, Publisher, Friend
from django.urls import reverse_lazy
from allauth.socialaccount.models import SocialAccount


class authView():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_login'] = True
        if self.request.user.is_authenticated:  
            context['username'] = self.request.user.username
            if SocialAccount.objects.filter(user=self.request.user).exists():
                context['extra_data'] = SocialAccount.objects.get(user=self.request.user).extra_data
        return context 

class BookList(authView, ListView):
    model = Book
    context_object_name = "books"
    template_name = "book_list.html"

class BookDetail(authView, DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreate(authView, CreateView):
    model = Book
    fields = '__all__'
    template_name = 'book_add.html'
    def get_form(self, form_class=None):
        form = super(BookCreate, self).get_form(form_class)
        form.fields['copy_count'].required = False
        form.fields['price'].required = False
        form.fields['ISBN'].required = False
        form.fields['friends'].required = False
        return form

class BookEdit(authView, UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_edit.html'
    def get_form(self, form_class=None):
        form = super(BookEdit, self).get_form(form_class)
        form.fields['copy_count'].required = False
        form.fields['price'].required = False
        form.fields['ISBN'].required = False
        form.fields['friends'].required = False
        return form
    @staticmethod
    def return_book(request):
        if request.method == 'POST':
            book_id = request.POST['id']
            if not book_id:
                return redirect(reverse_lazy('home_library:index'))
            else:
                book = Book.objects.filter(id=book_id).first()
                if not book:
                    return redirect(reverse_lazy('home_library:index'))
                book.friends = None
                book.save()
        return redirect(reverse_lazy('home_library:index'))

class BookDelete(authView, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home_library:index')

class AuthorList(authView, ListView):
    model = Author
    context_object_name = "authors"
    template_name = "author_list.html"

class AuthorCreate(authView, CreateView):
    model = Author
    fields = '__all__'
    template_name = 'author_add.html'

class AuthorEdit(authView, UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'author_edit.html'

class AuthorDelete(authView, DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('home_library:authors')

class PublisherList(authView, ListView):
    model = Publisher
    context_object_name = "publishers"
    template_name = "publisher_list.html"

class PublisherCreate(authView, CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'publisher_add.html'

class PublisherEdit(authView, UpdateView):
    model = Publisher
    fields = '__all__'
    template_name = 'publisher_edit.html'

class PublisherDelete(authView, DeleteView):
    model = Publisher
    template_name = 'publisher_delete.html'
    success_url = reverse_lazy('home_library:publishers')

class FriendList(authView, ListView):
    model = Friend
    context_object_name = "friends"
    template_name = "friend_list.html"

class FriendCreate(authView, CreateView):
    model = Friend
    fields = '__all__'
    template_name = 'friend_add.html'

class FriendEdit(authView, UpdateView):
    model = Friend
    fields = '__all__'
    template_name = 'friend_edit.html'

class FriendDelete(authView, DeleteView):
    model = Friend
    template_name = 'friend_delete.html'
    success_url = reverse_lazy('home_library:friends')
