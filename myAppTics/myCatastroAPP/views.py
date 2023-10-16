from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render

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
                return JsonResponse({'content': {'message': 'Exito al Iniciar Sesion', 'color': 'succes',
                                                 'nota': 'Bienvenido!!!',
                                                 }})
        else:
            return JsonResponse({'content': {'message': 'Error al Iniciar Sesion', 'color': 'danger',
                                             'nota': 'usuario o contraseña incorrectas!!!',
                                             }})
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form})