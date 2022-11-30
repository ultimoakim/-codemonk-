from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Challenge, Comment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm

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

def CommentToggle(request, pk):
  comment = Comment.objects.get(id = pk)
  if comment.likes.contains(request.user):
    comment.likes.remove(request.user)
  else:
    comment.likes.add(request.user)
  return redirect('detail', challenge_id = comment.challenge.id)


@login_required
def challenges_user_index(request):
    challenges = Challenge.objects.filter(user=request.user)
    return render(request, 'challenges/userindex.html', {
      'challenges': challenges
    })

def challenges_detail(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    comment_form = CommentForm()
    return render(request, 'challenges/detail.html', {
      'challenge': challenge,
      'comment_form': comment_form,
    })

class ChallengeCreate(LoginRequiredMixin, CreateView):
  model = Challenge
  fields = ['title', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ChallengeUpdate(LoginRequiredMixin, UpdateView):
  model = Challenge
  fields = ['title', 'description']

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

class CommentList(ListView):
  model = Comment
  fields = ['user', 'date', 'description']

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    likes_connected = get_object_or_404(Comment, id=self.kwargs['pk'])
    liked = False
    if likes_connected.likes.filter(id=self.request.user.id).exists():
      liked = True
    data['number_of_likes'] = likes_connected.number_of_likes()
    data['post_is_liked'] = liked
    return data

def add_comment(request, challenge_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.challenge_id = challenge_id
    new_comment.user = request.user
    new_comment.save()
  return redirect('detail', challenge_id=challenge_id)

class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  def get_success_url(self):
    return f"/challenges/{self.object.challenge.id}"

class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  def get_success_url(self):
    return f"/challenges/{self.object.challenge.id}"
  fields = ['description']







