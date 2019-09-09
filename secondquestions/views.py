from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Secondquestion
# from .models import SecondquestionForm
from django.utils import timezone
from django.contrib import messages

# @login_required
# def secondquestionstoanswer(request, project_id):
#   project = get_object_or_404(Project, pk=project_id)
#   if request.method == "POST":
#     form = SecondquestionForm(request.POST)
#     if form.is_valid():
#       form.instance.project = project
#       form.instance.developer = request.user
#       form.save()
#       messages.success(request, 'Answers saved for Maintenance of the value proposition')
#       return redirect('/projects/allprojects')
#   else:
#     form = SecondquestionForm()
#   return render(request, 'secondquestions/secondquestionstoanswer.html', {'project':project, 'form': form})


@login_required
def secondquestionstoanswer(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    # if request.POST['second_one']:
      question = Secondquestion()
      question.second_one = request.POST['second_one']
      question.second_two = request.POST['second_two']
      question.second_three = request.POST['second_three']
      question.second_four = request.POST['second_four']
      question.second_five = request.POST['second_five']
      question.second_six = request.POST['second_six']
      question.second_seven = request.POST['second_seven']
      question.second_eight = request.POST['second_eight']
      question.second_nine = request.POST['second_nine']
      question.developer = request.user
      question.project = project
      question.save()
      messages.success(request, 'Answers saved for Maintenance of the value proposition')
      return redirect('/projects/allprojects')
    # else:
    #   return render(request, 'secondquestions/secondquestionstoanswer.html', {'error':'All fields are required.'})
  return render(request, 'secondquestions/secondquestionstoanswer.html', {'project':project})


@login_required
def secondquestionsdetail(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'secondquestions/secondquestionsdetail.html', {'project':project})


@login_required
def secondquestionsedit(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    # if request.POST['second_one']:
      question = Secondquestion.objects.filter(project=project).first()
      question.second_one = request.POST['second_one']
      question.second_two = request.POST['second_two']
      question.second_three = request.POST['second_three']
      question.second_four = request.POST['second_four']
      question.second_five = request.POST['second_five']
      question.second_six = request.POST['second_six']
      question.second_seven = request.POST['second_seven']
      question.second_eight = request.POST['second_eight']
      question.second_nine = request.POST['second_nine']
      question.save()
      messages.success(request, 'Answers for User Centered Design questions have been edited')
      return redirect('/projects/allprojects')
    # else:
    #   return render(request, 'secondquestions/secondquestionsedit.html', {'error':'All fields are required.'})
  return render(request, 'secondquestions/secondquestionsedit.html', {'project':project})


