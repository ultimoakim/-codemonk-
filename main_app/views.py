from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Challenge
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def challenges_index(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/index.html', {
        'challenges': challenges
    })

@login_required
def challenges_user_index(request):
    challenges = Challenge.objects.filter(user=request.user)
    return render(request, 'challenges/userindex.html', {
        'challenges': challenges
    })

def challenges_detail(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    return render(request, 'challenges/detail.html', {
        'challenge': challenge
    })


class ChallengeCreate(LoginRequiredMixin, CreateView):
  model = Challenge
  fields = ['title', 'description']
  # success_url = '/challenges'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class ChallengeUpdate(LoginRequiredMixin, UpdateView):
  model = Challenge
  fields = '__all__'
    

class ChallengeDelete(LoginRequiredMixin, DeleteView):
  model = Challenge
  success_url = '/challenges'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)