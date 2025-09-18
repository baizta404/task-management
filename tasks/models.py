from django.db import models

# Create your models here.

# Project er sathe task er many to one rel thakbe
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self):
        return self.name
# Task er sathe Employee er many to many thakete pare
# 1 ta employee : Onekgula Task || 1 ta task : onek jon employee
class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    #Project er sathe many to one
    project = models.ForeignKey(
        Project,on_delete=models.CASCADE,
        default = 1,
        related_name = 'tasks' ) #ei nam disi cause Project.tasks diye acces kora jabe
    # employeer sathe many to many
    assigned_to =models.ManyToManyField(
        Employee,related_name='tasks' # Employee.tasks dekhar jonno
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# one to one 1ta task er sudhu 1 ta details thakbe
class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'

    PRIORITY_OPTIONS = (
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,"Low")
    )

    task = models.OneToOneField(
        Task,on_delete=models.CASCADE,
        related_name='details' # Task.details diye acces korte parbe
    )
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(choices=PRIORITY_OPTIONS,default=LOW,max_length=1)

