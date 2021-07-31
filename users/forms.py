from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['bio','profile_pic','website_url','facebook_url','twitter_url','linkedin_url','instagram_url']