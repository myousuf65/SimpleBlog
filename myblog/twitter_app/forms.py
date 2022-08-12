from django import forms
from .models import trends, tweets

class TweetForm(forms.ModelForm):
    class Meta:
        model = tweets
        fields = [
            'trends_topic',
            'content',
            'writer'
        ]

class TrendsForm(forms.ModelForm):
    class Meta:
        model = trends
        fields = [
            'trend_text'
        ]