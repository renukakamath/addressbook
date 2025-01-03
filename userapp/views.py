from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect, get_object_or_404
from .models import Address
from django.contrib.auth.decorators import login_required

@login_required
def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'userapp/address_list.html', {'addresses': addresses})

@login_required
def address_create(request):
    if request.method == 'POST':
        # Form processing logic will be added later
        pass
    return render(request, 'userapp/address_form.html')

@login_required
def address_edit(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        # Form processing logic will be added later
        pass
    return render(request, 'userapp/address_form.html', {'address': address})

@login_required
def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        address.delete()
        return redirect('userapp:address_list')
    return render(request, 'userapp/address_confirm_delete.html', {'address': address})
