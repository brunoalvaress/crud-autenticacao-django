from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if (form.is_valid()):
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if (form.is_valid()):
        form.save()
        return redirect('persons_list')

    return render(request, 'person_form.html', {'form': form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')

    return render(request, 'person_delete.html', {'form': form})