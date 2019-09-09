from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Thirdquestion
from django.utils import timezone
from django.contrib import messages
from django.http import FileResponse, Http404



@login_required
def thirdquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    # if request.POST['third_one'] and request.POST['third_two'] and request.POST['third_three'] and request.POST['third_four'] and request.POST['third_five'] and request.POST['third_seven'] and request.POST['third_eight'] and request.POST['third_nine'] and request.POST['third_ten']:
      question = Thirdquestion()
      question.third_one = request.POST['third_one']
      question.third_two = request.POST['third_two']
      question.third_three = request.POST['third_three']
      question.third_four = request.POST['third_four']
      question.third_five = request.POST['third_five']
      question.third_six = request.POST['third_six']
      try:
        question.third_seven = request.FILES['third_seven']
      except:
        question.third_seven = "There-is-no-file"
      question.third_eight = request.POST['third_eight']
      question.third_nine = request.POST['third_nine']
      try:
        question.third_ten = request.FILES['third_ten']
      except:
        question.third_ten = "There-is-no-file"
      question.developer = request.user
      question.project = project
      question.save()
      # import pdb; pdb.set_trace()
      messages.success(request, 'Answers saved for Data use')
      return redirect('/projects/allprojects')
    # else:
    #   return render(request, 'thirdquestions/thirdquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'thirdquestions/thirdquestionstoanswer.html', {'project':project})


@login_required
def thirdquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'thirdquestions/thirdquestionsdetail.html', {'project':project})


@login_required
def thirdquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  # import pdb; pdb.set_trace()

  if request.method == 'POST':
    # if request.POST['third_one'] and request.POST['third_two'] and request.POST['third_three'] and request.POST['third_four'] and request.POST['third_five'] and request.POST['third_eight'] and request.POST['third_nine']:
      question = Thirdquestion.objects.filter(project=project).first()
      question.third_one = request.POST['third_one']
      question.third_two = request.POST['third_two']
      question.third_three = request.POST['third_three']
      question.third_four = request.POST['third_four']
      question.third_five = request.POST['third_five']
      question.third_six = request.POST['third_six']
      try:
        question.third_seven = request.FILES['third_seven']
      except:
        # question.third_seven = "There-is-no-file"
          if project.thirdquestion.third_seven:
              question.third_seven = project.thirdquestion.third_seven
          else:
            question.third_seven = "There-is-no-file"
      question.third_eight = request.POST['third_eight']
      question.third_nine = request.POST['third_nine']
      try:
        question.third_ten = request.FILES['third_ten']
      except:
        # question.third_seven = "There-is-no-file"
          if project.thirdquestion.third_ten:
              question.third_ten = project.thirdquestion.third_ten
          else:
            question.third_ten = "There-is-no-file"
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers for Data use questions have been edited')
      return redirect('/projects/allprojects')
    # else:
    #   return render(request, 'thirdquestions/thirdquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'thirdquestions/thirdquestionsedit.html', {'project':project})


