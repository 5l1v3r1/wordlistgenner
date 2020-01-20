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
	print "\nUsage: ./wordlistgenner.py (TARGET_WEBSITE_URL)\n"
if len(sys.argv) != 2:
	usage()
	sys.exit()
else:
	print "[*] Target URL: "+sys.argv[1]
	print "[*] Starting CeWL- this may take a while ... "
	log_file = re.sub('https?...([a-z.]+).*',r'\1',sys.argv[1]) # the 'r' is required. Poor syntax.
	os.mkdir(log_file) # make the directory of the domain name to put everything into.
	log_file = log_file + "/"
	print "[*] Log files will start with: "+'"'+log_file+'"'
	# Open all files:
	lfh = open(log_file+".txt",'w') # open log file for writing and assign a file handle
	lfh_2020 = open(log_file+"2020.txt","w") # new file with 2020 appended to each line
	lfh_2019 = open(log_file+"2019.txt","w")
	lfh_123 = open(log_file+"123.txt","w")
	lfh_123_exclam = open(log_file+"123_exclam.txt","w")
	lfh_exclam = open(log_file+"exclam.txt","w")
	lfh_lower_capitalized = open(log_file+"lower_capitalized.txt","w")
	lfh_lower_capitalized_exclam = open(log_file+"lower_capitalized_exclam.txt","w")
	lfh_double = open(log_file+"double_word.txt","w")

	# run CeWL:
	with os.popen("cewl -m "+str(min_word_len)+" "+sys.argv[1]+" | sort -u") as pipe: # open pipe
		for word in pipe:
			lfh.write(word)
			lfh_2020.write(word.strip() + "2020\n")
			lfh_2019.write(word.strip()+"2019\n")
			lfh_123.write(word.strip()+"123\n")
			lfh_123_exclam.write(word.strip()+"123!\n")
			lfh_exclam.write(word.strip()+"!\n")
			lfh_lower_capitalized.write((word.strip()).capitalize()+"\n")
			lfh_lower_capitalized_exclam.write((word.strip()).capitalize()+"!\n")
			lfh_double.write(word.strip()+word.strip()+"\n")

	# Close all files:
	lfh_2020.close()
	lfh_2019.close()
	lfh_123.close()
	lfh_123_exclam.close()
	lfh_lower_capitalized.close()
	lfh_lower_capitalized_exclam.close()
	lfh_exclam.close()
	lfh_double.close()
	lfh.close() # and finally we close the master word list.
