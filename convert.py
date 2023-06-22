def html_to_jsonl(lawyer, witness, file, output):
    with open(file, "r", encoding="utf8") as bc:
        raw_text = bc.read()
        #<strong>Ahern:</strong> --> {"prompt": "
        #<br><strong>Bragg:</strong> --> ", "completion": ""
        #the next <br> should become "}\n
        no_quotes = raw_text.replace("\"", "'")
        jsonl1 = no_quotes.replace("<strong>" + lawyer + ":</strong>", "{\"prompt\":\"")
        jsonl2 = jsonl1.replace("<br><strong>"+ witness + ":</strong>", "\", \"completion\": \"")
        jsonl3 = jsonl2.replace("<br>", "\"}\n")
        jsonl = jsonl3 + "\"}\n" #will be missing on the last one because there is no trailing <br>
        #write the resulting jsonl to a file
        with open(output, "a") as out:
            out.write(jsonl)

examinations = [
    {
        "lawyer": "Ahern",
        "witness": "Bragg",
        "file": "bragg-cross.html",
        "output": "braggc.jsonl"
    },
    {
        "lawyer": "Green",
        "witness": "Bragg",
        "file": "bragg-examination.html",
        "output": "bragge.jsonl"
    },
    {
        "lawyer": "Green",
        "witness": "Hoover",
        "file": "hoover.html",
        "output": "hoover.jsonl"
    }
]

for ex in examinations:
    html_to_jsonl(ex["lawyer"], ex["witness"], ex["file"], "all.jsonl")


