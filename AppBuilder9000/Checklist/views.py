from django.shortcuts import render, get_object_or_404, redirect
from .models import WashingtonPark
from .forms import ParkForm


def home(request):
    parks_info = WashingtonPark.object.all()
    return render(request, 'Washington.html', {'parklist': parks_info})


# Function to use a selected park's primary key to pull all that park's info and render it into the ParkForm on the park_info page:
def park_details(request, pk):
    pk = int(pk)
    park = get_object_or_404(WashingtonPark, pk=pk)
    form = ParkForm(data=request.POST or None, instance=park)
    context = {'form': form, 'park': park}

    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('home')

        else:
            print(form.errors)

    else:
        return render(request, 'park_info.html', context)

# TO-DO:  As new states are added, the above function may need to be refactored to work for all states or renamed to be state-specific
