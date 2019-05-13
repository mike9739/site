from django.shortcuts import render,HttpResponse
html_base = """
<h1>WEB</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about">Acerca de</a></li>
    <li><a href="/portafolio">Portafolio</a></li>
    <li><a href="/contact">Contacto</a></li>
    
</ul>
"""
# Create your views here.
def home(request):
    return HttpResponse( html_base + "<h2>home</h2>")

def about(request):
    return HttpResponse(html_base + "<h2>about</h2><p>Pasteleria</p>")

def portafolio(request):
    return HttpResponse(html_base + "<h2>portafolio</h2><p>trabajos</p>")

def contacto(request):
    return HttpResponse(html_base + "<h2>contacto</h2>")