#! /usr/bin/env python

import sys
import fileinput

#Lines containing these words will be deleted
switch_words = ['No.', 'Frame', 'Ethernet', 'Data', 'Authentication', 'Discover', 'Protocol', 'Format', 'Logical', 'Key', 'Solicitation', 'Who', 'Report', 'Transaction', 'Standard', 'Destination', 'Secure', 'Request', 'Encrypted', 'Client', 'Domain', 'Server', 'TCP', 'ACK', 'Segments', 'ARP', 'HTTP', 'Certificate', 'QUIC', 'Bootstrap', 'Data', 'Control', 'EAPOL', 'Application', 'User', 'Datagram', 'Port', 'SYN', 'data', 'text']

#If These Words Are In a Line, Next Line Will Be Newline
newline_words = ['Data', 'Logical-Link', 'Authentication', 'request', 'v6', 'v4']

#Setting variable to number of arguments
numargs = len(sys.argv) - 1


if (numargs == 2):
	#Set path variables
	ascii = sys.argv[1]
	writefile = sys.argv[2]

	#Open ascii file for reading, and new file for writing
	with open(ascii) as asciifile, open(writefile, 'w') as newascii:
		for line in asciifile:
			#Keep only the lines that do not contain words from 'switch_words'
			if not any(switch_words in line for switch_words in switch_words):
				#Print those lines to file
				newascii.write(line)
		#Take newly written file and take out all blank lines
		for line in fileinput.FileInput(writefile,inplace=1):
			if line.rstrip():
				print line,

	newascii.close()
	asciifile.close()

if (numargs == 3):

	#Set path variables
        ascii = sys.argv[1]
        writefile = sys.argv[2]

        #Open ascii file for reading, and new file for writing
        with open(ascii) as asciifile, open(writefile, 'w') as newascii:
                for line in asciifile:
			#Keep Only Lines That Contain Words From 'switch_words'
                        if any(switch_words in line for switch_words in switch_words):
				#Print Those Lines to New File
                                newascii.write(line)
			#Add Newline After any Line Containing Words From 'newline_words'
			if any(newline_words in line for newline_words in newline_words):
				newascii.write('\n')
	newascii.close()
	asciifile.close()
