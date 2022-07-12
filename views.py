from django.shortcuts import render , redirect   
from datos_personas.models import Personas
from datos_personas.models import Usuario
from datos_personas.forms import RegistroForm, AutenticarForm 



def informacion(request):
    return render(request,"informacion.html")

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

    if len(nombre_p)!=0 and (apellido_p)!=0 and (rut_p)!=0 and (edad_p)!=0 and (comuna_p)!=0 and (nom_vacuna_p)!=0 and (nro_dosis_p)!=0 and (telefono_p)!=0: 
        pro = Personas(nombre=nombre_p,apellido=apellido_p,rut=rut_p,edad=edad_p,comuna=comuna_p,email=email_p,nombre_v=nom_vacuna_p,nro_dosis=nro_dosis_p,tfno=telefono_p)
        pro.save() 
        return render(request,'informacion.html')
    else:
        return render(request,'informacion.html')



def listar_datos(request):
    datos = Personas.objects.all()
    data = {
        'datoss':datos
    }

    return render(request,"informacion.html",data) 


def login(request):
    if request.POST:
        form = AutenticarForm()
    return render(request,"datos_personas/templates/Menu/menu.html", {'form':form})
    


def registro(request):
    nombre_l = request.POST["nombre_l"]
    Contraseña_l = request.POST["Contraseña_l"]
    Contraseña2_l = request.POST["Contraseña2_l"]
    if len(nombre_l)!=0 and (Contraseña_l)!=0 and (Contraseña2_l)!=0:
        form = RegistroForm()
        pro = Usuario(nombre=nombre_l,Contraseña=Contraseña_l,Contraseña2=Contraseña2_l)
        pro.save()
    return render(request,"datos_personas/login.html", {'form':form})

