from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Sixthquestion
from django.utils import timezone
from django.contrib import messages


@login_required
def sixthquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['sixth_thirteen']:
      question = Sixthquestion()
      try:
        question.sixth_one = request.FILES['sixth_one']
      except:
        question.sixth_one = "There-is-no-file"
      try:
        question.sixth_two = request.FILES['sixth_two']
      except:
        question.sixth_two = "There-is-no-file"
      try:
        question.sixth_three = request.FILES['sixth_three']
      except:
        question.sixth_three = "There-is-no-file"
      try:
        question.sixth_four = request.FILES['sixth_four']
      except:
        question.sixth_four = "There-is-no-file"
      try:
        question.sixth_five = request.FILES['sixth_five']
      except:
        question.sixth_five = "There-is-no-file"
      try:
        question.sixth_six = request.FILES['sixth_six']
      except:
        question.sixth_six = "There-is-no-file"
      try:
        question.sixth_seven = request.FILES['sixth_seven']
      except:
        question.sixth_seven = "There-is-no-file"
      question.sixth_eight = request.POST['sixth_eight']
      question.sixth_nine = request.POST['sixth_nine']
      question.sixth_ten = request.POST['sixth_ten']
      question.sixth_eleven = request.POST['sixth_eleven']
      question.sixth_twelve = request.POST['sixth_twelve']
      question.sixth_thirteen = request.POST['sixth_thirteen']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers saved for Transparency in data science')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'sixthquestions/sixthquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'sixthquestions/sixthquestionstoanswer.html', {'project':project})


@login_required
def sixthquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'sixthquestions/sixthquestionsdetail.html', {'project':project})


@login_required
def sixthquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['sixth_thirteen']:
      question = Sixthquestion.objects.filter(project=project).first()
      try:
        question.sixth_one = request.FILES['sixth_one']
      except:
        # question.third_seven = "There-is-no-file"
        if project.sixthquestion.sixth_one:
          question.sixth_one = project.sixthquestion.sixth_one
        else:
          question.sixth_one = "There-is-no-file"
      try:
        question.sixth_two = request.FILES['sixth_two']
      except:
        # question.third_seven = "There-is-no-file"
        if project.sixthquestion.sixth_two:
          question.sixth_two = project.sixthquestion.sixth_two
        else:
          question.sixth_two = "There-is-no-file"
      try:
        question.sixth_three = request.FILES['sixth_three']
      except:
        # question.third_seven = "There-is-no-file"
        if project.sixthquestion.sixth_three:
          question.sixth_three = project.sixthquestion.sixth_three
        else:
          question.sixth_three = "There-is-no-file"
      try:
        question.sixth_four = request.FILES['sixth_four']
      except:
        # question.third_seven = "There-is-no-file"
        if project.sixthquestion.sixth_four:
          question.sixth_four = project.sixthquestion.sixth_four
        else:
          question.sixth_four = "There-is-no-file"
      try:
        question.sixth_five = request.FILES['sixth_five']
      except:
        # question.third_seven = "There-is-no-file"
        if project.sixthquestion.sixth_five:
          question.sixth_five = project.sixthquestion.sixth_five
        else:
          question.sixth_five = "There-is-no-file"
      try:
        question.sixth_six = request.FILES['sixth_six']
      except:
        # question.third_seven = "There-is-no-file"
        if project.sixthquestion.sixth_six:
          question.sixth_six = project.sixthquestion.sixth_six
        else:
          question.sixth_six = "There-is-no-file"
      try:
        question.sixth_seven = request.FILES['sixth_seven']
      except:
        # question.third_seven = "There-is-no-file"
        if project.sixthquestion.sixth_seven:
          question.sixth_seven = project.sixthquestion.sixth_seven
        else:
          question.sixth_seven = "There-is-no-file"

      question.sixth_eight = request.POST['sixth_eight']
      question.sixth_nine = request.POST['sixth_nine']
      question.sixth_ten = request.POST['sixth_ten']
      question.sixth_eleven = request.POST['sixth_eleven']
      question.sixth_twelve = request.POST['sixth_twelve']
      question.sixth_thirteen = request.POST['sixth_thirteen']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers for Transparency in data science questions have been edited')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'sixthquestions/sixthquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'sixthquestions/sixthquestionsedit.html', {'project':project})





