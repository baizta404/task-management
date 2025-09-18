from django import forms
from tasks.models import Task
class TaskForm(forms.Form):
    title  = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea,
                                  label='Task Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget,label='Due Date')
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[])

    def __init__(self,*args, **kwargs):
        # print(args,kwargs)
        employees = kwargs.pop('employees',[])
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices=[
            (emp.id,emp.name) for emp in employees
        ]


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        #fields = '__all__' for selecting all fields
        fields =['title','description','due_date','assigned_to']
        #exclude=["",""] just mention which should exclude from all
        widgets ={
            'title':forms.TextInput(attrs={
                'class':"border-2 border-gray-300 w-full rounded-lg shadow-sm",
                'placeholder': "Enter Tasks's Title.."
            }),
            'due_date': forms.SelectDateWidget({
                'class': "border-2 border-gray-300 rounded-lg shadow-sm"
            }),
            'assigned_to':forms.CheckboxSelectMultiple(),
            'description':forms.Textarea(attrs={
                "class":"border-2 border-gray-300 w-full rounded-lg shadow-sm resize-none",
                'row':5,
                'placeholder':"Write detail's about the task"
            })
        }