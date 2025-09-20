from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

def homeSec(request):
    '''
    Renderiza a página inicial de segurança.
    '''
    return render(request, 'seguranca/homeSec.html')

def registro(request):
    '''
    Renderiza a página de registro de usuários.
    '''
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request,
        'seguranca/registro.html', context)