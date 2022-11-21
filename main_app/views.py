from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Challenge

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

def challenges_detail(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    return render(request, 'challenges/detail.html', {
        'challenge': challenge
    })

class ChallengeCreate(CreateView):
  model = Challenge
  fields = '__all__'
  # success_url = '/challenges'

class ChallengeUpdate(UpdateView):
  model = Challenge
  fields = '__all__'


class ChallengeDelete(DeleteView):
  model = Challenge
  success_url = '/challenges'