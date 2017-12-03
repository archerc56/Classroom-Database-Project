# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Assigned(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING, primary_key=True)
    assignment_no = models.ForeignKey('Assignment', models.DO_NOTHING, db_column='assignment_no')
	
    def __str__(self):
        return self.student.fname + ' ' + self.student.lname + ': '+self.assignment_no.name

    class Meta:
        managed = False
        db_table = 'assigned'
        unique_together = (('student', 'assignment_no'),)


class Assignment(models.Model):
    assignment_no = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=13, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    total_points = models.IntegerField(blank=True, null=True)
    week_no = models.ForeignKey('WeeklyLessonPlan', models.DO_NOTHING, db_column='week_no', blank=True, null=True)
	
    def __str__(self):
        return '# ' + str(self.assignment_no) + ' ' + self.name

    class Meta:
        managed = False
        db_table = 'assignment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DisciplinaryReport(models.Model):

    accidental = 1
    minor = 2
    average = 3
    major = 4
    SEVERITY_CHOICES = (
        (accidental, 'Accidental'),
        (minor, 'Minor'),
        (average, 'Average'),
        (major, 'Major'),
    )
    report_no = models.IntegerField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    incident = models.CharField(max_length=144, blank=True, null=True)
    time = models.CharField(max_length=5, blank=True, null=True)
    severity_index = models.IntegerField(choices=SEVERITY_CHOICES,blank=True, null=True)
	
    def __str__(self):
        return 'Report #' + str(self.report_no) + ' ' + self.student.lname + ', ' + self.student.fname

    class Meta:
        managed = False
        db_table = 'disciplinary_report'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IstationProgram(models.Model):
    program_no = models.IntegerField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    month = models.CharField(max_length=3, blank=True, null=True)
    no_of_sections = models.IntegerField(blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
	
    def __str__(self):
        return 'Program #' + str(self.program_no) + ' ' + self.student.lname + ', ' + self.student.fname

    class Meta:
        managed = False
        db_table = 'istation_program'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    overall_grade = models.FloatField(blank=True, null=True)
    emergency_contact_no = models.CharField(max_length=10, blank=True, null=True)
	
    def __str__(self):
        return str(self.student_id) + ': ' + self.lname + ', ' + self.fname

    class Meta:
        managed = False
        db_table = 'student'


class WeeklyLessonPlan(models.Model):
    week_no = models.IntegerField(primary_key=True)
    summary = models.CharField(max_length=144, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
	
    def __str__(self):
        return 'Week #' + str(self.week_no)

    class Meta:
        managed = False
        db_table = 'weekly_lesson_plan'
