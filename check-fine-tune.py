import requests

my_api_key = "sk-XXXXXXXXX" 
auth = {
    "Authorization": "Bearer " + my_api_key
}

resp = requests.get("https://api.openai.com/v1/fine-tunes/ft-tFfkZT1qNAKKEbj9gUZfDRD3", headers = auth)
print(resp.text)

'''
allmodels = requests.get("https://api.openai.com/v1/models", headers = auth)
model_list = allmodels.json()
for model in model_list["data"]:
    print(model["id"])
'''