from .Students import SStudents
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound


# получение данных из бд
def index(request):
    people = SStudents.objects.all()
    return render(request, "Studentsname.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = SStudents()
        person.first_name = request.POST.get("first_name")
        person.second_name = request.POST.get("second_name")
        person.save()
        people = SStudents.objects.all()
        return render(request, "Create.html", {"people": people})
    #return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = SStudents.objects.get(id=id)

        if request.method == "POST":
            person.first_name = request.POST.get("first_name")
            person.second_name = request.POST.get("second_name")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "name.html", {"person": person})
    except SStudents.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = SStudents.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("")
    except SStudents.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
