import random, time, requests
from twython import Twython
requests.packages.urllib3.disable_warnings()

APP_KEY = 'YOUR APP KEY'
APP_SECRET = 'YOUR APP SECRET'
OAUTH_TOKEN = 'YOUR TOKEN'  # Access Token here
OAUTH_TOKEN_SECRET = 'YOUR SECRET'  # Access Token Secret here

def confirm(prompt=None, resp=False):
    if prompt is None:
        prompt = 'Confirm'

    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')
        
    while True:
        ans = raw_input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print 'please enter y or n.'
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False

def random_line(afile):
    line = next(afile)
    index = 0
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue
        line = aline
    return line.strip()

tweetCancelled = ['cancelled ya bish\n', 'no tweets here\n', 'de-tweeted\n', "won't see the light of day\n", 'death 2 all tweets\n']
tweetTweeted = ['ay tweeted\n', "it's in the cloud now\n", "ok, you're a tweetmonger\n", "i guess if you want\n", "sent against my better judgement\n"]

print 'WELCOME TO THE TWITTERDOME'

while True:
    tweetline=random_line(open('./output.txt'))
    if len (tweetline) > 140:
        print "tweet's too fuckin big, don't do it"
        print 'here it is anyways: "' + tweetline + '"\n'
    else:
        if confirm(prompt='tweet "' + tweetline + '" or nah?', resp=True):
            twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
            twitter.update_status(status=tweetline)
            print(random.choice(tweetTweeted))
        else:
            print(random.choice(tweetCancelled))
