#!/usr/bin/env python
import subprocess
import paramiko
hostname = '192.168.1.101'
port = 22
username = 'root'
password = 'redhat'
t = paramiko.Transport((hostname, port))
t.connect(username = 'username', password = 'password')


def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print " Gathering system information with %s command:/n" %uname
    subprocess.call([uname, uname_arg])

def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print "Gsthering diskspace informatrion using %s command:/n" %diskspace
    subprocess.call([diskspace, diskspace_arg])
def main():
    uname_func()
    disk_func()

if __name__ == "__main__":
   main()

