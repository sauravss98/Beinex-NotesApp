from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
# Create your views here.
def NoteAdd(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/noteshow")
    else:
        form = NoteForm()
    return render(request, "notes/noteadd.html", {"form": form})


def ViewNote(request):
    notes = Note.objects.all()
    return render(request, "notes/noteshow.html", {"notes":notes})


def EditNote(request, id):
    note = Note.objects.get(id=id)
    return render(request, "notes/noteedit.html", {"note":note})


def UpdateNote(request, id):
    note = Note.objects.get(id=id)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        form.save()
        return redirect("/noteshow")
    return render(request, "notes/noteedit.html", {"note":note})


def DestroyNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect("/noteshow")
