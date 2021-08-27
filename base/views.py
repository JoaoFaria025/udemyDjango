from django.shortcuts import render
from django.contrib import messages
from .models import Cliente
from .forms import ContatoForm

def index(request):
    cliente = Cliente.objects.all()
    form = ContatoForm()

    messages.success(request,'Email enviado com sucesso')
    context = {
        'nome' : 'POO',
        'cliente':cliente,
        'form': form,
    }
    return render(request,'index.html',context)