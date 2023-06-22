import requests

my_api_key = "sk-XXXX"
auth = {
    "Authorization": "Bearer " + my_api_key
}
payload = {
    "purpose": "fine-tune"
}
files = {'file': open('all.jsonl','rb')}

resp = requests.post("https://api.openai.com/v1/files", headers = auth, files=files,  data = payload)
print(resp.text)

'''
{
  "object": "file",
  "id": "file-cIHGDMF0A1bAvEAqxalR3LAH",
  "purpose": "fine-tune",
  "filename": "all.jsonl",
  "bytes": 7703,
  "created_at": 1687372802,
  "status": "uploaded",
  "status_details": null
}

attempt 2
{
  "object": "file",
  "id": "file-6yvYcfiKBhI65A5ZkjmPa1F7",
  "purpose": "fine-tune",
  "filename": "all.jsonl",
  "bytes": 7702,
  "created_at": 1687375045,
  "status": "uploaded",
  "status_details": null
}
'''