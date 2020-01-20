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
	lfh = open(log_file+".txt",'w') # open log file for writing and assign a file handle
	# run CeWL:
	with os.popen("cewl -m "+str(min_word_len)+" "+sys.argv[1]+" | sort -u") as pipe: # open pipe
		for word in pipe:
			lfh.write(word)
	lfh.close() # close the original file and ensure the writes.
	print "[*] Completed target scan."
	print "[*] Generating mangled lists ... "
	lfh = open(log_file+".txt","r") # re-open the original file as "read only"
	lfh_2020 = open(log_file+"_2020.txt","w") # new file with 2020 appended to each line
	for word in lfh.readlines():
		lfh_2020.write(word.strip() + "2020\n")
	lfh.seek(0) # rewind file back to byte 0
	lfh_2020.close() # close this file
	lfh_2019 = open(log_file+"_2019.txt","w")
	for word in lfh.readlines():
		lfh_2019.write(word.strip()+"2019\n")
	lfh_2019.close()
	lfh.seek(0) # rewind file back to byte 0
	lfh_123 = open(log_file+"_123.txt","w")
	for word in lfh.readlines():
		lfh_123.write(word.strip()+"123\n")
	lfh_123.close()
	lfh.seek(0)
	lfh_123_exclam = open(log_file+"_123_exclam","w")
	for word in lfh.readlines():
		lfh_123_exclam.write(word.strip()+"123!\n")
	lfh_123_exclam.close()
	lfh.close() # and finally we close the master word list.
