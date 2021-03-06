#!/usr/bin/env python3
# Author: Francis Sy

# NOTE: When initially prompted with 'bad credential error', just follow this
# link to allow 3rd party access to gmail account: https://support.google.com/accounts/answer/6010255

import smtplib
import sys
from getpass import getpass

if __name__ == '__main__':
    # DEBUGGING
    # for i, j in enumerate(sys.argv):
        # print("sys.argv[%d]" % i, j)

    # check to see that there are argument flags
    if len(sys.argv) != 4:
        print("Error: no or missing flags\nexit(-1)")
        exit(-1)

    # obtain password: hide keylog
    password = str(getpass("Please enter account password: "))

    # create a SMTP session and start tls for security
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    # login authentication
    s.login(str(sys.argv[1]), password)

    message = str(input("Input message: "))

    # loop send the mail
    send_message = message # initial
    for i in range(int(sys.argv[3])):
        send_message += str(i+1)
        s.sendmail(sys.argv[1], sys.argv[2], send_message)
        send_message = message # reset

    s.quit() # quit
