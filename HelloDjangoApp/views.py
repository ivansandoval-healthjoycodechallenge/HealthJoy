import requests
from github import Github

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .forms import GitHubCreds 
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = GitHubCreds(request.POST)
        if form.is_valid():            
           try:
            # Github username
            token = request.POST.get('token')
        
            #connects to users account
            gg = Github(token)
            github_user = gg.get_user()
        
            # this applications repo PAT 
            # ideally store secure... 
            g = Github('bc54d96e80ae7a915c0666683f976ddee4cc009b')     
            repo = g.get_repo("ivansandoval-healthjoycodechallenge/HealthJoy")            

             # fork the repo to the users account
            myfork = github_user.create_fork(repo)  
                   
            #give the user a success message
            messages.success(request, 'Fork successful!')

           #reasonable to catch separately and do different things (timeouts, too many requests, etc.)
           #for the sake of this im just going to catch all
           except Exception as e:
                messages.error(request, e)
           
    else:
        form = GitHubCreds()
    return render(request, 'HelloDjangoApp/index.html', {'form': form})