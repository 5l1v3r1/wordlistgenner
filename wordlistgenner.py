#!/usr/bin/env python
#
# Wordlist generator
# pre-engagement tool
# 2020 Douglas Berdeaux
#
#
import sys
import os
import re
import time
# EDIT these to your fancy:
min_word_len = 6
print " ** Wordlist Generator ** \n"
def usage():
	print "\nUsage: ./wordlist_gen.py (TARGET_WEBSITE_URL)\n"
if len(sys.argv) != 2:
	usage()
	sys.exit()
else:
	print "[*] Target: "+sys.argv[1]
	print "[*] Starting initial scan, this may take a while ... "
	log_file = re.sub('https?...([a-z.]+).*',r'\1',sys.argv[1]) + "_" + str(time.time()) # the 'r' is required. Poor syntax.
	print "[*] Log file: "+log_file
	# Open all files:
	lfh = open(log_file+".txt",'w') # open log file for writing and assign a file handle
	lfh_2020 = open(log_file+"_2020.txt","w") # new file with 2020 appended to each line
	lfh_2019 = open(log_file+"_2019.txt","w")
	lfh_123 = open(log_file+"_123.txt","w")
	lfh_123_exclam = open(log_file+"_123_exclam.txt","w")

	# run CeWL:
	with os.popen("cewl -m "+str(min_word_len)+" "+sys.argv[1]+" | sort -u") as pipe: # open pipe
		for word in pipe:
			lfh.write(word)
			lfh_2020.write(word.strip() + "2020\n")
			lfh_2019.write(word.strip()+"2019\n")
			lfh_123.write(word.strip()+"123\n")
			lfh_123_exclam.write(word.strip()+"123!\n")
	# Close all files:
	lfh_2019.close()
	lfh_123.close()
	lfh_123_exclam.close()
	lfh.close() # and finally we close the master word list.
