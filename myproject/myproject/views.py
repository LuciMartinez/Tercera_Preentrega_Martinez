from django.shortcuts import render, redirect
from .forms import LibroForm

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros_lista')
    else:
        form = LibroForm()
    return render(request, 'libros/agregar_libro.html', {'form': form})

def buscar_libro(request):
    if request.method == 'POST':
        consulta = request.POST.get('consulta')
        libros = LibroForm.objects.filter(title__icontains=consulta) | LibroForm.objects.filter(autor__icontains=consulta)
        return render(request, 'libros/libro_busqueda.html', {'libros': libros})
    return render(request, 'libros/libro_busqueda.html')