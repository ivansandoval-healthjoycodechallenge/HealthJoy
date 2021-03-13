import requests
from github import Github

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .forms import GitHubCreds 
from pprint import pprint


def index(request):
    if request.method == 'POST':
        form = GitHubCreds(request.POST)
        if form.is_valid():
            # Github username
            username = request.POST.get('username')
            # Github password
            password = request.POST.get('password')

            # pygithub object
            g = Github(username, password)

            # get that user
            user = g.get_user()
            
            for repo in user.get_repos(): pprint(repo)

    else:
        form = GitHubCreds()
    return render(request, 'HelloDjangoApp/index.html', {'form': form})
 