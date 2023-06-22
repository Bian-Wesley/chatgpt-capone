import requests

my_api_key = "sk-XXXXXX"
auth = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + my_api_key
}
payload = {
    "training_file": "file-6yvYcfiKBhI65A5ZkjmPa1F7"
}

resp = requests.post("https://api.openai.com/v1/fine-tunes", headers = auth, json = payload)
print(resp.text)
'''
{
  "object": "fine-tune",
  "id": "ft-tFfkZT1qNAKKEbj9gUZfDRD3",
  "hyperparams": {
    "n_epochs": 4,
    "batch_size": null,
    "prompt_loss_weight": 0.01,
    "learning_rate_multiplier": null
  },
  "organization_id": "org-iOE2YQF9eN0bK1kz4otr8V3E",
  "model": "curie",
  "training_files": [
    {
      "object": "file",
      "id": "file-6yvYcfiKBhI65A5ZkjmPa1F7",
      "purpose": "fine-tune",
      "filename": "all.jsonl",
      "bytes": 7702,
      "created_at": 1687375045,
      "status": "processed",
      "status_details": null
    }
  ],
  "validation_files": [],
  "result_files": [],
  "created_at": 1687375087,
  "updated_at": 1687375087,
  "status": "pending",
  "fine_tuned_model": null,
  "events": [
    {
      "object": "fine-tune-event",
      "level": "info",
      "message": "Created fine-tune: ft-tFfkZT1qNAKKEbj9gUZfDRD3",
      "created_at": 1687375087
    }
  ]
}

'''