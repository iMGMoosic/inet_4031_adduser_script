#### Lief Johnson
#### Add Users to Linux
#### Program Creation Date: 2024-11-03
#### Program Last Updated Date: 2024-11-03

#!/usr/bin/python3

# os is imported to run the commands generate
# re is imported for regex matching for integrity
# sys is imported to use stdin buffer
import os
import re
import sys

def main():
    for line in sys.stdin:

        # ^# is an expression that checks the start of a line for the '#' character. True if it matches, false otherwise
        match = re.match("^#",line)

        # Strip the whitespace from the line and split into a list using ':' as a delimiter
        fields = line.strip().split(':')

        # if the line started with '#' or doesn't have enough fields, we skip it and take the next line in stdin
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print(cmd)
        os.system(cmd)
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print(cmd)
        os.system(cmd)

        for group in groups:
            # to denote no group, we use '-' in the input file. this checks if we've done so and skips assignment if so
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
