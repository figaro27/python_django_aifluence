from InstagramAPI import InstagramAPI
import re
import os
import json
import requests
import time

InstagramInstance = None
class CustomizedInstagramAPI(InstagramAPI):
    def find_urls(self, text):
        regex = r"((?:(http|https|Http|Https|rtsp|Rtsp):\/\/(?:(?:[a-zA-Z0-9\$\-\_\.\+\!\*\'\(\)\,\;\?\&\=]|(?:\%[a-fA-F0-9]{2})){1,64}(?:\:(?:[a-zA-Z0-9\$\-\_\.\+\!\*\'\(\)\,\;\?\&\=]|(?:\%[a-fA-F0-9]{2})){1,25})?\@)?)?((?:(?:[a-zA-Z0-9\_][a-zA-Z0-9\_\-]{0,64}\.)+(?:(?:aero|arpa|asia|a[cdefgilmnoqrstuwxz])|(?:biz|b[abdefghijmnorstvwyz])|(?:cat|com|coop|c[acdfghiklmnoruvxyz])|d[ejkmoz]|(?:edu|e[cegrstu])|f[ijkmor]|(?:gov|g[abdefghilmnpqrstuwy])|h[kmnrtu]|(?:info|int|i[delmnoqrst])|(?:jobs|j[emop])|k[eghimnprwyz]|l[abcikrstuvy]|(?:mil|mobi|museum|m[acdeghklmnopqrstuvwxyz])|(?:name|net|n[acefgilopruz])|(?:org|om)|(?:pro|p[aefghklmnrstwy])|qa|r[eosuw]|s[abcdeghijklmnortuvyz]|(?:tel|travel|t[cdfghjklmnoprtvwz])|u[agksyz]|v[aceginu]|w[fs]|y[et]|z[amw]))|(?:(?:25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[1-9][0-9]|[1-9])\.(?:25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[1-9][0-9]|[1-9]|0)\.(?:25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[1-9][0-9]|[1-9]|0)\.(?:25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[1-9][0-9]|[0-9])))(?:\:\d{1,5})?)(\/(?:(?:[a-zA-Z0-9\;\/\?\:\@\&\=\#\~\-\.\+\!\*\'\(\)\,\_])|(?:\%[a-fA-F0-9]{2}))*)?(?:\b|$)"

        urls = []
        matches = re.finditer(regex, text, re.UNICODE)
        for matchNum, match in enumerate(matches):
            urls.append(match.group())
        return urls

    def direct_message(self, text, recipients):
        if type(recipients) != type([]):
            recipients = [str(recipients)]
        recipient_users = '"",""'.join(str(r) for r in recipients)
        endpoint = 'direct_v2/threads/broadcast/text/'
        boundary = self.uuid
        bodies   = [
            {
                'type' : 'form-data',
                'name' : 'recipient_users',
                'data' : '[["{}"]]'.format(recipient_users),
            },
            {
                'type' : 'form-data',
                'name' : 'client_context',
                'data' : self.uuid,
            },
            {
                'type' : 'form-data',
                'name' : 'thread',
                'data' : '["0"]',
            }
        ]

        # Check if URLS are present in text

        urls = self.find_urls(text)

        print(len(urls))

        if(len(urls) >= 1):
            endpoint = 'direct_v2/threads/broadcast/link/'
            bodies.append({
                'type' : 'form-data',
                'name' : 'link_text',
                'data' : text or '',
            })
            bodies.append({
                'type' : 'form-data',
                'name' : 'link_urls',
                'data' : json.dumps(self.find_urls(text)),
            })
        else:
            bodies.append({
                'type' : 'form-data',
                'name' : 'text',
                'data' : text or '',
            })


        data = self.buildBody(bodies, boundary)
        self.s.headers.update (
            {
                'User-Agent' : self.USER_AGENT,
                'Proxy-Connection' : 'keep-alive',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'multipart/form-data; boundary={}'.format(boundary),
                'Accept-Language': 'en-en',
            }
        )
        #self.SendRequest(endpoint,post=data) #overwrites 'Content-type' header and boundary is missed
        response = self.s.post(self.API_URL + endpoint, data=data.encode('utf-8'))      # Added encoding for emoji support

        if response.status_code == 200:
            self.LastResponse = response
            self.LastJson = json.loads(response.text)
            return True
        else:
           # print ("Request return " + str(response.status_code) + " error!")
            # for debugging
            try:
                self.LastResponse = response
                self.LastJson = json.loads(response.text)
            except:
                pass
            return False

    def get_user_info(self, influencer_account):
        boundary = self.uuid
        self.s.headers.update (
            {
                'User-Agent' : self.USER_AGENT,
                'Proxy-Connection' : 'keep-alive',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'multipart/form-data; boundary={}'.format(boundary),
                'Accept-Language': 'en-en',
            }
        )
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query=" + influencer_account + "&count=1"
        return self.s.get(url)

def send_instagram_invitation(influencer_account, campaign_id, invitation_key):
    # username = 'Aifluencetest'
    # pwd = 'Aifluencepass123'

    username = 'naldokan318'
    pwd = 'Asdfg@123#'

    time.sleep(1)
    global InstagramInstance
    if InstagramInstance == None:
        InstagramInstance = CustomizedInstagramAPI(username, pwd)
        print('InstagramInstance-----------', InstagramInstance)
        InstagramInstance.login()

    API = InstagramInstance
    print('instance-----------', API)

    respJSON = API.get_user_info(influencer_account).json()

    print('------------------', respJSON)

    influencer_user_id = str(respJSON['users'][0].get("user").get("pk"))
    invitation_message = "Dear " + str(respJSON['users'][0].get("user").get("full_name")) + ",\n"
    invitation_message += "We invite you to the marketing campaign you'd be interested in.\n"
    invitation_message += "Please signup our platform using below url:\n"
    invitation_message += "https://aifluenceplatform.com/" + "invitations/" + invitation_key
    res = API.direct_message(invitation_message, [influencer_user_id])


    return res

def send_invitation(influencer_account, influencer_platform, campaign_id, invitation_key):
    res = False
    if influencer_platform == "IN":
        res = send_instagram_invitation(influencer_account, campaign_id, invitation_key)
    return res


