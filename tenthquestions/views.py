from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Tenthquestion
from django.utils import timezone
from django.contrib import messages


@login_required
def tenthquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['tenth_eleven']:
      question = Tenthquestion()
      try:
        question.tenth_one = request.FILES['tenth_one']
      except:
        question.tenth_one = "There-is-no-file"
      try:
        question.tenth_two = request.FILES['tenth_two']
      except:
        question.tenth_two = "There-is-no-file"
      try:
        question.tenth_three = request.FILES['tenth_three']
      except:
        question.tenth_three = "There-is-no-file"
      question.tenth_four = request.POST['tenth_four']
      try:
        question.tenth_five = request.FILES['tenth_five']
      except:
        question.tenth_five = "There-is-no-file"



      question.tenth_six = request.POST['tenth_six']
      question.tenth_seven = request.POST['tenth_seven']
      question.tenth_eight = request.POST['tenth_eight']
      question.tenth_nine = request.POST['tenth_nine']
      question.tenth_ten = request.POST['tenth_ten']
      question.tenth_eleven = request.POST['tenth_eleven']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers saved for Commercial issues')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'tenthquestions/tenthquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'tenthquestions/tenthquestionstoanswer.html', {'project':project})


@login_required
def tenthquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'tenthquestions/tenthquestionsdetail.html', {'project':project})


@login_required
def tenthquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['tenth_eleven']:
      question = Tenthquestion.objects.filter(project=project).first()

      try:
        question.tenth_one = request.FILES['tenth_one']
      except:
        # question.third_seven = "There-is-no-file"
        if project.tenthquestion.tenth_one:
          question.tenth_one = project.tenthquestion.tenth_one
        else:
          question.tenth_one = "There-is-no-file"

      try:
        question.tenth_two = request.FILES['tenth_two']
      except:
        # question.third_seven = "There-is-no-file"
        if project.tenthquestion.tenth_two:
          question.tenth_two = project.tenthquestion.tenth_two
        else:
          question.tenth_two = "There-is-no-file"

      try:
        question.tenth_three = request.FILES['tenth_three']
      except:
        # question.third_seven = "There-is-no-file"
        if project.tenthquestion.tenth_three:
          question.tenth_three = project.tenthquestion.tenth_three
        else:
          question.tenth_three = "There-is-no-file"

      question.tenth_four = request.POST['tenth_four']

      try:
        question.tenth_five = request.FILES['tenth_five']
      except:
        # question.third_seven = "There-is-no-file"
        if project.tenthquestion.tenth_five:
          question.tenth_five = project.tenthquestion.tenth_five
        else:
          question.tenth_five = "There-is-no-file"

      question.tenth_six = request.POST['tenth_six']
      question.tenth_seven = request.POST['tenth_seven']
      question.tenth_eight = request.POST['tenth_eight']
      question.tenth_nine = request.POST['tenth_nine']
      question.tenth_ten = request.POST['tenth_ten']
      question.tenth_eleven = request.POST['tenth_eleven']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers for Commercial issues questions have been edited')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'tenthquestions/tenthquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'tenthquestions/tenthquestionsedit.html', {'project':project})





