from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import DestinationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def destination_list(request):
	destinations = Destination.objects.all().order_by('-id')
	return render(request, 'destinations/destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
	destination = get_object_or_404(Destination, pk=pk)
	return render(request, 'destinations/destination_detail.html', {'destination': destination})

@login_required
def destination_add(request):
	if request.method == 'POST':
		form = DestinationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Destination added!')
			return redirect('destination_list')
	else:
		form = DestinationForm()
	return render(request, 'destinations/destination_add.html', {'form': form})
