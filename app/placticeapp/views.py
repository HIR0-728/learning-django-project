from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from placticeapp.models import Person
from placticeapp.forms import PersonForm


# Create your views here.
def person_list(request):
    persons = Person.objects.all().order_by("id")
    return render(request, "placticeapp/person_list.html", {"persons": persons})


def person_edit(request, person_id=None):
    if person_id:
        person = get_object_or_404(Person, pk=person_id)
    else:
        person = Person()

    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect("placticeapp:person_list")
    else:
        form = PersonForm(instance=person)
    return render(
        request, "placticeapp/person_edit.html", dict(form=form, person_id=person_id)
    )


def person_delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("placticeapp:person_list")
