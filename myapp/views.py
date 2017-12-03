from django.http import HttpResponse
from django.shortcuts import render
import datetime

from .models import Assigned, Assignment, DisciplinaryReport, IstationProgram, Student, WeeklyLessonPlan 

#homepage
def index(request):
	students = Student.objects.all
	today = datetime.datetime.now().date()
	
	print("hello", request)
	
	
	
	return render(request, 'myapp/index.html', {'students': students, 'today' : today})
	
	
#Reports
def studentReport(request):
	students = Student.objects.all
	today = datetime.datetime.now().date()
	return render(request, 'myapp/studentReport.html', {'students': students, 'today' : today})
	
def assignmentReport(request):
	assignments = Assignment.objects.all
	today = datetime.datetime.now().date()
	return render(request, 'myapp/assignmentReport.html', {'assignments': assignments, 'today' : today})
	
def disciplinaryReport(request):
	disciplinaryReports = DisciplinaryReport.objects.all
	today = datetime.datetime.now().date()
	return render(request, 'myapp/disciplinaryReport.html', {'disciplinary_reports': disciplinaryReports, 'today' : today})
	
def weeklyLessonPlanReport(request):
	weeklyLessonPlans = WeeklyLessonPlan.objects.all
	today = datetime.datetime.now().date()
	return render(request, 'myapp/weeklyLessonPlanReport.html', {'weekly_lesson_plans': weeklyLessonPlans, 'today' : today})
	
def iStationProgramReport(request):
	iStationPrograms = IstationProgram.objects.all
	today = datetime.datetime.now().date()
	return render(request, 'myapp/iStationProgramReport.html', {'iStations': iStationPrograms, 'today' : today})

	
#Queries
def studentQ1(request):
	
	students = Student.objects.all
	results = Student.objects.none()
	choice = ""
	if request.method ==  "POST":		
		results = Student.objects.raw('SELECT * FROM STUDENT WHERE student_id = %s',[request.POST['studentQ1']])
		choice	= str(request.POST['studentQ1'])
	
	return render(request, 'myapp/studentQ1.html', {'students': students, 'results': results, 'choice':choice })
	

def studentQ2(request):
	students = Student.objects.all
	results = Student.objects.none()
	choice = ""
	
	if request.method ==  "POST":
		results = Student.objects.raw('SELECT student_id,fname, lname, overall_grade FROM STUDENT WHERE overall_grade >= %s',[request.POST['studentQ2']])
		choice	= str(request.POST['studentQ2'])
		
	return render(request, 'myapp/studentQ2.html', {'students': students, 'results': results, 'choice':choice})
	
	
def weeklyLessonPlanQ1(request):
	weeklyLessonPlans = WeeklyLessonPlan.objects.all
	results = WeeklyLessonPlan.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = WeeklyLessonPlan.objects.raw('SELECT * FROM WEEKLY_LESSON_PLAN WHERE week_no = %s',[request.POST['weeklyLessonPlanQ1']])
		choice	= str(request.POST['weeklyLessonPlanQ1'])
	
	return render(request, 'myapp/weeklyLessonPlanQ1.html', {'weeklyLessonPlans': weeklyLessonPlans, 'results': results, 'choice':choice})
	
	
def weeklyLessonPlanQ2(request):
	weeklyLessonPlans = WeeklyLessonPlan.objects.all
	results = WeeklyLessonPlan.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = WeeklyLessonPlan.objects.raw('SELECT * FROM WEEKLY_LESSON_PLAN WHERE start_date BETWEEN  CAST(%s AS DATE) AND CAST(%s AS DATE)',(request.POST['startDate'],request.POST['endDate']))
		choice	=str(request.POST['startDate']) +" to "+ str(request.POST['endDate'])
	
	return render(request, 'myapp/weeklyLessonPlanQ2.html', {'weeklyLessonPlans': weeklyLessonPlans, 'results': results, 'choice':choice})

	
def assignmentQ1(request):
	assignments = Assignment.objects.all
	results = Assignment.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = Assignment.objects.raw('SELECT * FROM ASSIGNMENT WHERE assignment_no = %s',[request.POST['assignmentQ1']])
		choice	= str(request.POST['assignmentQ1'])
	
	return render(request, 'myapp/assignmentQ1.html', {'assignments': assignments, 'results': results, 'choice':choice})
	
	
def assignmentQ2(request):
	weeklyLessonPlans = WeeklyLessonPlan.objects.all
	results = Assignment.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = Assignment.objects.raw('SELECT * FROM ASSIGNMENT WHERE week_no = %s',[request.POST['assignmentQ2']])
		choice	= str(request.POST['assignmentQ2'])
		
	
	return render(request, 'myapp/assignmentQ2.html', {'weeklyLessonPlans': weeklyLessonPlans, 'results': results, 'choice':choice})

def assignmentQ3(request):
	assignments = Assignment.objects.all
	results = Assignment.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = Assigned.objects.raw('SELECT * FROM ASSIGNED as A,STUDENT as S WHERE S.student_id = A.student_id AND A.assignment_no = %s',[request.POST['assignmentQ3']])
		choice	= str(request.POST['assignmentQ3'])
	
	return render(request, 'myapp/assignmentQ3.html', {'assignments': assignments, 'results': results, 'choice':choice})

def assignmentQ4(request):
	assignments = Assignment.objects.all
	results = Assignment.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = Assignment.objects.raw('SELECT * FROM ASSIGNMENT WHERE subject = %s',[request.POST['assignmentQ4']])
		choice	= str(request.POST['assignmentQ4'])
		
	
	return render(request, 'myapp/assignmentQ4.html', {'assignments': assignments, 'results': results, 'choice':choice})
	
def iStationQ1(request):
	iStationPrograms = IstationProgram.objects.all
	results = IstationProgram.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = IstationProgram.objects.raw('SELECT * FROM ISTATION_PROGRAM WHERE program_no = %s',[request.POST['iStationQ1']])
		choice	= str(request.POST['iStationQ1'])
		
	
	return render(request, 'myapp/iStationQ1.html', {'iStationPrograms': iStationPrograms, 'results': results, 'choice':choice})
	
def iStationQ2(request):
	students = Student.objects.all
	results = IstationProgram.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = Student.objects.raw('SELECT * FROM ISTATION_PROGRAM WHERE student_id = %s',[request.POST['iStationQ2']])
		choice	= str(request.POST['iStationQ2'])
		
	
	return render(request, 'myapp/iStationQ2.html', {'students': students, 'results': results, 'choice':choice})

	
def disciplinaryReportQ1(request):
	disciplinaryReports = DisciplinaryReport.objects.all
	results = DisciplinaryReport.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = DisciplinaryReport.objects.raw('SELECT * FROM DISCIPLINARY_REPORT WHERE report_no = %s',[request.POST['disciplinaryReportQ1']])
		choice	= str(request.POST['disciplinaryReportQ1'])
		
	
	return render(request, 'myapp/disciplinaryReportQ1.html', {'disciplinaryReports': disciplinaryReports, 'results': results, 'choice':choice})

	
def disciplinaryReportQ2(request):
	students = Student.objects.all
	results = DisciplinaryReport.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = DisciplinaryReport.objects.raw('SELECT * FROM DISCIPLINARY_REPORT WHERE student_id = %s',[request.POST['disciplinaryReportQ2']])
		choice	= str(request.POST['disciplinaryReportQ2'])
		
	
	return render(request, 'myapp/disciplinaryReportQ2.html', {'students': students, 'results': results, 'choice':choice})
	
	
def disciplinaryReportQ3(request):
	disciplinaryReports = DisciplinaryReport.objects.all
	results = DisciplinaryReport.objects.none()
	choice = ""
	
	if request.method ==  "POST":		
		results = DisciplinaryReport.objects.raw('SELECT * FROM DISCIPLINARY_REPORT WHERE severity_index = %s',[request.POST['disciplinaryReportQ3']])
		choice	= str(request.POST['disciplinaryReportQ3'])
			
	return render(request, 'myapp/disciplinaryReportQ3.html', {'disciplinaryReports': disciplinaryReports, 'results': results, 'choice':choice})