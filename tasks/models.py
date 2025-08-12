from django.db import models

#Many to Many Relationship
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


#Many to One Relationship
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()


# Create your models here.
class Task(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                default = 1)
    assigned_to = models.ManyToManyField(Employee,related_name='tasks')
    title = models.CharField(max_length = 250)
    description = models.TextField()
    due_date = models.DateField()
    is_complited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#one to one
class TaskDetails(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
    )
    task = models.OneToOneField(Task,
                                on_delete = models.CASCADE,
                                related_name = "details")
    assigned_to = models.CharField(max_length = 100)
    priority = models.CharField(max_length = 1 ,choices = PRIORITY_OPTIONS,default = LOW)

#ekta task ->onek gula employee
#ekjon employee -> onek gula task
#ekta project a onek task
# >>> from tasks.models import Employee,Task
# >>> employee = Employee.objects.create(name="Romjan Ali",email="ramjan@gmail.com")
# >>> employee2 = Employee.objects.create(name="Minjaj Adil",email="minhaj@gmail.com")
# >>> task = Task.objects.create(title="Notun taska ri",description="Ki ar hoibo re bhai emni",due_date ="2025-12-25")
# >>> task.assigned_to.add(employee)
