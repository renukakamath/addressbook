from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'adminapp/group_list.html', {'groups': groups})

@user_passes_test(is_admin)
def group_create(request):
    if request.method == 'POST':
        # Form processing logic will be added later
        pass
    return render(request, 'adminapp/group_form.html')

@user_passes_test(is_admin)
def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        # Form processing logic will be added later
        pass
    return render(request, 'adminapp/group_form.html', {'group': group})

@user_passes_test(is_admin)
def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('adminapp:group_list')
    return render(request, 'adminapp/group_confirm_delete.html', {'group': group})
