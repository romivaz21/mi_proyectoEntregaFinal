from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from .models import Curso
from .forms import CursoForm
#from django.shortcuts import render, redirect, get_object_or_404




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'usuarios/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})



from django.shortcuts import render

def home_view(request):
    return render(request, 'usuarios/home.html')





@login_required
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/curso_list.html', {'cursos': cursos})

@login_required
def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'cursos/curso_form.html', {'form': form})

@login_required
def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/curso_form.html', {'form': form})

@login_required
def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')
    return render(request, 'cursos/curso_confirm_delete.html', {'curso': curso})



from django.shortcuts import render

def about_me_view(request):
    return render(request, 'usuarios/about_me.html')