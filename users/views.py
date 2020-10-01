from django.urls import reverse_lazy
from django.views import generic
from .forms import ProfileUserCreationForm

class SignUp(generic.CreateView):
	form_class = ProfileUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'
