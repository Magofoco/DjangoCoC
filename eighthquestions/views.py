from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Eighthquestion
from django.utils import timezone
from django.contrib import messages


@login_required
def eighthquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['eighth_one']:
      question = Eighthquestion()
      question.eighth_one = request.POST['eighth_one']
      question.eighth_two = request.POST['eighth_two']
      question.eighth_three = request.POST['eighth_three']
      question.eighth_four = request.POST['eighth_four']
      try:
        question.eighth_five = request.FILES['eighth_five']
      except:
        question.eighth_five = "There-is-no-file"
      try:
        question.eighth_six = request.FILES['eighth_six']
      except:
        question.eighth_six = "There-is-no-file"
      try:
        question.eighth_seven = request.FILES['eighth_seven']
      except:
        question.eighth_seven = "There-is-no-file"
      try:
        question.eighth_eight = request.FILES['eighth_eight']
      except:
        question.eighth_eight = "There-is-no-file"
      try:
        question.eighth_nine = request.FILES['eighth_nine']
      except:
        question.eighth_nine = "There-is-no-file"

      question.eighth_ten = request.POST['eighth_ten']
      question.eighth_eleven = request.POST['eighth_eleven']
      question.eighth_twelve = request.POST['eighth_twelve']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers saved for Risk and Rewards')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'eighthquestions/eighthquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'eighthquestions/eighthquestionstoanswer.html', {'project':project})


@login_required
def eighthquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'eighthquestions/eighthquestionsdetail.html', {'project':project})


@login_required
def eighthquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['eighth_one']:
      question = Eighthquestion.objects.filter(project=project).first()
      question.eighth_one = request.POST['eighth_one']
      question.eighth_two = request.POST['eighth_two']
      question.eighth_three = request.POST['eighth_three']
      question.eighth_four = request.POST['eighth_four']
      try:
        question.eighth_five = request.FILES['eighth_five']
      except:
        # question.third_seven = "There-is-no-file"
        if project.eighthquestion.eighth_five:
          question.eighth_five = project.eighthquestion.eighth_five
        else:
          question.eighth_five = "There-is-no-file"
      try:
        question.eighth_six = request.FILES['eighth_six']
      except:
        # question.third_seven = "There-is-no-file"
        if project.eighthquestion.eighth_six:
          question.eighth_six = project.eighthquestion.eighth_six
        else:
          question.eighth_six = "There-is-no-file"
      try:
        question.eighth_seven = request.FILES['eighth_seven']
      except:
        # question.third_seven = "There-is-no-file"
        if project.eighthquestion.eighth_seven:
          question.eighth_seven = project.eighthquestion.eighth_seven
        else:
          question.eighth_seven = "There-is-no-file"
      try:
        question.eighth_eight = request.FILES['eighth_eight']
      except:
        # question.third_seven = "There-is-no-file"
        if project.eighthquestion.eighth_eight:
          question.eighth_eight = project.eighthquestion.eighth_eight
        else:
          question.eighth_eight = "There-is-no-file"
      try:
        question.eighth_nine = request.FILES['eighth_nine']
      except:
        # question.third_seven = "There-is-no-file"
        if project.eighthquestion.eighth_nine:
          question.eighth_nine = project.eighthquestion.eighth_nine
        else:
          question.eighth_nine = "There-is-no-file"

      question.eighth_ten = request.POST['eighth_ten']
      question.eighth_eleven = request.POST['eighth_eleven']
      question.eighth_twelve = request.POST['eighth_twelve']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers for Risk and Rewards questions have been edited')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'eighthquestions/eighthquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'eighthquestions/eighthquestionsedit.html', {'project':project})





