# encoding: utf-8
import json
import sys

import browser_cookie3
import requests as requests

from workflow import Workflow

API_KEY = 'your-pinboard-api-key'

class user():
    def __int__(self, id, user_id, username, name, avatar_url, org_name, position_name):
        self.id = id
        self.user_id = user_id
        self.username = username
        self.name = name
        self.avatar_url = avatar_url
        self.org_name = org_name
        self.position_name = position_name

def user(cls):
    return {
        'id': cls.id,
        'user_id': cls.user_id,
        'username': cls.username,
        'name': cls.name,
        'avatar_url': cls.avatar_url,
        'org_name': cls.org_name,
        'position_name': cls.position_name
    }

class group():
    def __int__(self, gid, name, avatar, owner, ownername):
        self.gid = gid
        self.name = name
        self.avatar = avatar
        self.owner = owner
        self.ownername = ownername

def group(cls):
    return {
        'gid': cls.gid,
        'name': cls.name,
        'avatar': cls.avatar,
        'owner': cls.owner,
        'ownername': cls.ownername
    }

class Search_request():
    def __init__(self, search, page_id, mode, scene, folder_id):
        self.search = search
        self.page_id = page_id
        self.mode = mode
        self.scene = scene
        self.folder_id = folder_id

def search_to_direct(cls):
    return {
        'search': cls.search,
        'page_id': cls.page_id,
        'mode': cls.mode,
        'scene': cls.scene,
        'folder_id': cls.folder_id
    }

class Search_response():
    def __init__(self, user):
        self.__dict__ = user

    def add_user(self, user):
        self.users.append(user)

def search(query):
    url = "https://apijoyspace.jd.com/v1/search"
    temp_request = Search_request(query, 'cgHL83y1H66MU9Frjlh2', 15, 'share', '')
    request_dic = search_to_direct(temp_request)
    request = json.dumps(request_dic)
    cookie = browser_cookie3.chrome(domain_name='.jd.com')
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=request, cookies=cookie, headers=headers)
    result = json.loads(response.text, object_hook=Search_response)
    users = result.data.users
    groups = result.data.groups

    u_length = len(users)
    if len(users) > 5:
        u_length = 5
    g_length = len(groups)
    if len(groups) > 5:
        g_length = 5

    for i in range(u_length):
        wf.add_item(arg=users[i].username, type="user", title="姓名: " + users[i].name, subtitle="erp: " + users[i].username, valid=True, icon=users[i].avatar_url)

    for j in range(g_length):
        wf.add_item(arg=groups[j].gid, type="group", title="群名称: " + groups[j].name, subtitle="owner: " + groups[j].ownername, valid=True, icon=groups[j].avatar)

    wf.send_feedback()
    session = requests.session()
    session.keep_alive = False

if __name__ == "__main__":
    wf = Workflow()
    query = sys.argv[1]
    search(query)
