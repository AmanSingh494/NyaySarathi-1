from django.shortcuts import render,redirect

from django.http import JsonResponse
# written by admin

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login, logout
# from django.contrib import messages
# from django.http import HttpResponse

# For API handling and request OpenAI
import json
import openai
import requests
# from django.conf import settings 

# Create your views here.


# By chat-gpt needs modification for further usage 
def get_vidura_response(user_message):
    # Define your OpenAI API endpoint
    # endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
    endpoint = "https://api.openai.com/v1/engines/davinci/completions"

    # Set your OpenAI API key
    
    # api_key = "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"
    api_key = "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"

    # Define the data for the API request
    data = {
        "prompt": user_message,
        "max_tokens": 50  # Adjust the number of tokens as needed
    }

    # Set headers with your API key
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Send a POST request to the OpenAI API
    response = requests.post(endpoint, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json().get("choices")[0].get("text")
    else:
        # getting the error messae
        with open("response.txt", 'w') as f:
            f.write(response.text)
            
        return "I'm sorry, I couldn't process your request at the moment."


# Handliing request for vidura from openai api
def vidura(request):
    greeting = "Hi, How can I assist you today? "

    if request.method == 'POST':
        user_message = request.POST.get("message")
        vidura_response = get_vidura_response(user_message)
        return JsonResponse({"message": vidura_response})
    
    return render(request, "vidura.html", {"greeting" : greeting })


