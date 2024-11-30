from django.shortcuts import render
from django.http import HttpResponse

def start_quiz(request, topic_name):
    return HttpResponse(f"Starting quiz for topic: {topic_name}")
