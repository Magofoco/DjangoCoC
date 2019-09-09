from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Seventhquestion
from django.utils import timezone
from django.contrib import messages


@login_required
def seventhquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['seventh_five']:
      question = Seventhquestion()
      try:
        question.seventh_one = request.FILES['seventh_one']
      except:
        question.seventh_one = "There-is-no-file"
      try:
        question.seventh_two = request.FILES['seventh_two']
      except:
        question.seventh_two = "There-is-no-file"
      try:
        question.seventh_three = request.FILES['seventh_three']
      except:
        question.seventh_three = "There-is-no-file"
      try:
        question.seventh_four = request.FILES['seventh_four']
      except:
        question.seventh_four = "There-is-no-file"
      question.seventh_five = request.POST['seventh_five']
      question.seventh_six = request.POST['seventh_six']
      question.seventh_seven = request.POST['seventh_seven']
      question.seventh_eight = request.POST['seventh_eight']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers saved for Transparency in data science')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'seventhquestions/seventhquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'seventhquestions/seventhquestionstoanswer.html', {'project':project})


@login_required
def seventhquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'seventhquestions/seventhquestionsdetail.html', {'project':project})


@login_required
def seventhquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['seventh_five']:
      question = Seventhquestion.objects.filter(project=project).first()
      try:
        question.seventh_one = request.FILES['seventh_one']
      except:
        # question.third_seven = "There-is-no-file"
        if project.seventhquestion.seventh_one:
          question.seventh_one = project.seventhquestion.seventh_one
        else:
          question.seventh_one = "There-is-no-file"
      try:
        question.seventh_two = request.FILES['seventh_two']
      except:
        # question.third_seven = "There-is-no-file"
        if project.seventhquestion.seventh_two:
          question.seventh_two = project.seventhquestion.seventh_two
        else:
          question.seventh_two = "There-is-no-file"
      try:
        question.seventh_three = request.FILES['seventh_three']
      except:
        # question.third_seven = "There-is-no-file"
        if project.seventhquestion.seventh_three:
          question.seventh_three = project.seventhquestion.seventh_three
        else:
          question.seventh_three = "There-is-no-file"
      try:
        question.seventh_four = request.FILES['seventh_four']
      except:
        # question.third_seven = "There-is-no-file"
        if project.seventhquestion.seventh_four:
          question.seventh_four = project.seventhquestion.seventh_four
        else:
          question.seventh_four = "There-is-no-file"

      question.seventh_five = request.POST['seventh_five']
      question.seventh_six = request.POST['seventh_six']
      question.seventh_seven = request.POST['seventh_seven']
      question.seventh_eight = request.POST['seventh_eight']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers for Transparency in data science questions have been edited')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'seventhquestions/seventhquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'seventhquestions/seventhquestionsedit.html', {'project':project})





