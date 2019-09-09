from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Fifthquestion
from django.utils import timezone
from django.contrib import messages


@login_required
def fifthquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['fifth_one']:
      question = Fifthquestion()
      question.fifth_one = request.POST['fifth_one']
      question.fifth_two = request.POST['fifth_two']
      question.fifth_three = request.POST['fifth_three']
      question.fifth_four = request.POST['fifth_four']
      question.fifth_five = request.POST['fifth_five']
      question.fifth_six = request.POST['fifth_six']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers saved for Openness')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'fifthquestions/fifthquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'fifthquestions/fifthquestionstoanswer.html', {'project':project})


@login_required
def fifthquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'fifthquestions/fifthquestionsdetail.html', {'project':project})


@login_required
def fifthquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['fifth_one']:
      question = Fifthquestion.objects.filter(project=project).first()
      question.fifth_one = request.POST['fifth_one']
      question.fifth_two = request.POST['fifth_two']
      question.fifth_three = request.POST['fifth_three']
      question.fifth_four = request.POST['fifth_four']
      question.fifth_five = request.POST['fifth_five']
      question.fifth_six = request.POST['fifth_six']
      question.save()
      messages.success(request, 'Answers for Openness questions have been edited')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'fifthquestions/fifthquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'fifthquestions/fifthquestionsedit.html', {'project':project})





