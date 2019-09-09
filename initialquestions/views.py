from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Initialquestion
from django.utils import timezone
from django.contrib import messages
from projects.models import Project
from .forms import InitialquestionForm

@login_required
def initialquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST.get('initial_one') and request.POST.get('initial_two') :
      question = Initialquestion()
      question.initial_one = request.POST.getlist('initial_one')
      question.initial_two = request.POST.getlist('initial_two')
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Initial questions are created')
      # import pdb; pdb.set_trace()
      return redirect('/projects/allprojects')

    # else:
    #   return render(request, 'initialquestions/initialquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'initialquestions/initialquestionstoanswer.html', {'project':project})

@login_required
def initialquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST.get('initial_one') and request.POST.get('initial_two'):
      question = Initialquestion.objects.filter(project=project).first()
      question.initial_one = request.POST.getlist('initial_one')
      question.initial_two = request.POST.getlist('initial_two')
      question.save()
      messages.success(request, 'Initial questions answer have been edited')
      return redirect('/projects/allprojects')
    # else:
    #   return render(request, 'initialquestions/initialquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'initialquestions/initialquestionsedit.html', {'project':project})




@login_required
def initialquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  # import pdb; pdb.set_trace()
  return render(request, 'initialquestions/initialquestionsdetail.html', {'project':project})

