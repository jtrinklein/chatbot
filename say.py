#!/usr/bin/python

from subprocess import call


while True:
    with open('/home/ubuntu/sayio', 'r') as input:
        message = input.read()
        if message:
            msg = '"' + message + '"'
            print('> ' + msg)

            call(['espeak', '-ven+m2', '-a15', '-k5', '-s150', msg])
