import argparse
import math
import pathlib
import shutil
import sys
import rdams_client as rc
from time import sleep
import re

status = rc.get_status()

for elem in status['data']:
  request_index = str(elem['request_index'])
  rc.purge_request(request_index)
  
