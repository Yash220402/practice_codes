import os
from os import system as osys
import sys

import time

while True:
	osys("git add .")
	osys('git commit -m "update" ')
	osys("git branch -M main")
	osys("git push -u origin main")
	time.sleep(10)