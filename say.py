#!/usr/bin/python

from subprocess import call


while True:
    with open('/home/ubuntu/sayio', 'r') as input:
        message = input.read()
        if message:
            print('> ' + message)
            call('espeak', ['-ven+m2','-k5', '-s150', '"' + message + '"'])

