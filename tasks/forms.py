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


class StyledFormMixin:
    """Maxin to apply style to form fields"""
    default_classes= "border-2 border-gray-300 w-full rounded-lg shadow-sm"
    

    def apply_styled_widgets(self):
        for field_name,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f'Enter {field.label.lower()}'
                })
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class': f'{self.default_classes} resize-none',
                    'placeholder': f'Enter {field.label.lower()}',
                    'rows':5
                })
            elif isinstance(field.widget,forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': "border-2 border-gray-300 rounded-lg shadow-sm"
                })
            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class':'space-y-2'
                })


#mixin use korte hoile kintu Mixin ta inheritance korte hobe .always first a bosaite hobe
class TaskModelForm(StyledFormMixin,forms.ModelForm):
    class Meta:
        model = Task
        #fields = '__all__' for selecting all fields
        fields =['title','description','due_date','assigned_to']
        #exclude=["",""] just mention which should exclude from all
        widgets={
            'due_date':forms.SelectDateWidget,
            'assigned_to':forms.CheckboxSelectMultiple
        }
        """Manual adding without mixin : allways widgets need to be in Meta Class"""
        # widgets ={
        #     'title':forms.TextInput(attrs={
        #         'class':"border-2 border-gray-300 w-full rounded-lg shadow-sm",
        #         'placeholder': "Enter Tasks's Title.."
        #     }),
        #     'due_date': forms.SelectDateWidget({
        #         'class': "border-2 border-gray-300 rounded-lg shadow-sm"
        #     }),
        #     'assigned_to':forms.CheckboxSelectMultiple(),
        #     'description':forms.Textarea(attrs={
        #         "class":"border-2 border-gray-300 w-full rounded-lg shadow-sm resize-none",
        #         'row':5,
        #         'placeholder':"Write detail's about the task"
        #     })
        # }

    """def __init__ for self appllying mixin| Meta Class er baire thakte hobe"""
    def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.apply_styled_widgets()