from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('panel:panel')
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form})

def index_view(request):
    #inst = ConfiguracionIndex.objects.get(pk=1)
    #noti = noticias_index.objects.all()
    #orga = organizaciones.objects.all()
    #productos = presentacion.objects.all()[:5]
    return render(request, 'paneladministracion/index.html',
                  {})