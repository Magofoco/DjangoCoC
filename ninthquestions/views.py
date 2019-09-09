from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Ninthquestion
from django.utils import timezone
from django.contrib import messages


@login_required
def ninthquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['ninth_nine']:
      question = Ninthquestion()
      question.ninth_one = request.POST['ninth_one']
      try:
        question.ninth_two = request.FILES['ninth_two']
      except:
        question.ninth_two = "There-is-no-file"
      try:
        question.ninth_three = request.FILES['ninth_three']
      except:
        question.ninth_three = "There-is-no-file"
      question.ninth_four = request.POST['ninth_four']
      question.ninth_five = request.POST['ninth_five']
      question.ninth_six = request.POST['ninth_six']
      try:
        question.ninth_seven = request.FILES['ninth_seven']
      except:
        question.ninth_seven = "There-is-no-file"
      question.ninth_nine = request.POST['ninth_nine']

      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers saved for Data solutions')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'ninthquestions/ninthquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'ninthquestions/ninthquestionstoanswer.html', {'project':project})


@login_required
def ninthquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'ninthquestions/ninthquestionsdetail.html', {'project':project})


@login_required
def ninthquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['ninth_nine']:
      question = Ninthquestion.objects.filter(project=project).first()
      question.ninth_one = request.POST['ninth_one']

      try:
        question.ninth_two = request.FILES['ninth_two']
      except:
        # question.third_seven = "There-is-no-file"
        if project.ninthquestion.ninth_two:
          question.ninth_two = project.ninthquestion.ninth_two
        else:
          question.ninth_two = "There-is-no-file"
      try:
        question.ninth_three = request.FILES['ninth_three']
      except:
        # question.third_seven = "There-is-no-file"
        if project.ninthquestion.ninth_three:
          question.ninth_three = project.ninthquestion.ninth_three
        else:
          question.ninth_three = "There-is-no-file"
      question.ninth_four = request.POST['ninth_four']
      question.ninth_five = request.POST['ninth_five']
      question.ninth_six = request.POST['ninth_six']

      try:
        question.ninth_seven = request.FILES['ninth_seven']
      except:
        # question.third_seven = "There-is-no-file"
        if project.ninthquestion.ninth_seven:
          question.ninth_seven = project.ninthquestion.ninth_seven
        else:
          question.ninth_seven = "There-is-no-file"
      question.ninth_nine = request.POST['ninth_nine']

      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers for Data solutions questions have been edited')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'ninthquestions/ninthquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'ninthquestions/ninthquestionsedit.html', {'project':project})





