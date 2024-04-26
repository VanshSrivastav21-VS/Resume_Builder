from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'about', 'age', 'email', 'phone,', 'skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'degree1', 'college1', 'year1', 'degree2', 'college2', 'year2', 'degree3', 'college3', 'year3', 'lang1', 'lang2', 'lang3', 'project1', 'durat1', 'desc1', 'project2', 'durat2', 'desc2', 'company1', 'post1', 'duration1', 'lin11', 'company2', 'post2', 'duration2', 'lin21', 'ach1', 'ach2', 'ach3')
  # Include all fields of the model
