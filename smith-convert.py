with open("smith.html", "r", encoding="utf8") as bc:
    raw_text = bc.read()
    no_quotes = raw_text.replace("\"", "'")
    #<p><strong>Grossman:</strong> --> {"prompt": "
    jsonl1 = no_quotes.replace("<p><strong>Grossman:</strong>", "{\"prompt\": \" ")
    jsonl2 = jsonl1.replace("<br><strong></strong></p>\n<p><strong>Smith:</strong>", "\", \"completion\":\" ")
    jsonl = jsonl2.replace("<br><strong></strong></p>", "\"}")
    #write the resulting jsonl to a file
    with open("all.jsonl", "a") as out:
        out.write(jsonl)