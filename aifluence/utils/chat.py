from aifluence.constants import QB_CONFIG

import hashlib
import hmac
import random
import math
import datetime
import requests
import json
import asyncio
# from requests import async
# import requests_async as requests

def create_signature(key, message):
    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')
    digester = hmac.new(key, message, hashlib.sha1)
    return digester.hexdigest()

def session_params():
    params = {}
    params['application_id'] = QB_CONFIG['credentials']['app_id']
    params['auth_key'] = QB_CONFIG['credentials']['auth_key']
    params['nonce'] = math.floor(random.random() * 10000)
    params['timestamp'] = math.floor(datetime.datetime.now().timestamp())
    # signature
    message = 'application_id=' + params['application_id'] + '&auth_key=' + params['auth_key'] + '&nonce=' + str(params['nonce']) + '&timestamp=' + str(params['timestamp'])
    key = QB_CONFIG['credentials']['auth_secret']
    params['signature'] = create_signature(key, message)
    return params

async def create_session():
    params = session_params()
    url = QB_CONFIG['url']['base'] + QB_CONFIG['url']['session']
    res = requests.post(url, params)
    res_json = res.json()
    session_token = res_json['session']['token']
    return session_token

async def create_user(session_token, username):
    url = QB_CONFIG['url']['base'] + QB_CONFIG['url']['users']['base']
    user_params = {'login' : username, 'password' : QB_CONFIG['user']['password']}
    params = {'user' : user_params}
    headers = {'Content-Type' : 'application/json', 'QB-Token' : session_token}
    res = requests.post(url, data = json.dumps(params), headers = headers)
    if 'errors' in res:
        session_token =  asyncio.run(create_session())
        headers['QB-Token'] = session_token
        res = requests.post(url, data = json.dumps(params), headers = headers)
    res_json = res.json()
    return res_json['user']['id']

async def login_chat(session_token, username):
    url = QB_CONFIG['url']['base'] + QB_CONFIG['url']['login']
    headers = {'Content-Type' : 'application/json', 'QB-Token' : session_token}
    params = {'login' : username, 'password' : QB_CONFIG['user']['password']}
    res_json = requests.post(url, data = json.dumps(params), headers = headers).json()
    return res_json['user']['id']

async def create_dialog(session_token, dialog_name, username, opponent_id, type, campaign_id, campaign_brief, campaign_detail):
    url = QB_CONFIG['url']['base'] + QB_CONFIG['url']['chat']['dialog']
    headers = {'Content-Type' : 'application/json', 'QB-Token' : session_token}
    params = {'type' : QB_CONFIG['chat']['dialog_type']['GROUP'], 'name' : dialog_name, 'occupants_ids' : str(opponent_id), 'data' : {'class_name' : QB_CONFIG['chat']['custom_class']['name'], 'type' : type, 'campaign_id' : campaign_id, 'campaign_brief' : campaign_brief, 'campaign_detail' : campaign_detail}}
    res = requests.post(url, data = json.dumps(params), headers = headers)
    if 'errors' in res:
        session_token =  asyncio.run(create_session())
        asyncio.run(login_chat(session_token, username))
        headers['QB-Token'] = session_token
        res = requests.post(url, data = json.dumps(params), headers = headers)
    print('util/chat.py/create_dialog/params++++++++++++++++++++++++++++', params)
    print('util/chat.py/create_dialog/res++++++++++++++++++++++++++++', res.json())
    return res.json()

# not used now
async def id_by_login(session_token, username):
    url = QB_CONFIG['url']['base'] + QB_CONFIG['url']['users']['by_login'] + '?login=' + username
    headers = {'QB-Token' : session_token}
    res_json = requests.get(url, headers = headers).json()
    return res_json['user']['id']

async def get_dialogs(session_token):
    url = QB_CONFIG['url']['base'] + QB_CONFIG['url']['chat']['dialog']
    headers = {'Content-Type' : 'application/json', 'QB-Token' : session_token}
    res_json = requests.post(url, headers = headers).json()
    return res_json['items']




