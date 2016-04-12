#!/usr/bin/python2
# Author Hank Wagner
# Twitter nulledwizard
# GitHub lolwtfbbq
# License WTFPL
# Version 1 (April 11, 2016)

import os, sys, random, base64, requests, json
from base64 import b64encode

apikey = 'YOUR_KEY'
clientkey = 'YOUR_KEY'
savedir = '/tmp/'

try:
    randname = '' . join(random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(random.randint(4, 25))) + '.png'
    fname = savedir + randname

    os.system("scrot -s " + fname)
    print "{!} Saved Image " + fname

    req = requests.post(
        "https://api.imgur.com/3/upload.json",
        headers = {"Authorization": "Client-ID " + clientkey},
        data = {
            "key": apikey,
            "image": b64encode(open(fname, "rb").read()),
            "type": "base64",
            "name": randname,
            "title": "Picture " + randname
        }
    )
    print "{!} Uploaded Image to Imgur " + fname

    imgurlink = json.loads(req.text)["data"]["link"]
    os.system("echo " + imgurlink + " | xsel -b")

    print "{!} Copied Imgur link to clipboard " + imgurlink
except Exception, e:
    print "{!!!} Failed! Contact the developer!" + str(e)
