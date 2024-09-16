from django.shortcuts import render, get_object_or_404, redirect
from .models import ComicbookCollection
from .forms import ComicbookForm


# Render landing page for comics collection app:
def collection(request):
    collection_data = ComicbookCollection.object.all()
    return render(request, 'comicbooks.html', {'comic_collection': collection_data})


# Render a page where the user can log a new addition into their comic book collection:
def add_to_collection(request):
    form = ComicbookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('collection')
    else:
        print(form.errors)
        form = ComicbookForm()
        return render(request, 'add_issue.html', {'form': form, })


# Renders a page where the user can view comic book entry details and edit them if desired:
def edit_collection(request, pk):
    pk = int(pk)
    entry = get_object_or_404(ComicbookCollection, pk=pk)
    form1 = ComicbookForm(data=request.POST or None, instance=entry)

    if request.method == 'POST':
        if form1.is_valid():
            form2 = form1.save(commit=False)
            form2.save()
            return redirect('collection')
        else:
            print(form1.errors)
    else:
        return render(request, 'edit_comic.html', {'form': form1})


# Render a page where the user can delete an entry from their comic book collection
def delete(request, pk):
    pk = int(pk)
    entry = get_object_or_404(ComicbookCollection, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('collection')
    else:
        return render(request, "delete_comic.html", {'entry': entry})


def confirmed(request):
    if request.method == 'POST':
        # Create form
        form = ComicbookForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('collection')
    else:
        return redirect('collection')
