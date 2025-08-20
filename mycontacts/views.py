from django.shortcuts import render
from .forms import AddForm
from .models import Contact
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

def show(request):
    """ 
    This function gets all the members in your Database through your Model
    Any further usage please refer to: https://docs.djangoproject.com/el/1.10/ref/models/querysets/
    """
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/show.html',{'contacts': contact_list})
    
def add(request):
    """ Adiciona um contato ao banco de dados """
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()  # Salva diretamente no banco
            return redirect('show')  # Redireciona para a página que mostra os contatos
    else:
        form = AddForm()  # Se for GET, apenas exibe o formulário vazio

    return render(request, 'mycontacts/add.html', {'form': form})
# READ (detalhes de 1 contato)
def detail(request, id):
    contact = get_object_or_404(Contact, pk=id)
    return render(request, 'mycontacts/detail.html', {'contact': contact})

def edit(request, id):
    contact = get_object_or_404(Contact, pk=id)
    if request.method == "POST":
        contact.name = request.POST.get("name")
        contact.relation = request.POST.get("relation")
        contact.phone = request.POST.get("phone")
        contact.email = request.POST.get("email")
        contact.save()
        return redirect('detail', id=contact.id)  # agora vai para a página de detalhes
    return render(request, 'mycontacts/edit.html', {'contact': contact})

def delete(request, id):
    contact = get_object_or_404(Contact, pk=id)
    if request.method == "POST":
        contact.delete()
        return redirect('show')  # agora redireciona para a lista de contatos
    return render(request, 'mycontacts/delete.html', {'contact': contact})
