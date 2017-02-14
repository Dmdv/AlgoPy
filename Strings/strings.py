#!/usr/bin/env python

s = "udacityudacity"

test = s.find("ity")
print("Found location: {0}".format(test))

print("Opening the file extractor.log...")
file = open("extractor.log", "r")

str = file.read()
print("String length = {0}".format(len(str)))
pos = str.find("udacity")
print("Position = {0}".format(pos))

input("Press Enter to exit...")


