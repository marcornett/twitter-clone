from django import forms
from twitteruser.models import TwitterUser
class TweetForm(forms.Form):
    tweet = forms.CharField(max_length=140, widget=forms.Textarea)

