from django.conf.urls import url

from . import views

urlpatterns = [

	#Homepage
	url(r'^$', views.index, name='index'),
	
	#Disciplinary Report Query Pages
	url(r'disciplinaryReportQ1', views.disciplinaryReportQ1, name = 'disciplinaryReportQ1'),
	url(r'disciplinaryReportQ2', views.disciplinaryReportQ2, name = 'disciplinaryReportQ2'),
	url(r'disciplinaryReportQ3', views.disciplinaryReportQ3, name = 'disciplinaryReportQ3'),
	
	#Report Pages
    url(r'studentReport', views.studentReport, name='studentReport'),
	url(r'assignmentReport', views.assignmentReport, name='assignmentReport'),
	url(r'disciplinaryReport', views.disciplinaryReport, name='disciplinaryReport'),
	url(r'weeklyLessonPlanReport', views.weeklyLessonPlanReport, name='weeklyLessonPlanReport'),
	url(r'iStationProgramReport', views.iStationProgramReport, name='iStationProgramReport'),
	
	#Query Pages
	url(r'studentQ1', views.studentQ1, name = 'studentQ1'),
	url(r'studentQ2', views.studentQ2, name = 'studentQ2'),
	url(r'weeklyLessonPlanQ1', views.weeklyLessonPlanQ1, name = 'weeklyLessonPlanQ1'),
	url(r'weeklyLessonPlanQ2', views.weeklyLessonPlanQ2, name = 'weeklyLessonPlanQ2'),
	url(r'assignmentQ1', views.assignmentQ1, name = 'assignmentQ1'),
	url(r'assignmentQ2', views.assignmentQ2, name = 'assignmentQ2'),
	url(r'assignmentQ3', views.assignmentQ3, name = 'assignmentQ3'),
	url(r'assignmentQ4', views.assignmentQ4, name = 'assignmentQ4'),
	url(r'iStationQ1', views.iStationQ1, name = 'iStationQ1'),
	url(r'iStationQ2', views.iStationQ2, name = 'iStationQ2'),
	
	
]