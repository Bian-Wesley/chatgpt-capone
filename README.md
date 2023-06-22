# ChatGPT testifies against Al Capone
## In this project, I used witness testimony against Al Capone and ChatGPT's fine tuning functionality to train it to testify against Al Capone.
### Al Capone went to jail for tax evasion, and witness testimony that showed he had undeclared income was a key part of his downfall. I got the transcripts from famous-trials.com
### OpenAI offers a fine tuning service with their API, where developers can enhance an OpenAI model with their own prompt/completions. 
## Guide to this repository
results.txt holds ChatGPT's answers to examination by a lawyer on questions relating to Al Capone. There isn't enough training data to make it very accurate, but Cicero, a raid, and Al Capone's criminal nature were all present in the original testimonies and they all show up in ChatGPT's "testimony".

All .html files are the original testimony transcripts from the links in links.txt. 

convert.py and convert-smith.py turn the .html files into .jsonl files, which is the format of the training data for OpenAI fine tuning. Special cases are described in notes.txt .

upload.py, make-fine-tune.py, and check-fine-tune.py are all involved in creating the fine tune model and getting it ready to use. 

completion.py sends prompts to the fine tuned model and records its responses. 

This whole project cost me 6 cents. An API key can be obtained from OpenAI to replicate this repository. 
