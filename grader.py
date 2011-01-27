#!/usr/bin/env python

"""
!grader.py

Created by Chengyin Liu on 2011-01-26.
"""

import sys
import os
import glob
import subprocess

def __input_number(prompt = "> "):
  while True:
    feedback = raw_input(prompt)
    if feedback == "":
      return
    try:
      feedback = int(feedback)
    except:
      print "Error: %s is not an interger" % (feedback)
    else:
      return feedback

def main(argv=None):
  path = './'
  for file in glob.glob(os.path.join(path, '*.pdf')):
    meta_str = file.split('-')
    if len(meta_str) == 6:
      print "Processing %s" % (file)
      
      # OTHER PROCESS 
      if os.name == 'mac':
        p = subprocess.call("open \"%s\"" % file, shell=True)
      elif os.name == 'nt':
        p = subprocess.call("start \"\" \"%s\"" % file, shell=True)
      elif os.name == 'posix':
        p = subprocess.call("xdg-open \"%s\"" % file, shell=True)
      # FINISH OTHER PROCESS
      
      feedback_A = __input_number("Points earned WITHOUT IDK rule ([ENTER] w/o input to cancel): ")
      if not feedback_A is None:
        feedback_B = __input_number("Points earned FROM IDK rule ([ENTER] w/o input to cancel): ")
        if not feedback_B is None:
          new_name_parts = file.split('.')
          new_name_parts[len(new_name_parts)-2] += '-' + str(feedback_A) + '-' + str(feedback_B)
          new_name = ".".join(new_name_parts)
          os.rename(file, new_name)
          print "[Rename] %s -> %s" % (file, new_name)
          continue
      
      print 'Cancelled processing %s' % (file)
          
if __name__ == '__main__':
    sys.exit(main())

