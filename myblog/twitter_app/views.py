from django.shortcuts import render, HttpResponse
from .models import trends, tweets
from .forms import TrendsForm, TweetForm
# Create your views here.
def indexView(request):
    trend = trends.objects.all()
    context = {
        'trend' : trend
    }
    return render(request , 'index.html' , context)


def detailView(request, trends_topic_id):
    tweet = trends.objects.get(pk=trends_topic_id)
    context = {
        'tweet': tweet
    }
    return render(request, 'detail.html' , context)

def createTweetView(request):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TweetForm()

    context = {
        'form': form
    }
    return render(request , 'createTweet.html' , context)

def createTrendView(request):
    form = TrendsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TrendsForm()

    context = {
        'form': form
    }
    return render(request , 'createTrend.html' , context)