import os
from datetime import datetime


#  change threshhold to 7 minutes
def check_update():
  now = datetime.strptime(str(datetime.now()).split(' ')[0], '%Y-%m-%d')
  with open('./update.py', 'r') as f:
    text = f.read()
    comment = text.split('\n')[0]
    timestamp = datetime.strptime(comment.split('|')[1].strip(), '%Y-%m-%d')

    if timestamp < now:
      print(f'The repository has not been updated since {str(timestamp)}. Please run update.py on the day of merging the branch.')
      assert False

check_update()