#! /usr/bin/env python

#This script copies all sensative browser data inlcuding;
#Cookies, Bookmarks, History...etc.

import subprocess
import shutil
import os
import sys
import fnmatch
import platform

def find_browser_files(cur_op_sys):

	if cur_op_sys == "Windows":
		rel = platform.release()
		print("Using: "+cur_op_sys+" "+rel+"\n")
		print("")
		home_dir = 'C:/'
	else:
		reltwo = platform.release()
		print("Using: "+cur_op_sys+" "+reltwo+"\n")
		home_dir = '/'

	search_files = '*.sqlite'
	file_names = []

	print("Locating All Browser Files On System...")
	print("This May Take A While...Please Wait...")

	for path, directories, sysfiles in os.walk(home_dir):
		for fileName in sysfiles:
			if fnmatch.fnmatch(fileName, search_files):
				file_names.append(os.path.join(path, fileName))

	if not file_names:
		print("No Browser Files Could Be Found..")
		print("Exiting...")
		sys.exit(1)
	else:
		print("Browser Files Found!\n")
		print("")
		return file_names

def copy_files(list_of_files):

	path_name = raw_input("Please Enter Full Path To Save Destination: ")
	print("")
	print("Will Now Copy Files To: "+path_name)

	if not os.path.exists(path_name):
		print("Specified Path Does Not Exist.")
		print("Creating Path...")
		os.mkdir(path_name)
		
	
	for file_path in list_of_files:
		shutil.copy(file_path, path_name)

	if os.listdir(path_name) != []:
		print("\nCopied Browser Files Are Now In The Directory: "+path_name)
		print("Thank You For Using GFInfo!")
		sys.exit(0)
	else:
		print("There Was A Problem Copying The Files.")
		print("Exiting...")
		sys.exit(1)
	

print("Welcome to GBInfo...\n")
op_sys = platform.system()
file_list = find_browser_files(op_sys)
copy_files(file_list)
