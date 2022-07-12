
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render , redirect 
from datos_personas.models import Personas
from datos_personas.models import Usuario
from datos_personas.forms import RegistroForm, AutenticarForm 





def informacion(request):
    datos = Personas.objects.all()
    data = {
      'datoss':datos  
    }
    return render(request,"informacion.html",data) 


def menu(request):
    return render(request,"menu.html")  


def ingresar_datos(request): 
    nombre_p = request.POST["nombre_p"]
    apellido_p = request.POST["apellido_p"]
    rut_p = request.POST["rut_p"]
    edad_p = request.POST["edad_p"]
    comuna_p = request.POST["comuna_p"]
    email_p = request.POST["email_p"]
    nom_vacuna_p = request.POST["nom_vacuna_p"]
    nro_dosis_p = request.POST["nro_dosis_p"]
    telefono_p = request.POST["telefono_p"]

    if request.method == "POST":
        if len(nombre_p)!=0 and (apellido_p)!=0 and (rut_p)!=0 and (edad_p)!=0 and (comuna_p)!=0 and (nom_vacuna_p)!=0 and (nro_dosis_p)!=0 and (telefono_p)!=0: 
            pro = Personas(nombre=nombre_p,apellido=apellido_p,rut=rut_p,edad=edad_p,comuna=comuna_p,email=email_p,nombre_v=nom_vacuna_p,nro_dosis=nro_dosis_p,tfno=telefono_p)
            pro.save()
            if request.POST:
                return render(request,"menu.html")
        return HttpResponse("<p>datos no validos<p>")

def eliminar(request,id):
    persona = Personas.objects.get(id=id)
    persona.delete()
    persona = Personas.objects.all()
    data = {
      'datoss':persona  
    }
    return render(request,"informacion.html",data) 





def login(request):
        if request.method == "POST":
            form = AutenticarForm()
            return render(request,"menu.html", {'form':form})


def registro(request):
    form = RegistroForm()
    return render(request,"registration/login.html",{'form':form})