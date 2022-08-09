from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm


def inicio(request):
    return render(request,'aplicacion1/index.html')

class Registro(View):
    def get(self,request):
        form = NewUserForm(request.POST)
        return render(request,'aplicacion1/registro.html',{'register_form':form})
    
    def post(self,request):
        form  = NewUserForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
            messages.success(request,'Usuario creado exitosamente')
            return redirect('inicio')
        else:
            messages.error(request,'Error al crear usuario')
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request, 'aplicacion1/registro.html',{'register_form':form})
        