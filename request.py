import requests
import json
import sys


if len(sys.argv) != 2:
    print("syntax: python request.py json_query_file")
    exit()
else:
    input = sys.argv[1]
    url = "http://localhost:8080/api"
    req = requests.post(url, json=json.load(open(input, "r")))
    json.dump(req.json(), open(input.replace(".json", "_a.json"), "w"))
