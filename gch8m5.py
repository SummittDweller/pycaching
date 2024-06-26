# gch8m5.py
#

import os
import time
import csv 
import json
from pprint import pprint
from datetime import datetime, timedelta

# Add local project root ot sys.path so local modules are used
# Per https://fortierq.github.io/python-import/
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)

# Local packages
# import constant as c
# import func as f
import pycaching

##-----------------------------------------------------------------------------------------
## gch8m5.py
##

#--------------------------------------------------------------------------
# Login
geocaching = pycaching.login( )  # assume the .gc_credentials file is presented

#--------------------------------------------------------------------------
# Open our target cache listing
cache = geocaching.get_cache("GCH8M5")
print(cache.name)      # cache.load( ) is automatically called
print(cache.location)  # stored in cache, printed immediately

#---------------------------------------------------------------------------
# Read the data and write to a .csv file

field_names = ['_uuid', '_author', '_visited', '_type', 'membership', 'log_image', '_text'] 

with open('gch8m5_logs.csv', 'w') as csvfile: 
  writer = csv.DictWriter(csvfile, fieldnames = field_names) 
  writer.writeheader( ) 
	# writer.writerows(cars) 

  for log in cache.load_logbook(limit=2000):
    obj_vars = vars(log)
    writer.writerow(obj_vars)





# #--------------------------------------------------------------------------
# # Open a logs.json file and write log data to it...
# with open('gch8m5_logs.json', 'w') as json_file: 

#   #------------------------------------------------------------------------
#   # Get the log entries...
#   for log in cache.load_logbook(limit=2000):
#     obj_vars = vars(log)
#     pprint(obj_vars)
#     # print(log.visited, log.type, log.author, log.text)
#     # print(log.uuid)
    
#     #----------------------------------------------------------------------
#     # Dump the log details as json
#     json_file.write(str(obj_vars))
#     json_file.write("\n")
#     # json_file.write(json.dumps(obj_vars))
