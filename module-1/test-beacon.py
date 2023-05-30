# Usage
# `python test-beacon.py <BEACONURL> 10000 0.5`

import requests
import random
import sys
import argparse
import time

def getEvent():
  events = {
    0 : 'click',
    1 : 'pageview',
    2 : 'conversion',
    3 : 'exception',
    4 : 'playvideo',
    5 : 'login',
    6 : 'logoff'
  }
  return events[random.randint(0,6)]

def getPage():
  return f'page_{random.randint(1, 100)}.html'

def getUser():
  return f'user{random.randint(1, 1000)}' 

def getReferer():
  return f'referer_{random.randint(1, 20)}'

def getUserAgent():
  return f'python_manual_agent_{random.randint(1, 20)}'

def getIntMetricName():
  custom_metrics = {
    0 : 'page_load_time',
    1 : 'cart_item_quantity',
    2 : 'impression_count',
    3 : 'idle_time_ms',
    4 : 'mouse_distance_pixles'
  }
  return custom_metrics[random.randint(0,4)]

def getStringMetricName():
  custom_metrics = {
    0 : 'poll_response',
    1 : 'display_x_y',
    2 : 'blocker_type',
    3 : 'browser_version'
  }
  return custom_metrics[random.randint(0,3)]

def getFloatMetricName():
  custom_metrics = {
    0 : 'purchase_amount',
    1 : 'gpu_driver_version',
    2 : 'page_percent_displayed',
    3 : 'video_stopped_location',
    4 : 'compute_render_time'
  }
  return custom_metrics[random.randint(0,4)]

def getIntMetricValue():
  return str(random.randint(0,100))

def getFloatMetricValue():
  return str(random.random() * random.randint(0,100))

def getStringMetricValue():
  return f"dummy_string_value_{str(random.random() * random.randint(0, 10))}" 

parser = argparse.ArgumentParser()
parser.add_argument("target", help="<http...> the http(s) location to send the GET request")
parser.add_argument("calls", help="the number of HTTP calls to make")
parser.add_argument("delay", help="the time in seconds to delay between calls (ie 0.5 is half a second)")

args = parser.parse_args()
i = 0
s = requests.Session()

while (i < int(args.calls)):
  time.sleep(float(args.delay))
  random_metric = random.randint(0,3)
  if random_metric == 0:
    headers = {'event' : getEvent(), 'clientid' : getUser(), 'page' : getPage(), 'Referer' : getReferer() }
  elif random_metric == 1:
    headers = {'event' : getEvent(), 'clientid' : getUser(), 'page' : getPage(), 'Referer' : getReferer(), 'custom_metric_name' : getIntMetricName(), 'custom_metric_int_value' : getIntMetricValue() }
  elif random_metric == 2:
    headers = {'event' : getEvent(), 'clientid' : getUser(), 'page' : getPage(), 'Referer' : getReferer(), 'custom_metric_name' : getFloatMetricName(), 'custom_metric_float_value' : getFloatMetricValue() }
  elif random_metric == 3:
    headers = {'event' : getEvent(), 'clientid' : getUser(), 'page' : getPage(), 'Referer' : getReferer(), 'custom_metric_name' : getStringMetricName(), 'custom_metric_string_value' : getStringMetricValue() }
  r = s.post(f'{args.target}?call={i}', headers=headers)
  #r = requests.get(args.target)
  if (r.status_code==200):
    sys.stdout.write(f"{i}-")
  else:
    sys.stdout.write(f"{i}---->{r.status_code}" + "\n")
  sys.stdout.flush()
  i+=1
