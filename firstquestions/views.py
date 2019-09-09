from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Firstquestion
from django.utils import timezone
from django.contrib import messages
from projects.models import Project

# Create your views here.



@login_required
def firstquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    # if request.POST['first_one']:
      question = Firstquestion()
      question.first_one = request.POST['first_one']
      question.first_two = request.POST['first_two']
      question.first_three = request.POST['first_three']
      question.first_four = request.POST['first_four']
      question.first_five = request.POST['first_five']
      question.first_six = request.POST['first_six']
      # question.first_seven = request.POST['first_seven']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Questions of User Centered Design questions are created')
      return redirect('/projects/allprojects')
    # else:
    #   return render(request, 'firstquestions/firstquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'firstquestions/firstquestionstoanswer.html', {'project':project})


@login_required
def firstquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'firstquestions/firstquestionsdetail.html', {'project':project})


@login_required
def firstquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['first_six']:
      question = Firstquestion.objects.filter(project=project).first()
      question.first_one = request.POST['first_one']
      question.first_two = request.POST['first_two']
      question.first_three = request.POST['first_three']
      question.first_four = request.POST['first_four']
      question.first_five = request.POST['first_five']
      question.first_six = request.POST['first_six']
      # question.first_seven = request.POST['first_seven']
      question.save()
      messages.success(request, 'Answers for User Centered Design questions have been edited')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'firstquestions/firstquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'firstquestions/firstquestionsedit.html', {'project':project})



