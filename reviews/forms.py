from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['rating', 'comment']
		widgets = {
			'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your experience...'}),
			'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'step': 1}),
		}
