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
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_relation = django_form.data.get("relation")
            new_member_phone = django_form.data.get('phone')
            new_member_email = django_form.data.get('email')
            
            """ This is how your model connects to database and create a new member """
            Contact.objects.create(
                name =  new_member_name, 
                relation = new_member_relation,
                phone = new_member_phone,
                email = new_member_email, 
                )
                 
            contact_list = Contact.objects.all()
            return render(request, 'mycontacts/show.html',{'contacts': contact_list})    
        
        else:
            """ redirect to the same page if django_form goes wrong """
            return render(request, 'mycontacts/add.html')
    else:
        return render(request, 'mycontacts/add.html')
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
