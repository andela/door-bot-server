import json
import requests
import time

t = 0

def get_url():
  try:
    req=requests.get("http://127.0.0.1:4040/api/tunnels", headers={"content-type":"application/json"});
  except Exception, e:
    print e
    retry()
  else:
    if req.status_code == 200:
      obj = json.loads(req.content)
      if obj['tunnels'] and obj['tunnels'][0]:
        report_url(obj['tunnels'][0]['public_url'])
      else:
        retry()
    else:
     retry()


def retry():
  global t
  t = t + 5
  print "ngrok unavailable retrying in " + str(t) + " seconds"
  time.sleep(t)
  get_url()

def report_url(url_str):
  if url_str:
    payload = '{"ngrokURL":  "%s"}' % url_str + '/open/'
    print "Saving to Firebase: " + payload
    try:
      req = requests.put("https://doorbot.firebaseio.com/settings.json", data=payload)
    except Exception, e:
      print e
      retry()
    else:
      result = req.content
      status_code = req.status_code
      if req.status_code  == 200:
        print "\n\nDone: Status: %s\n%s" % (status_code, result)
      else:
        print "\n\nError: Status: %s\n%s" + (status_code, result)
  else:
    print "Malformed URL"
    retry()

get_url()