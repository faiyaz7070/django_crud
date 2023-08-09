from django.shortcuts import render, redirect
from .forms import KeyValueForm

data_dict = {} 

def create_view(request):
    if request.method == 'POST':
        form = KeyValueForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            value = form.cleaned_data['value']
            data_dict[key] = value
            return redirect('read')
    else:
        form = KeyValueForm()
    return render(request, 'create.html', {'form': form})

def read_view(request):
    return render(request, 'read.html', {'data_dict': data_dict})

def update_view(request):
    if request.method == 'POST':
        form = KeyValueForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            if key in data_dict:
                value = form.cleaned_data['value']
                data_dict[key] = value
                return redirect('read')
    else:
        form = KeyValueForm()
    return render(request, 'update.html', {'form': form})

def delete_view(request):
    if request.method == 'POST':
        key_to_delete = request.POST.get('key_to_delete')
        if key_to_delete in data_dict:
            del data_dict[key_to_delete]
            return redirect('read')
    return render(request, 'delete.html', {'data_dict': data_dict})
