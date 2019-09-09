from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from users.models import CustomUser
from seventhquestions.models import Seventhquestion
from django.utils import timezone
from django.contrib import messages
import plotly.graph_objects as go
from plotly.offline import plot
import plotly.express as px
import pandas as pd

@login_required
def allprojects(request):
    projects = Project.objects
    return render(request, 'projects/allprojects.html', {'projects': projects})

@login_required
def createproject(request):
  if request.method == 'POST':
    if request.POST['title'] and request.POST['content']:
      project = Project()
      project.title = request.POST['title']
      project.content = request.POST['content']
      project.developer = request.user
      project.save()
      messages.success(request, 'New project created')
      return redirect('/projects/allprojects')
    else:
      return render(request, 'projects/createproject.html', {'error':'All fields are required.'})
  else:
    return render(request, 'projects/createproject.html')

@login_required
def projectdetail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/projectdetail.html', {'project':project})

@login_required
def editproject(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['title'] and request.POST['content']:
      project.title = request.POST['title']
      project.content = request.POST['content']
      project.developer = request.user
      project.save()
      messages.success(request, 'Sucess edit project')
      return redirect('/projects/allprojects')
  return render(request, 'projects/editproject.html', {'error':'All fields are required.','project':project})


@login_required
def deleteproject(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if project.delete():
    messages.success(request, 'Project has been deleted')
    return redirect('/projects/allprojects')
  else:
    return redirect('/projects/')

@login_required
def auditproject(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if request.method == 'POST':
    if request.POST['is_audited']:
      project.is_audited = request.POST['is_audited']
      project.save()
      messages.success(request, 'Sucess auditing project')
      return redirect('/projects/allprojects')
  return render(request, 'projects/auditproject.html', {'error':'All fields are required.','project':project})


# def unaudited_audited_projects():
#   projects = Project.objects.all()
#   unaudited_projects = []
#   audited_projects = []
#   for project in projects:
#     if hasattr(project, "seventhquestion"):
#         answer_seventh_five = project.seventhquestion.seventh_five
#         if answer_seventh_five == "Yes":
#           audited_projects.append(project)
#         else:
#           unaudited_projects.append(project)
#   return unaudited_projects, audited_projects


def unaudited_audited_projects():
  projects = Project.objects.all()
  unaudited_projects = []
  audited_projects = []
  for project in projects:
    if project.is_audited == "Yes":
      audited_projects.append(project)
    else:
      unaudited_projects.append(project)
  # import pdb; pdb.set_trace()

  return unaudited_projects, audited_projects


def unaudited_dict():
  developers_all = CustomUser.objects.all().exclude(is_nhs=True)

  unaudited_by_solution = {}
  unaudited_by_application_group = {}
  sorted_unaudited_by_solution = {}
  sorted_unaudited_by_application_group = {}

  unaudited_projects, audited_projects = unaudited_audited_projects()
  for unaudited_project in unaudited_projects:
    if hasattr(unaudited_project, "initialquestion"):
      # unaudited_by_solution[unaudited_project] = unaudited_project.initialquestion.initial_one
      unaudited_by_application_group[unaudited_project] = unaudited_project.initialquestion.initial_two

  for developer in developers_all:
    # unaudited_by_solution[developer] = Project.objects.all().filter(developer=developer)
      unaudited_by_solution[developer] = [unaudited_project for unaudited_project in unaudited_projects if unaudited_project.developer == developer]

  unaudited_by_solution = { k:v for k, v in unaudited_by_solution.items() if v!=[] }

  # for k in sorted(unaudited_by_solution, key=lambda k: len(unaudited_by_solution[k]), reverse=True):
  #   sorted_unaudited_by_solution[k] = k.initialquestion.initial_one

  sorted_unaudited_by_solution = sorted(unaudited_by_solution.items(), key = lambda item : len(item[1]), reverse=True)

  for y in sorted(unaudited_by_application_group, key=lambda y: len(unaudited_by_application_group[y]), reverse=True):
    sorted_unaudited_by_application_group[y] = y.initialquestion.initial_two

  # import pdb; pdb.set_trace()

  return sorted_unaudited_by_solution, sorted_unaudited_by_application_group

def audited_dict():
  developers_all = CustomUser.objects.all().exclude(is_nhs=True)

  audited_by_solution = {}
  audited_by_application_group = {}
  sorted_audited_by_solution = {}
  sorted_audited_by_application_group = {}

  unaudited_projects, audited_projects = unaudited_audited_projects()
  for audited_project in audited_projects:
    if hasattr(audited_project, "initialquestion"):
      # audited_by_solution[audited_project] = audited_project.initialquestion.initial_one
      audited_by_application_group[audited_project] = audited_project.initialquestion.initial_two

  for developer in developers_all:
    # unaudited_by_solution[developer] = Project.objects.all().filter(developer=developer)
      audited_by_solution[developer] = [audited_project for audited_project in audited_projects if audited_project.developer == developer]

  audited_by_solution = { k:v for k, v in audited_by_solution.items() if v!=[] }

  sorted_audited_by_solution = sorted(audited_by_solution.items(), key = lambda item : len(item[1]), reverse=True)


  # import pdb; pdb.set_trace()


  # for k in sorted(audited_by_solution, key=lambda k: len(audited_by_solution[k]), reverse=True):
  #   sorted_audited_by_solution[k] = k.initialquestion.initial_one

  for y in sorted(audited_by_application_group, key=lambda y: len(audited_by_application_group[y]), reverse=True):
    sorted_audited_by_application_group[y] = y.initialquestion.initial_two



  return sorted_audited_by_solution, sorted_audited_by_application_group


@login_required
def nhsstatistics(request):
  projects = Project.objects.all()
  sorted_unaudited_by_solution, sorted_unaudited_by_application_group = unaudited_dict()
  sorted_audited_by_solution, sorted_audited_by_application_group = audited_dict()
  # import pdb; pdb.set_trace()

  return render(request, 'projects/nhsstatistics.html', {
    'projects': projects,
    'sorted_unaudited_by_solution': sorted_unaudited_by_solution,
    'sorted_unaudited_by_application_group': sorted_unaudited_by_application_group,
    'sorted_audited_by_solution': sorted_audited_by_solution,
    'sorted_audited_by_application_group': sorted_audited_by_application_group,
    })




def project_first_questions(request, project_id):
  answered_first = 0
  not_answered_first = 0
  try:
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects.all()
    first_one =  project.firstquestion.first_one
    first_two =  project.firstquestion.first_two
    first_three =  project.firstquestion.first_three
    first_four =  project.firstquestion.first_four
    first_five =  project.firstquestion.first_five
    first_six =  project.firstquestion.first_six
    # first_seven =  project.firstquestion.first_seven
    first_questions = [first_one, first_two, first_three, first_four, first_five, first_six]
  except:
    first_questions = []
  if len(first_questions)>0:
    for answer in first_questions:
      if answer:
        answered_first = answered_first + 1
      else:
        not_answered_first = not_answered_first + 1
  else:
    percentage_answered_first = 0
    percentage_not_answered_first = 1
    return percentage_answered_first, percentage_not_answered_first

  percentage_answered_first = round(float(answered_first / len(first_questions)), 2)
  percentage_not_answered_first = round(float(not_answered_first / len(first_questions)),2)
  return percentage_answered_first, percentage_not_answered_first

def other_first_questions(request, project_id):
  other_first_questions = (Project.objects.all().exclude(id=project_id).count())*6

  my_count_first = 0
  other_projects = Project.objects.all().exclude(id=project_id)

  for other_project in other_projects:
    try:
      other_first_one =  other_project.firstquestion.first_one
    except:
      my_count_first = my_count_first + 1
  for other_project in other_projects:
    try:
      other_first_two =  other_project.firstquestion.first_two
    except:
      my_count_first = my_count_first + 1
  for other_project in other_projects:
    try:
      other_first_three =  other_project.firstquestion.first_three
    except:
      my_count_first = my_count_first + 1
  for other_project in other_projects:
    try:
      other_first_four =  other_project.firstquestion.first_four
    except:
      my_count_first = my_count_first + 1
  for other_project in other_projects:
    try:
      other_first_five =  other_project.firstquestion.first_five
    except:
      my_count_first = my_count_first + 1
  for other_project in other_projects:
    try:
      other_first_six =  other_project.firstquestion.first_six
    except:
      my_count_first = my_count_first + 1
  # for other_project in other_projects:
  #   try:
  #     other_first_seven =  other_project.firstquestion.first_seven
  #   except:
  #     my_count_first = my_count_first + 1

  if other_first_questions == 0:
    other_percentage_answered_first = 0
    other_percentage_not_answered_first = 0
  else:
    other_percentage_answered_first = round(float((other_first_questions - my_count_first) / other_first_questions), 2)
    other_percentage_not_answered_first = round(float(my_count_first / other_first_questions), 2)
  # import pdb; pdb.set_trace()

  return other_percentage_answered_first, other_percentage_answered_first


def project_second_questions(request, project_id):
  answered_second = 0
  not_answered_second =0

  project = get_object_or_404(Project, pk=project_id)
  projects = Project.objects.all()

  try:
    second_one =  project.secondquestion.second_one
    second_two =  project.secondquestion.second_two
    second_three =  project.secondquestion.second_three
    second_four =  project.secondquestion.second_four
    second_five =  project.secondquestion.second_five
    second_six =  project.secondquestion.second_six
    second_seven =  project.secondquestion.second_seven
    second_eight = project.secondquestion.second_eight
    second_nine = project.secondquestion.second_nine
    second_questions = [second_one, second_two, second_three, second_four, second_five, second_six, second_seven, second_eight, second_nine]
  except:
    second_questions = []

  if len(second_questions)>0:
    for answer in second_questions:
      if answer:
        answered_second = answered_second + 1
      else:
        not_answered_second = not_answered_second + 1
  else:
    percentage_answered_second = 0
    percentage_not_answered_second = 1
    return percentage_answered_second, percentage_not_answered_second

  percentage_answered_second = round(float(answered_second / len(second_questions)), 2)
  percentage_not_answered_second = round(float(not_answered_second / len(second_questions)),2)
  return percentage_answered_second, percentage_not_answered_second

def other_second_questions(request, project_id):
  other_second_questions = (Project.objects.all().exclude(id=project_id).count())*9
  my_count_second = 0
  other_projects = Project.objects.all().exclude(id=project_id)



  for other_project in other_projects:
    try:
      other_second_one =  other_project.secondquestion.second_one
    except:
      my_count_second = my_count_second + 1
  for other_project in other_projects:
    try:
      other_second_two =  other_project.secondquestion.second_two
    except:
      my_count_second = my_count_second + 1
  for other_project in other_projects:
    try:
      other_second_three =  other_project.secondquestion.second_three
    except:
      my_count_second = my_count_second + 1
  for other_project in other_projects:
    try:
      other_second_four =  other_project.secondquestion.second_four
    except:
      my_count_second = my_count_second + 1
  for other_project in other_projects:
    try:
      other_second_five =  other_project.secondquestion.second_five
    except:
      my_count_second = my_count_second + 1
  for other_project in other_projects:
    try:
      other_second_six =  other_project.secondquestion.second_six
    except:
      my_count_second = my_count_second + 1
  for other_project in other_projects:
    try:
      other_second_seven =  other_project.secondquestion.second_seven
    except:
      my_count_second = my_count_second + 1
  for other_project in other_projects:
    try:
      other_second_eight =  other_project.secondquestion.second_eight
    except:
      my_count_second = my_count_second + 1
  for other_project in other_projects:
    try:
      other_second_nine =  other_project.secondquestion.second_nine
    except:
      my_count_second = my_count_second + 1

  if other_second_questions == 0:
    other_percentage_answered_second = 0
    other_percentage_not_answered_second = 0
  else:
    other_percentage_answered_second = round(float((other_second_questions - my_count_second) / other_second_questions), 2)
    other_percentage_not_answered_second = round(float(my_count_second / other_second_questions), 2)
  return other_percentage_answered_second, other_percentage_answered_second


def project_third_questions(request, project_id):
  answered_third = 0
  not_answered_third =0

  project = get_object_or_404(Project, pk=project_id)
  projects = Project.objects.all()

  try:
    third_one =  project.thirdquestion.third_one
    third_two =  project.thirdquestion.third_two
    third_three =  project.thirdquestion.third_three
    third_four =  project.thirdquestion.third_four
    third_five =  project.thirdquestion.third_five
    third_six =  project.thirdquestion.third_six
    third_seven =  project.thirdquestion.third_seven
    third_eight = project.thirdquestion.third_eight
    third_nine = project.thirdquestion.third_nine
    third_questions = [third_one, third_two, third_three, third_four, third_five, third_six, third_seven, third_eight, third_nine]
  except:
    third_questions = []

  if len(third_questions)>0:
    for answer in third_questions:
      if answer:
        answered_third = answered_third + 1
      else:
        not_answered_third = not_answered_third + 1

    percentage_answered_third = round(float(answered_third / len(third_questions)), 2)
    percentage_not_answered_third = round(float(not_answered_third / len(third_questions)),2)
    return percentage_answered_third, percentage_not_answered_third
  else:
    percentage_answered_third = 0
    percentage_not_answered_third = 1
    return percentage_answered_third, percentage_not_answered_third


def other_third_questions(request, project_id):
  other_third_questions = (Project.objects.all().exclude(id=project_id).count())*9
  my_count_third = 0
  other_projects = Project.objects.all().exclude(id=project_id)

  for other_project in other_projects:
    try:
      other_third_one =  other_project.thirdquestion.third_one
    except:
      my_count_third = my_count_third + 1
  for other_project in other_projects:
    try:
      other_third_two =  other_project.thirdquestion.third_two
    except:
      my_count_third = my_count_third + 1
  for other_project in other_projects:
    try:
      other_third_three =  other_project.thirdquestion.third_three
    except:
      my_count_third = my_count_third + 1
  for other_project in other_projects:
    try:
      other_third_four =  other_project.thirdquestion.third_four
    except:
      my_count_third = my_count_third + 1
  for other_project in other_projects:
    try:
      other_third_five =  other_project.thirdquestion.third_five
    except:
      my_count_third = my_count_third + 1
  for other_project in other_projects:
    try:
      other_third_six =  other_project.thirdquestion.third_six
    except:
      my_count_third = my_count_third + 1
  for other_project in other_projects:
    try:
      other_third_seven =  other_project.thirdquestion.third_seven
    except:
      my_count_third = my_count_third + 1
  for other_project in other_projects:
    try:
      other_third_eight =  other_project.thirdquestion.third_eight
    except:
      my_count_third = my_count_third + 1
  for other_project in other_projects:
    try:
      other_third_nine =  other_project.thirdquestion.third_nine
    except:
      my_count_third = my_count_third + 1

  if other_third_questions == 0:
    other_percentage_answered_third = 0
    other_percentage_not_answered_third = 0
  else:
    other_percentage_answered_third = round(float((other_third_questions - my_count_third) / other_third_questions), 2)
    other_percentage_not_answered_third = round(float(my_count_third / other_third_questions), 2)
  return other_percentage_answered_third, other_percentage_answered_third



def project_fourth_questions(request, project_id):
  answered_fourth = 0
  not_answered_fourth =0
  try:
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects.all()
    fourth_one =  project.fourthquestion.fourth_one
    fourth_two =  project.fourthquestion.fourth_two
    fourth_three =  project.fourthquestion.fourth_three
    fourth_four =  project.fourthquestion.fourth_four
    fourth_five =  project.fourthquestion.fourth_five
    fourth_six =  project.fourthquestion.fourth_six
    fourth_seven =  project.fourthquestion.fourth_seven
    fourth_eight = project.fourthquestion.fourth_eight
    fourth_nine = project.fourthquestion.fourth_nine
    fourth_questions = [fourth_one, fourth_two, fourth_three, fourth_four, fourth_five, fourth_six, fourth_seven, fourth_eight, fourth_nine]
  except:
    fourth_questions = []
  if len(fourth_questions)>0:
    for answer in fourth_questions:
      if answer and answer != "There-is-no-file":
        answered_fourth = answered_fourth + 1
      else:
        not_answered_fourth = not_answered_fourth + 1
    # import pdb; pdb.set_trace()

  else:
    percentage_answered_fourth = 0
    percentage_not_answered_fourth = 1

    return percentage_answered_fourth, percentage_not_answered_fourth

  percentage_answered_fourth = round(float(answered_fourth / len(fourth_questions)), 2)
  percentage_not_answered_fourth = round(float(not_answered_fourth / len(fourth_questions)),2)
  return percentage_answered_fourth, percentage_not_answered_fourth

def other_fourth_questions(request, project_id):
  other_fourth_questions = (Project.objects.all().exclude(id=project_id).count())*9
  my_count_fourth = 0
  other_projects = Project.objects.all().exclude(id=project_id)

  for other_project in other_projects:
    try:
      other_fourth_one =  other_project.fourthquestion.fourth_one
    except:
      my_count_fourth = my_count_fourth + 1
  for other_project in other_projects:
    try:
      other_fourth_two =  other_project.fourthquestion.fourth_two
    except:
      my_count_fourth = my_count_fourth + 1
  for other_project in other_projects:
    try:
      other_fourth_three =  other_project.fourthquestion.fourth_three
    except:
      my_count_fourth = my_count_fourth + 1
  for other_project in other_projects:
    try:
      other_fourth_four =  other_project.fourthquestion.fourth_four
    except:
      my_count_fourth = my_count_fourth + 1
  for other_project in other_projects:
    try:
      other_fourth_five =  other_project.fourthquestion.fourth_five
    except:
      my_count_fourth = my_count_fourth + 1
  for other_project in other_projects:
    try:
      other_fourth_six =  other_project.fourthquestion.fourth_six
    except:
      my_count_fourth = my_count_fourth + 1
  for other_project in other_projects:
    try:
      other_fourth_seven =  other_project.fourthquestion.fourth_seven
    except:
      my_count_fourth = my_count_fourth + 1
  for other_project in other_projects:
    try:
      other_fourth_eight =  other_project.fourthquestion.fourth_eight
    except:
      my_count_fourth = my_count_fourth + 1
  for other_project in other_projects:
    try:
      other_fourth_nine =  other_project.fourthquestion.fourth_nine
    except:
      my_count_fourth = my_count_fourth + 1

  if other_fourth_questions == 0:
    other_percentage_answered_fourth = 0
    other_percentage_not_answered_fourth = 0
  else:
    other_percentage_answered_fourth = round(float((other_fourth_questions - my_count_fourth) / other_fourth_questions), 2)
    other_percentage_not_answered_fourth = round(float(my_count_fourth / other_fourth_questions), 2)
  return other_percentage_answered_fourth, other_percentage_answered_fourth


def project_fifth_questions(request, project_id):
  answered_fifth = 0
  not_answered_fifth =0

  try:
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects.all()
    fifth_one =  project.fifthquestion.fifth_one
    fifth_two =  project.fifthquestion.fifth_two
    fifth_three =  project.fifthquestion.fifth_three
    fifth_four =  project.fifthquestion.fifth_four
    fifth_five =  project.fifthquestion.fifth_five
    fifth_six =  project.fifthquestion.fifth_six
    fifth_questions = [fifth_one, fifth_two, fifth_three, fifth_four, fifth_five, fifth_six]
  except:
    fifth_questions = []
  if len(fifth_questions)>0:
    for answer in fifth_questions:
      if answer:
        answered_fifth = answered_fifth + 1
      else:
        not_answered_fifth = not_answered_fifth + 1

  else:
    percentage_answered_fifth = 0
    percentage_not_answered_fifth = 1
    return percentage_answered_fifth, percentage_not_answered_fifth

  percentage_answered_fifth = round(float(answered_fifth / len(fifth_questions)), 2)
  percentage_not_answered_fifth = round(float(not_answered_fifth / len(fifth_questions)),2)
  return percentage_answered_fifth, percentage_not_answered_fifth


def other_fifth_questions(request, project_id):
  other_fifth_questions = (Project.objects.all().exclude(id=project_id).count())*6
  my_count_fifth = 0
  other_projects = Project.objects.all().exclude(id=project_id)

  for other_project in other_projects:
    try:
      other_fifth_one =  other_project.fifthquestion.fifth_one
    except:
      my_count_fifth = my_count_fifth + 1
  for other_project in other_projects:
    try:
      other_fifth_two =  other_project.fifthquestion.fifth_two
    except:
      my_count_fifth = my_count_fifth + 1
  for other_project in other_projects:
    try:
      other_fifth_three =  other_project.fifthquestion.fifth_three
    except:
      my_count_fifth = my_count_fifth + 1
  for other_project in other_projects:
    try:
      other_fifth_four =  other_project.fifthquestion.fifth_four
    except:
      my_count_fifth = my_count_fifth + 1
  for other_project in other_projects:
    try:
      other_fifth_five =  other_project.fifthquestion.fifth_five
    except:
      my_count_fifth = my_count_fifth + 1
  for other_project in other_projects:
    try:
      other_fifth_six =  other_project.fifthquestion.fifth_six
    except:
      my_count_fifth = my_count_fifth + 1

  if other_fifth_questions == 0:
    other_percentage_answered_fifth = 0
    other_percentage_not_answered_fifth = 0
  else:
    other_percentage_answered_fifth = round(float((other_fifth_questions - my_count_fifth) / other_fifth_questions), 2)
    other_percentage_not_answered_fifth = round(float(my_count_fifth / other_fifth_questions), 2)
  return other_percentage_answered_fifth, other_percentage_answered_fifth

def project_sixth_questions(request, project_id):
  answered_sixth = 0
  not_answered_sixth =0
  try:
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects.all()
    sixth_one =  project.sixthquestion.sixth_one
    sixth_two =  project.sixthquestion.sixth_two
    sixth_three =  project.sixthquestion.sixth_three
    sixth_four =  project.sixthquestion.sixth_four
    sixth_five =  project.sixthquestion.sixth_five
    sixth_six =  project.sixthquestion.sixth_six
    sixth_seven =  project.sixthquestion.sixth_seven
    sixth_eight = project.sixthquestion.sixth_eight
    sixth_nine = project.sixthquestion.sixth_nine
    sixth_ten = project.sixthquestion.sixth_ten
    sixth_eleven = project.sixthquestion.sixth_eleven
    sixth_twelve = project.sixth_twelve.sixth_twelve
    sixth_questions = [sixth_one, sixth_two, sixth_three, sixth_four, sixth_five, sixth_six, sixth_seven, sixth_eight, sixth_nine, sixth_ten, sixth_eleven, sixth_twelve]
  except:
    sixth_questions = []
  if len(sixth_questions)>0:
    for answer in sixth_questions:
      if answer:
        answered_sixth = answered_sixth + 1
      else:
        not_answered_sixth = not_answered_sixth + 1
  else:
    percentage_answered_sixth = 0
    percentage_not_answered_sixth = 1
    return percentage_answered_sixth, percentage_not_answered_sixth

  percentage_answered_sixth = round(float(answered_sixth / len(sixth_questions)), 2)
  percentage_not_answered_sixth = round(float(not_answered_sixth / len(sixth_questions)),2)
  return percentage_answered_sixth, percentage_not_answered_sixth

def other_sixth_questions(request, project_id):
  other_sixth_questions = (Project.objects.all().exclude(id=project_id).count())*12
  my_count_sixth = 0
  other_projects = Project.objects.all().exclude(id=project_id)

  for other_project in other_projects:
    try:
      other_sixth_one =  other_project.sixthquestion.sixth_one
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_two =  other_project.sixthquestion.sixth_two
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_three =  other_project.sixthquestion.sixth_three
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_four =  other_project.sixthquestion.sixth_four
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_five =  other_project.sixthquestion.sixth_five
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_six =  other_project.sixthquestion.sixth_six
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_seven =  other_project.sixthquestion.sixth_seven
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_eight =  other_project.sixthquestion.sixth_eight
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_nine =  other_project.sixthquestion.sixth_nine
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_ten =  other_project.sixthquestion.sixth_ten
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_eleven =  other_project.sixthquestion.sixth_eleven
    except:
      my_count_sixth = my_count_sixth + 1
  for other_project in other_projects:
    try:
      other_sixth_twelve =  other_project.sixthquestion.sixth_twelve
    except:
      my_count_sixth = my_count_sixth + 1
  if other_sixth_questions == 0:
    other_percentage_answered_sixth = 0
    other_percentage_not_answered_sixth = 0
  else:
    other_percentage_answered_sixth = round(float((other_sixth_questions - my_count_sixth) / other_sixth_questions), 2)
    other_percentage_not_answered_sixth = round(float(my_count_sixth / other_sixth_questions), 2)
  return other_percentage_answered_sixth, other_percentage_answered_sixth


def project_seventh_questions(request, project_id):
  answered_seventh = 0
  not_answered_seventh =0
  try:
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects.all()
    seventh_one =  project.seventhquestion.seventh_one
    seventh_two =  project.seventhquestion.seventh_two
    seventh_three =  project.seventhquestion.seventh_three
    seventh_four =  project.seventhquestion.seventh_four
    seventh_five =  project.seventhquestion.seventh_five
    seventh_six =  project.seventhquestion.seventh_six
    seventh_seven =  project.seventhquestion.seventh_seven
    seventh_eight = project.seventhquestion.seventh_eight
    seventh_nine = project.seventhquestion.seventh_nine

    seventh_questions = [seventh_one, seventh_two, seventh_three, seventh_four, seventh_five, seventh_six, seventh_seven, seventh_eight, seventh_nine]
  except:
    seventh_questions = []
  if len(seventh_questions)>0:
    for answer in seventh_questions:
      if answer:
        answered_seventh = answered_seventh + 1
      else:
        not_answered_seventh = not_answered_seventh + 1
  else:
    percentage_answered_seventh = 0
    percentage_not_answered_seventh = 1
    return percentage_answered_seventh, percentage_not_answered_seventh

  percentage_answered_seventh = round(float(answered_seventh / len(seventh_questions)), 2)
  percentage_not_answered_seventh = round(float(not_answered_seventh / len(seventh_questions)),2)
  return percentage_answered_seventh, percentage_not_answered_seventh


def other_seventh_questions(request, project_id):
  other_seventh_questions = (Project.objects.all().exclude(id=project_id).count())*9
  my_count_seventh = 0
  other_projects = Project.objects.all().exclude(id=project_id)

  for other_project in other_projects:
    try:
      other_seventh_one =  other_project.seventhquestion.seventh_one
    except:
      my_count_seventh = my_count_seventh + 1
  for other_project in other_projects:
    try:
      other_seventh_two =  other_project.seventhquestion.seventh_two
    except:
      my_count_seventh = my_count_seventh + 1
  for other_project in other_projects:
    try:
      other_seventh_three =  other_project.seventhquestion.seventh_three
    except:
      my_count_seventh = my_count_seventh + 1
  for other_project in other_projects:
    try:
      other_seventh_four =  other_project.seventhquestion.seventh_four
    except:
      my_count_seventh = my_count_seventh + 1
  for other_project in other_projects:
    try:
      other_seventh_five =  other_project.seventhquestion.seventh_five
    except:
      my_count_seventh = my_count_seventh + 1
  for other_project in other_projects:
    try:
      other_seventh_six =  other_project.seventhquestion.seventh_six
    except:
      my_count_seventh = my_count_seventh + 1
  for other_project in other_projects:
    try:
      other_seventh_seven =  other_project.seventhquestion.seventh_seven
    except:
      my_count_seventh = my_count_seventh + 1
  for other_project in other_projects:
    try:
      other_seventh_eight =  other_project.seventhquestion.seventh_eight
    except:
      my_count_seventh = my_count_seventh + 1
  for other_project in other_projects:
    try:
      other_seventh_nine =  other_project.seventhquestion.seventh_nine
    except:
      my_count_seventh = my_count_seventh + 1
  if other_seventh_questions == 0:
    other_percentage_answered_seventh = 0
    other_percentage_not_answered_seventh = 0
  else:
    other_percentage_answered_seventh = round(float((other_seventh_questions - my_count_seventh) / other_seventh_questions), 2)
    other_percentage_not_answered_seventh = round(float(my_count_seventh / other_seventh_questions), 2)
  return other_percentage_answered_seventh, other_percentage_answered_seventh


def project_eighth_questions(request, project_id):
  answered_eighth = 0
  not_answered_eighth =0
  try:
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects.all()
    eighth_one =  project.eighthquestion.eighth_one
    eighth_two =  project.eighthquestion.eighth_two
    eighth_three =  project.eighthquestion.eighth_three
    eighth_four =  project.eighthquestion.eighth_four
    eighth_five =  project.eighthquestion.eighth_five
    eighth_six =  project.eighthquestion.eighth_six
    eighth_seven =  project.eighthquestion.eighth_seven
    eighth_eight = project.eighthquestion.eighth_eight
    eighth_nine = project.eighthquestion.eighth_nine
    eighth_ten = project.eighthquestion.eighth_ten
    eighth_eleven = project.eighthquestion.eighth_eleven
    eighth_twelve = project.eighth_twelve.eighth_twelve
    eighth_questions = [eighth_one, eighth_two, eighth_three, eighth_four, eighth_five, eighth_six, eighth_seven, eighth_eight, eighth_nine, eighth_ten, eighth_eleven, eighth_twelve]
  except:
    eight_questions = []
  if len(eight_questions)>0:
    for answer in eight_questions:
      if answer:
        answered_eight = answered_eight + 1
      else:
        not_answered_eight = not_answered_eight + 1
  else:
    percentage_answered_eight = 0
    percentage_not_answered_eight = 1
    return percentage_answered_eight, percentage_not_answered_eight

  percentage_answered_eight = round(float(answered_eight / len(eight_questions)), 2)
  percentage_not_answered_eight = round(float(not_answered_eight / len(eight_questions)),2)
  return percentage_answered_eight, percentage_not_answered_eight


def other_eighth_questions(request, project_id):
  other_eighth_questions = (Project.objects.all().exclude(id=project_id).count())*12
  my_count_eighth = 0
  other_projects = Project.objects.all().exclude(id=project_id)

  for other_project in other_projects:
    try:
      other_eighth_one =  other_project.eighthquestion.eighth_one
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_two =  other_project.eighthquestion.eighth_two
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_three =  other_project.eighthquestion.eighth_three
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_four =  other_project.eighthquestion.eighth_four
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_five =  other_project.eighthquestion.eighth_five
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_six =  other_project.eighthquestion.eighth_six
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_seven =  other_project.eighthquestion.eighth_seven
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_eight =  other_project.eighthquestion.eighth_eight
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_nine =  other_project.eighthquestion.eighth_nine
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_ten =  other_project.eighthquestion.eighth_ten
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_eleven =  other_project.eighthquestion.eighth_eleven
    except:
      my_count_eighth = my_count_eighth + 1
  for other_project in other_projects:
    try:
      other_eighth_twelve =  other_project.eighthquestion.eighth_twelve
    except:
      my_count_eighth = my_count_eighth + 1
  if other_eighth_questions == 0:
    other_percentage_answered_eighth = 0
    other_percentage_not_answered_eighth = 0
  else:
    other_percentage_answered_eighth = round(float((other_eighth_questions - my_count_eighth) / other_eighth_questions), 2)
    other_percentage_not_answered_eighth = round(float(my_count_eighth / other_eighth_questions), 2)
  return other_percentage_answered_eighth, other_percentage_answered_eighth

def project_ninth_questions(request, project_id):
  answered_ninth = 0
  not_answered_ninth =0
  try:
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects.all()
    ninth_one =  project.ninthquestion.ninth_one
    ninth_two =  project.ninthquestion.ninth_two
    ninth_three =  project.ninthquestion.ninth_three
    ninth_four =  project.ninthquestion.ninth_four
    ninth_five =  project.ninthquestion.ninth_five
    ninth_six =  project.ninthquestion.ninth_six
    ninth_seven =  project.ninthquestion.ninth_seven

    ninth_questions = [ninth_one, ninth_two, ninth_three, ninth_four, ninth_five, ninth_six, ninth_seven]
  except:
    ninth_questions = []
  if len(ninth_questions)>0:
    for answer in ninth_questions:
      if answer:
        answered_ninth = answered_ninth + 1
      else:
        not_answered_ninth = not_answered_ninth + 1

  else:
    percentage_answered_ninth = 0
    percentage_not_answered_ninth = 1
    return percentage_answered_ninth, percentage_not_answered_ninth
  percentage_answered_ninth = round(float(answered_ninth / len(ninth_questions)), 2)
  percentage_not_answered_ninth = round(float(not_answered_ninth / len(ninth_questions)),2)

  return percentage_answered_ninth, percentage_not_answered_ninth

def other_ninth_questions(request, project_id):
  other_ninth_questions = (Project.objects.all().exclude(id=project_id).count())*7
  my_count_ninth = 0
  other_projects = Project.objects.all().exclude(id=project_id)

  for other_project in other_projects:
    try:
      other_ninth_one =  other_project.ninthquestion.ninth_one
    except:
      my_count_ninth = my_count_ninth + 1
  for other_project in other_projects:
    try:
      other_ninth_two =  other_project.ninthquestion.ninth_two
    except:
      my_count_ninth = my_count_ninth + 1
  for other_project in other_projects:
    try:
      other_ninth_three =  other_project.ninthquestion.ninth_three
    except:
      my_count_ninth = my_count_ninth + 1
  for other_project in other_projects:
    try:
      other_ninth_four =  other_project.ninthquestion.ninth_four
    except:
      my_count_ninth = my_count_ninth + 1
  for other_project in other_projects:
    try:
      other_ninth_five =  other_project.ninthquestion.ninth_five
    except:
      my_count_ninth = my_count_ninth + 1
  for other_project in other_projects:
    try:
      other_ninth_six =  other_project.ninthquestion.ninth_six
    except:
      my_count_ninth = my_count_ninth + 1
  for other_project in other_projects:
    try:
      other_ninth_seven =  other_project.ninthquestion.ninth_seven
    except:
      my_count_ninth = my_count_ninth + 1

  if other_ninth_questions == 0:
    other_percentage_answered_ninth = 0
    other_percentage_not_answered_ninth = 0

  else:
    other_percentage_answered_ninth = round(float((other_ninth_questions - my_count_ninth) / other_ninth_questions), 2)
    other_percentage_not_answered_ninth = round(float(my_count_ninth / other_ninth_questions), 2)
  return other_percentage_answered_ninth, other_percentage_answered_ninth

def project_tenth_questions(request, project_id):
  answered_tenth = 0
  not_answered_tenth = 0
  try:
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects.all()
    tenth_one =  project.tenthquestion.tenth_one
    tenth_two =  project.tenthquestion.tenth_two
    tenth_three =  project.tenthquestion.tenth_three
    tenth_four =  project.tenthquestion.tenth_four
    tenth_five =  project.tenthquestion.tenth_five
    tenth_six =  project.tenthquestion.tenth_six
    tenth_seven =  project.tenthquestion.tenth_seven
    tenth_eight = project.tenthquestion.tenth_eight
    tenth_nine = project.tenthquestion.tenth_nine
    tenth_ten = project.tenthquestion.tenth_ten
    tenth_eleven = project.tenthquestion.tenth_eleven
    tenth_questions = [tenth_one, tenth_two, tenth_three, tenth_four, tenth_five, tenth_six, tenth_seven, tenth_eight, tenth_nine, tenth_ten, tenth_eleven]
  except:
    tenth_questions = []
  if len(tenth_questions)>0:
    for answer in tenth_questions:
      if answer and answer!= "There-is-no-file":
        answered_tenth = answered_tenth + 1
      else:
        not_answered_tenth = not_answered_tenth + 1
    # import pdb; pdb.set_trace()

  else:
    percentage_answered_tenth = 0
    percentage_not_answered_tenth = 1
    return percentage_answered_tenth, percentage_not_answered_tenth

  percentage_answered_tenth = round(float(answered_tenth / len(tenth_questions)), 2)
  percentage_not_answered_tenth = round(float(not_answered_tenth / len(tenth_questions)),2)
  return percentage_answered_tenth, percentage_not_answered_tenth

def other_tenth_questions(request, project_id):
  other_tenth_questions = (Project.objects.all().exclude(id=project_id).count())*11
  my_count_tenth = 0
  other_projects = Project.objects.all().exclude(id=project_id)

  for other_project in other_projects:
    try:
      other_tenth_one =  other_project.tenthquestion.tenth_one
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_two =  other_project.tenthquestion.tenth_two
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_three =  other_project.tenthquestion.tenth_three
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_four =  other_project.tenthquestion.tenth_four
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_five =  other_project.tenthquestion.tenth_five
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_six =  other_project.tenthquestion.tenth_six
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_seven =  other_project.tenthquestion.tenth_seven
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_eight =  other_project.tenthquestion.tenth_eight
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_nine =  other_project.tenthquestion.tenth_nine
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_ten =  other_project.tenthquestion.tenth_ten
    except:
      my_count_tenth = my_count_tenth + 1
  for other_project in other_projects:
    try:
      other_tenth_eleven = other_project.tenthquestion.tenth_eleven
    except:
      my_count_tenth = my_count_tenth + 1
  if other_tenth_questions == 0:
    other_percentage_answered_tenth = 0
    other_percentage_not_answered_tenth = 0
  else:
    other_percentage_answered_tenth = round(float((other_tenth_questions - my_count_tenth) / other_tenth_questions), 2)
    other_percentage_not_answered_tenth = round(float(my_count_tenth / other_tenth_questions), 2)
  return other_percentage_answered_tenth, other_percentage_answered_tenth



@login_required
def statistics(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  projects = Project.objects.all()

  percentage_answered_first, percentage_not_answered_first = project_first_questions(request, project_id)
  percentage_answered_second, percentage_not_answered_second = project_second_questions(request, project_id)
  percentage_answered_third, percentage_not_answered_third = project_third_questions(request, project_id)
  percentage_answered_fourth, percentage_not_answered_fourth = project_fourth_questions(request, project_id)
  percentage_answered_fifth, percentage_not_answered_fifth = project_fifth_questions(request, project_id)
  percentage_answered_sixth, percentage_not_answered_sixth = project_sixth_questions(request, project_id)
  percentage_answered_seventh, percentage_not_answered_seventh = project_seventh_questions(request, project_id)
  percentage_answered_eighth, percentage_not_answered_eighth = project_eighth_questions(request, project_id)
  percentage_answered_ninth, percentage_not_answered_ninth = project_ninth_questions(request, project_id)
  percentage_answered_tenth, percentage_not_answered_tenth = project_tenth_questions(request, project_id)


  other_percentage_answered_first, other_percentage_not_answered_first = other_first_questions(request, project_id)
  other_percentage_answered_second, other_percentage_not_answered_second = other_second_questions(request, project_id)
  other_percentage_answered_third, other_percentage_not_answered_third = other_third_questions(request, project_id)
  other_percentage_answered_fourth, other_percentage_not_answered_fourth = other_fourth_questions(request, project_id)
  other_percentage_answered_fifth, other_percentage_not_answered_fifth = other_fifth_questions(request, project_id)
  other_percentage_answered_sixth, other_percentage_not_answered_sixth = other_sixth_questions(request, project_id)
  other_percentage_answered_seventh, other_percentage_not_answered_seventh = other_seventh_questions(request, project_id)
  other_percentage_answered_eighth, other_percentage_not_answered_eighth = other_eighth_questions(request, project_id)
  other_percentage_answered_ninth, other_percentage_not_answered_ninth = other_ninth_questions(request, project_id)
  other_percentage_answered_tenth, other_percentage_not_answered_tenth = other_tenth_questions(request, project_id)


  categories = ['1-User centred design','2-Maintenance of the value proposition','3-Data use',
                '4-Data protection', '5-Openness', '6-Transparency in data science', '7-Explainability and ethical use', '8-Risk and rewards', '9-Data solutions', '10-Commercial issues']

  fig = go.Figure()
  fig.add_trace(go.Scatterpolar(
        r=[percentage_answered_first, percentage_answered_second, percentage_answered_third, percentage_answered_fourth, percentage_answered_fifth, percentage_answered_sixth, percentage_answered_seventh, percentage_answered_eighth, percentage_answered_ninth, percentage_answered_tenth],
        theta=categories,
        fill='toself',
        name='Your project'
  ))
  fig.add_trace(go.Scatterpolar(
        r=[other_percentage_answered_first, other_percentage_answered_second, other_percentage_answered_third, other_percentage_answered_fourth, other_percentage_answered_fifth, other_percentage_answered_sixth, other_percentage_answered_seventh, other_percentage_answered_eighth, other_percentage_answered_ninth, other_percentage_answered_tenth],
        theta=categories,
        fill='toself',
        name='Other projects',
  ))
  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True,
        range = [0, 1],

      )),
    showlegend=True
  )
  fig.update_layout(
      title=go.layout.Title(
          text="<b>This graph plots the percentage (0 to 1) of how many questions you answered (blue) vs the others (red)</b>",
          font=dict(size=10),
          xref="paper",
          x=0
      ),
    )


  fig2 = go.Figure()
  fig2.add_trace(go.Bar(
      x=categories,
      y=[percentage_answered_first, percentage_answered_second, percentage_answered_third, percentage_answered_fourth, percentage_answered_fifth, percentage_answered_sixth, percentage_answered_seventh, percentage_answered_eighth, percentage_answered_ninth, percentage_answered_tenth],
      name='Your project',
      marker_color='#A5A9F7'

  ))
  fig2.add_trace(go.Bar(
      x=categories,
      y=[other_percentage_answered_first, other_percentage_answered_second, other_percentage_answered_third, other_percentage_answered_fourth, other_percentage_answered_fifth, other_percentage_answered_sixth, other_percentage_answered_seventh, other_percentage_answered_eighth, other_percentage_answered_ninth, other_percentage_answered_tenth],
      name='Other projects',
      marker_color='#E89C8C'
  ))
  fig2.update_layout(
      title=go.layout.Title(
          text="<b>This graph chart plots the percentage (0 to 1) of how many questions you answered (blue) vs the others (red)<b>",
          font=dict(size=10),
          xref="paper",
          x=0
      ),
    yaxis=dict(
        range=[0, 1]
    )
    )



  radar_graph_div = plot(fig, output_type='div', include_plotlyjs=False)
  bar_chart_div = plot(fig2, output_type='div', include_plotlyjs=False)



  return render(request, 'projects/statistics.html', {
    'project':project,
    'projects': projects,
    'radar_graph_div': radar_graph_div,
    'bar_chart_div': bar_chart_div,
      'percentage_answered_first': percentage_answered_first,
    'percentage_not_answered_first': percentage_not_answered_first,
      'percentage_answered_second': percentage_answered_second,
    'percentage_not_answered_second': percentage_not_answered_second,
      'percentage_answered_third': percentage_answered_third,
    'percentage_not_answered_third': percentage_not_answered_third,
      'percentage_answered_fourth': percentage_answered_fourth,
    'percentage_not_answered_fourth': percentage_not_answered_fourth,
      'percentage_answered_fifth': percentage_answered_fifth,
    'percentage_not_answered_fifth': percentage_not_answered_fifth,
        'percentage_answered_sixth': percentage_answered_sixth,
    'percentage_not_answered_sixth': percentage_not_answered_sixth,
        'percentage_answered_seventh': percentage_answered_seventh,
    'percentage_not_answered_seventh': percentage_not_answered_seventh,
        'percentage_answered_eighth': percentage_answered_eighth,
    'percentage_not_answered_eighth': percentage_not_answered_eighth,
        'percentage_answered_ninth': percentage_answered_ninth,
    'percentage_not_answered_ninth': percentage_not_answered_ninth,
        'percentage_answered_tenth': percentage_answered_tenth,
    'percentage_not_answered_tenth': percentage_not_answered_tenth,
      'other_percentage_answered_first': other_percentage_answered_first,
    'other_percentage_not_answered_first': other_percentage_not_answered_first,
      'other_percentage_answered_second': other_percentage_answered_second,
    'other_percentage_not_answered_second': other_percentage_not_answered_second,
      'other_percentage_answered_third': other_percentage_answered_third,
    'other_percentage_not_answered_third': other_percentage_not_answered_third,
      'other_percentage_answered_fourth': other_percentage_answered_fourth,
    'other_percentage_not_answered_fourth': other_percentage_not_answered_fourth,
      'other_percentage_answered_fifth': other_percentage_answered_fifth,
    'other_percentage_not_answered_fifth': other_percentage_not_answered_fifth,
      'other_percentage_answered_sixth': other_percentage_answered_sixth,
    'other_percentage_not_answered_sixth': other_percentage_not_answered_sixth,
      'other_percentage_answered_seventh': other_percentage_answered_seventh,
    'other_percentage_not_answered_seventh': other_percentage_not_answered_seventh,
      'other_percentage_answered_eighth': other_percentage_answered_eighth,
    'other_percentage_not_answered_eighth': other_percentage_not_answered_eighth,
      'other_percentage_answered_ninth': other_percentage_answered_ninth,
    'other_percentage_not_answered_ninth': other_percentage_not_answered_ninth,
      'other_percentage_answered_tenth': other_percentage_answered_tenth,
    'other_percentage_not_answered_tenth': other_percentage_not_answered_tenth,
    })



