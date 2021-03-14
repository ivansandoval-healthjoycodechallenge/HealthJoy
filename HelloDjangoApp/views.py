import requests
from github import Github
from django.shortcuts import render
from .forms import GitHubCreds 
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = GitHubCreds(request.POST)
        if form.is_valid():     
            
            # Please note..
            # Ideally I would make an API call and not have the below GitHub logic coupled to this button event
                #reusability - call the 'FORK' endpoint from anywhere, not just this form...
                #security - adding OAuth authentication/authorization for the API/endpoint creates another layer of security
            # Not familiar enough with Python/Django, would take significant amount of time to build out a legitimate solution for this (front facing app and api with oauth)
            
           try:
            # Github username
            token = request.POST.get('token')
        
            #connects to users account
            gg = Github(token)
            github_user = gg.get_user()
        
            #ideally store in app settings, config file of some sort...                   
            g = Github('d282c87763b50bdc71233bbb26f803785e946cbb')     
            repo = g.get_repo("ivansandoval-sandbox/HealthJoy")            

            # fork the repo to the users account
            myfork = github_user.create_fork(repo)  
                   
            #give the user a success message
            messages.success(request, 'Fork successful!')

           #reasonable to catch separately and do different things (timeouts, too many requests, etc.)
           #for the sake of this im just going to catch all under 'Exception'
           except Exception as e:
                messages.error(request, e)
           
    else:
        form = GitHubCreds()
    return render(request, 'HelloDjangoApp/index.html', {'form': form})