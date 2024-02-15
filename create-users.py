#!/usr/bin/python <- This may need to change depending on your system
import os
import re
import sys

def main():
	for line in sys.stdin:

        match = re.match('#', line)

		fields = line.strip().split(':') #strip any whitespace and split into 
         if match or len(fields) != 5:
# The line above ensures that lines starting with a # and lines without 5 fields are skipped in the loop
            continue
		username = fields[0]
		password = fields[1]

		gecos    = "%s %s,,," % (fields[3],fields[2])

		groups   = fields[4].split(',') #This splits the fifth field (groups) into a list based on commas.

		print "==> Creating account for %s..." % (username))
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
		#print cmd
		os.system(cmd)  #It runs the command
		print "==> Setting the password for %s..." % (username)
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
		#print cmd
		os.system(cmd)
		for group in groups: #It iterated through the list of groups and assignes the user to each group.
			if group != '-':
			    print "==> Assigning %s to the %s group..." % (username,group)
			    cmd = "/usr/sbin/adduser %s %s" % (username,group)
			    #print cmd
			    os.system(cmd)


if __name__ == '__main__':  #remember to use double underlines here
	main()


