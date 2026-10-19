from django.shortcuts import render
from django.http import HttpResponse

def hello_django(request):
    return HttpResponse("Hello, Django!")

def profile_view(request):
    return render(request, 'profile.html')

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')


from django.shortcuts import render
from .models import Book
from .forms import UserForm

# Part A: Display Books using Django ORM
def book_list(request):
    books = Book.objects.all()  # Django ORM se all books fetch karna
    return render(request, 'book_list.html', {'books': books})

# Part B: Form Submit & Result Views
def submit_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'result.html', {'name': name, 'email': email})
    else:
        form = UserForm()
    return render(request, 'form.html', {'form': form})
# Create your views here.
