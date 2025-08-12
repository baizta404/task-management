from django import forms
from tasks.models import Task

#Django Forms
class TaskForm(forms.Form):
    title = forms.CharField(max_length=250,label="Task Title")
    description = forms.CharField(widget=forms.Textarea,label="Task Description")
    due_date = forms.DateField(widget=forms.SelectDateWidget,label="Due Date")
    assigned_to = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[],
        label="Assigned to Whom?"
        )
    def __init__(self,*args, **kwargs):
        # print("pop korar age",args,kwargs)
        employees = kwargs.pop("employees",[])
        # print(employees)
        
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [(emp.id,emp.name) for emp in employees ]

class StyledFormMixin:
    """Mixin to apply style to form fields"""
    default_classes = "border-2 border-gray-300 w-full rounded-lg shadow-sm"
    def apply_styled_widgets(self):
        for field_name,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':f'Enter {field.label.lower()}'
                    })
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':f"{self.default_classes} resize-none",
                    'placeholder':f'Enter {field.label.lower()}',
                    'rows':5
                })
            elif isinstance(field.widget,forms.SelectDateWidget):
                print('inside date box')
                field.widget.attrs.update({
                    'class':"border-2 border-gray-800 bg-red-600 px-3 py-2 rounded-lg shadow-sm "
                })
            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                print('inside check box')
                field.widget.attrs.update({
                    'class':"space-y-2"
                })
            else:
                print("Inside else")
                field.widget.attrs.update({
                    'class':self.default_classes
                })

# Django Model Forms
class TaskModelForm(StyledFormMixin,forms.ModelForm):
    class Meta:
        model = Task
        # fields diel selected gula dekha jabe serial wise
        fields = ['title','description','due_date','assigned_to']
        widgets={
            'due_date':forms.SelectDateWidget,
            'assigned_to':forms.CheckboxSelectMultiple
        }
        
        #exclude dile egula chara baki gula
        # exclude = ['project','is_complited','created_at','updated_at']
        """Manual Widgets"""
        # widgets = {
        #             'title':forms.TextInput(attrs={
        #                 'class':"border-2 border-gray-300 w-full rounded-lg shadow-sm ",'placeholder':'Enter Your Task title'
        #             }),
        #             'description':forms.Textarea(attrs={
        #                 'class':"border-2 border-gray-300 w-full rounded-lg p-3 shadow-sm ",'placeholder':'Describe the task...'
        #             }),
        #             'due_date':forms.SelectDateWidget(attrs={
        #                 'class':"border-2 border-gray-800 bg-red-600 px-3 py-2 rounded-lg shadow-sm "
        #             }),
        #             'assigned_to':forms.CheckboxSelectMultiple(attrs={
        #                 'class':" "
        #             })
        #           }
    """Using Mixin widget""" #meta class er bbahire mixin korte hoy
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()


