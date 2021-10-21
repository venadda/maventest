from django import forms
import datetime
class sample(forms.Form):
    first_name=forms.CharField(max_length=100) #<input type=text lenght=100 >
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    #<select>
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    gender =  forms.BooleanField(initial=True)# male or female default is True
    Ip = forms.GenericIPAddressField()
    file=forms.FileField()
    t=(('1','one'),('2','Two'),('3','Three'))
    mchoice=forms.MultipleChoiceField(choices=t)
    mtchoice=forms.TypedMultipleChoiceField(choices=t,coerce=str)
    choice=forms.TypedChoiceField(choices=t,coerce=str)
    department = forms.ChoiceField(choices = (('1','CSE'),('2','IT'),('3','ECE'),('4','EEE')))
    datejoined=forms.DateField( initial=datetime.date.today)
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
