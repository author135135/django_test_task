from django import forms
from students_base_app.models import Student, Group


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'birthdate', 'studentid_cart', 'group']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthdate': forms.TextInput(attrs={'class': 'form-control'}),
            'studentid_cart': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

        self.fields['group_monitor'].choices = Student.objects.filter(group=self.instance.id).values_list('id',
                                                                                                          'full_name')

    class Meta:
        model = Group
        fields = ['group_name', 'group_monitor']
        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control'}),
            'group_monitor': forms.Select(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
