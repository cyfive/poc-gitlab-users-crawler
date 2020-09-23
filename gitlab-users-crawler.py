#!/usr/bin/env python3
import requests
from requests.exceptions import HTTPError
import json, time 

# stupid config
gitlab_url = "https://gitlab.local"
api_url = "/api/v4/users/"
start_id = 1
stop_id = 100

print("id;state;created_at;username;name;public_email;organization;job_title;work_information;avatar_url;web_url")

for id in range(start_id, stop_id+1):
    r = requests.get(gitlab_url+api_url+str(id))
    if r.status_code == 200:
        res_line = ""
        data = r.json()

        if 'id' in data:
            res_line = res_line + str(data['id'])+";"
        else:
            res_line = res_line + ";"

        if 'state' in data:
            res_line = res_line + data['state']+";"
        else:
            res_line = res_line + ";"

        if 'created_at' in data:
            res_line = res_line + data['created_at']+";"
        else:
            res_line = res_line + ";"

        if 'username' in data:
            res_line = res_line + data['username']+";"
        else:
            res_line = res_line + ";"

        if 'name' in data:
            res_line = res_line + data['name']+";"
        else:
            res_line = res_line + ";"

        if 'public_email' in data:
            res_line = res_line + data['public_email']+";"
        else:
            res_line = res_line + ";"

        if 'organization' in data:
            res_line = res_line + str(data['organization'])+";"
        else:
            res_line = res_line + ";"

        if 'job_title' in data:
            res_line = res_line + data['job_title']+";"
        else:
            res_line = res_line + ";"

        if 'work_information' in data:
            res_line = res_line + str(data['work_information'])+";"
        else:
            res_line = res_line + ";"

        if 'avatar_url' in data:
            res_line = res_line + data['avatar_url']+";"
        else:
            res_line = res_line + ";"

        if 'web_url' in data:
            res_line = res_line + data['web_url']

        print(res_line)
    time.sleep(1)

