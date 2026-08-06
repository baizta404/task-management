from django import forms
from tasks.models import Task

class TaskForm(forms.Form):
    title = forms.CharField(max_length=250,label='Task Title')
    description = forms.CharField(widget=forms.Textarea,label='Task Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget,label='Due Date')
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[],label='Assigned To')

    def __init__(self,*args,**kwargs):
        employees = kwargs.pop('employees',[])
        super().__init__(*args, **kwargs )
        self.fields['assigned_to'].choices = [
            (emp.id,emp.name) for emp in employees]

class StyledForMixin:
    '''Mixin to apply style to form fields'''
    default_clasees = "border-2 border-red-200 w-full p-2 bg-gray-300 rounded-lg shadow-sm"
    def apply_styled_widgets(self):
        for fied_name ,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class':self.default_clasees,
                    'placeholder':f'Enter {field.label.lower()}'
                })
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':self.default_clasees,
                    'placeholder':f'Enter {field.label.lower()}'
                })
            elif isinstance(field.widget,forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class':'border border-red-200 px-3 py-2 bg-gray-300 rounded-md shadow-sm'
                })
            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': 'px-3 py-2 rounded-lg'
                })
            else:{
                field.widget.attrs.update({
                    'class':self.default_clasees
                })
            }
            

#Django Model Forms
class TaskModelForm(StyledForMixin,forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','assigned_to']
        widgets={
            'due_date':forms.SelectDateWidget,
            'assigned_to':forms.CheckboxSelectMultiple
        }
        # exclude = ['project','is_completed','created_at','updated_at'] #egula baad diye baki gula dekhabe taile
        ''' Manual Widget
        # widgets = {
        #     'title':forms.TextInput(attrs={
        #         "class":"border-2 border-red-200 w-full p-2 bg-gray-300 rounded-lg shadow-sm","placeholder":"Enter Your Projects Title"
        #     }),
        #     'description':forms.Textarea(attrs={
        #         "class":"border-2 border-red-200 p-2 w-full bg-gray-300 rounded-lg shadow-sm","placeholder":"Enter Your Descriptions",
        #         "rows":5
        #     }),
        #     'due_date':forms.SelectDateWidget(attrs={
        #         "class":"border-2 border-red-200 bg-gray-200 p-2 rounded-md shadow-sm"
        #     }),
        #     'assigned_to':forms.CheckboxSelectMultiple(attrs={
        #         "class":"px-3 py-2 rounded-lg shadow-sm"
        #     })
        # } 
         '''
    '''Widget with Mixin'''
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()