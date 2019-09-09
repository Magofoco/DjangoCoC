from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Fourthquestion
from django.utils import timezone
from django.contrib import messages


@login_required
def fourthquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['fourth_one']:
      question = Fourthquestion()
      question.fourth_one = request.POST['fourth_one']
      question.fourth_two = request.POST['fourth_two']
      question.fourth_three = request.POST['fourth_three']
      question.fourth_four = request.POST['fourth_four']
      question.fourth_five = request.POST['fourth_five']
      try:
        question.fourth_six = request.FILES['fourth_six']
      except:
        question.fourth_six = "There-is-no-file"
      try:
        question.fourth_seven = request.FILES['fourth_seven']
      except:
        question.fourth_seven = "There-is-no-file"
      question.fourth_eight = request.POST['fourth_eight']
      try:
        question.fourth_nine = request.FILES['fourth_nine']
      except:
        question.fourth_nine = "There-is-no-file"
      # question.fourth_ten = request.POST['fourth_ten']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers saved for Data Protection')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'fourthquestions/fourthquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'fourthquestions/fourthquestionstoanswer.html', {'project':project})


@login_required
def fourthquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'fourthquestions/fourthquestionsdetail.html', {'project':project})


@login_required
def fourthquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['fourth_one']:
      question = Fourthquestion.objects.filter(project=project).first()
      question.fourth_one = request.POST['fourth_one']
      question.fourth_two = request.POST['fourth_two']
      question.fourth_three = request.POST['fourth_three']
      question.fourth_four = request.POST['fourth_four']
      question.fourth_five = request.POST['fourth_five']
      try:
        question.fourth_six = request.FILES['fourth_six']
      except:
        # question.third_seven = "There-is-no-file"
          if project.fourthquestion.fourth_six:
              question.fourth_six = project.fourthquestion.fourth_six
          else:
            question.fourth_six = "There-is-no-file"
      try:
        question.fourth_seven = request.FILES['fourth_seven']
      except:
        # question.third_seven = "There-is-no-file"
          if project.fourthquestion.fourth_seven:
              question.fourth_seven = project.fourthquestion.fourth_seven
          else:
            question.fourth_seven = "There-is-no-file"
      question.fourth_eight = request.POST['fourth_eight']
      try:
        question.fourth_nine = request.FILES['fourth_nine']
      except:
        # question.third_seven = "There-is-no-file"
          if project.fourthquestion.fourth_nine:
              question.fourth_nine = project.fourthquestion.fourth_nine
          else:
            question.fourth_nine = "There-is-no-file"
      # question.fourth_ten = request.POST['fourth_ten']
      question.developer = request.user
      question.project = project
      # question.fourth_ten = request.POST['fourth_ten']
      question.save()
      messages.success(request, 'Answers for Data Protection questions have been edited')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'fourthquestions/fourthquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'fourthquestions/fourthquestionsedit.html', {'project':project})





