from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm

@login_required
def reviews_page(request):
	if request.method == 'POST':
		form = ReviewForm(request.POST, request.FILES)
		if form.is_valid():
			review = form.save(commit=False)
			review.user = request.user
			review.save()
			return redirect('reviews_page')
	else:
		form = ReviewForm()
	reviews = Review.objects.all().order_by('-created_at')
	return render(request, 'reviews/review_base.html', {'form': form, 'reviews': reviews})
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm

@login_required
def reviews_page(request):
	if request.method == 'POST':
		form = ReviewForm(request.POST, request.FILES)
		if form.is_valid():
			review = form.save(commit=False)
			review.user = request.user
			# Automatically attach user's profile pic
			user_profile = getattr(request.user, 'user_profile', None)
			if user_profile and user_profile.profile_pic:
				review.avatar = user_profile.profile_pic
			review.save()
			return redirect('reviews_page')
	else:
		form = ReviewForm()
	reviews = Review.objects.all().order_by('-created_at')
	return render(request, 'reviews/review_base.html', {'form': form, 'reviews': reviews})

from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def index(request):
	reviews = Review.objects.order_by('-created_at')
	form = ReviewForm(request.POST or None, request.FILES or None)
	if request.method == "POST" and form.is_valid():
		review = form.save(commit=False)
		if request.user.is_authenticated:
			review.user = request.user
		review.save()
		return redirect('reviews_index')
	return render(request, 'reviews/review_base.html', {"reviews": reviews, "form": form})
