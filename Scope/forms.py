from django import forms
from .models import Student
from .models import Course

class student_Form(forms.Form):
        full_name = forms.CharField(required=True)
        dob = forms.DateField(required=True)   
        gender = forms.CharField(required=True)
        email  = forms.EmailField(required=True) 
        mob = forms.CharField(required=True) 
        education = forms.CharField(required=True) 
        guardian = forms.CharField(required=True) 
        guard_occupation = forms.CharField(required=True)
        guard_mob = forms.CharField(required=True) 
        course = forms.CharField(required=True)
        mode = forms.CharField(required=True) 
        location = forms.CharField(required=True) 
        timing = forms.CharField(required=True) 
        address = forms.CharField(required=True) 
        country = forms.CharField(required=True) 
        state = forms.CharField(required=True) 
        city = forms.CharField(required=True) 
        pin = forms.CharField(required=True) 
            
# #CUSTOM VALIDATIONS:

        def clean_mob(self):
                Mobile = self.cleaned_data.get('mob')
                if not Mobile.isnumeric():
                        raise forms.ValidationError("Contact field must contain numbers only !")
                elif len(Mobile)!=10:
                        raise forms.ValidationError("Contact field must contain 10 Numbers !")
                return Mobile            


           
        def clean_full_name(self):
                Full_Name =self.cleaned_data.get('full_name')
                if not Full_Name.replace(' ', '').isalpha():
                        raise forms.ValidationError("Name Field must contain Alphabets only")
                return Full_Name
        
        def clean_email(self):
                Email = self.cleaned_data.get('email')
                if Email.find('@gmail.com')==-1:
                        raise forms.ValidationError("Please enter valid Gmail Id!!")
                return Email


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'Full_Name', 'Date_of_Birth', 'Gender', 'Email', 'Mobile_number',
            'Education_Qualification', 'Guardian_Name', 'Guardian_Occupation',
            'Guardian_Mobile', 'Address', 'Country', 'State', 'City', 'Pin_code',
            'Profile_Image' ,'Password' 
        ]
        widgets = {
            'Date_of_Birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['Profile_Image'].required = False

# ⬇️ Add this for password safety
        self.fields['Password'].required = False
        self.fields['Password'].widget.attrs.update({
        'placeholder': 'Leave blank to keep current password'
    })



