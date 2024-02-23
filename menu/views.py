from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Call
from .forms import CallForm
from django.contrib.auth import authenticate, login
# Create your views here.



def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.product_set.all()
    return render(request, 'category_detail.html', {'category': category, 'products': products})




def call_garson(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CallForm()
    return render(request, 'garson_call_form.html', {'form': form})

def garson_list(request):
    if not request.user.is_authenticated:
        return redirect("home")
    calls = Call.objects.all()
    return render(request, 'garson.html', {'calls': calls})

def delete_call(request, call_id):
    # İlgili çağrıyı al
    call = get_object_or_404(Call, pk=call_id)
    
    # İsteği POST ile yapılmışsa (yani bir form gönderilmişse)
    if request.method == 'POST':
        # Çağrıyı sil
        call.delete()
        # Garson çağrı listesi sayfasına yönlendir
        return redirect('garson_list')
    
    # Eğer POST ile yapılmamışsa, bir hata oluşmuş demektir
    return HttpResponseNotAllowed(['POST'])
