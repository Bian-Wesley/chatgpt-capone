import requests

#using the longest response given (Rev. Hoover) and the below website
token_length = 83 #https://platform.openai.com/tokenizer

my_api_key = "sk-XXXXXX"
auth = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + my_api_key
}
payload = {
    "model": "curie:ft-personal-2023-06-21-19-33-27",
    "prompt": "Who is the defendant of this trial?",
    "temperature": 0.7,
    "max_tokens": token_length
}
questions = [
    "Who is the defandant of this trial?",
    "Do you know Al Capone?",
    "On what year did the raid take place?",
    "Please describe what you in this raid",
    "Does Al Capone own gambling enterprises?",
    "Is Al Capone a good man?",
    "Why did you participate in the citizen's raid on 4818 West 22nd Street?",
    "Have you ever received threats from Al Capone or his subordinates?",
    "How many raids have you been a part of?",
    "How would Capone pay his bills?",
    "Have you ever spoken to the defendant Alphonse Capone?",
    "What city do you live in?",
    "Is Al Capone a rich man?",
    "Do you believe Al Capone has been avoiding income tax?"
]

for question in questions:
    payload["prompt"] = question
    resp = requests.post("https://api.openai.com/v1/completions", headers = auth, json = payload)
    print("Q:", question)
    print("A:", resp.json()["choices"][0]["text"])

