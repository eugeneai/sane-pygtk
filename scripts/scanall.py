#!/usr/bin/python
import sys

prg=sys.argv[0]
info="""
Running the program
%s <first_page_number>

E.g.:
%s 0
Starts scan from page 0.
""" % (prg,prg)

rotate=""
rotate="-rotate 90"


try:
    i=int(sys.argv[1])
except (ValueError, IndexError):
    print info
    raise SystemExit, "Program exiting."

nocolor=[
    "scanimage --format tiff --mode LineArt -d snapscan:libusb:%(s0)s:%(s1)s --resolution 300 -y 290 -x 200 > tmp.tiff",
    "convert tmp.tiff %s tmp1.tiff" % rotate,
    "cjb2 tmp1.tiff -clean %(fname)s.djvu",
    "rm tmp*.tiff",
]
color=[
    "scanimage --format tiff --mode color -d snapscan:libusb:%(s0)s:%(s1)s --resolution 300 -y 290 -x 200 > tmp.tiff",
    "convert tmp.tiff %s tmp1.tiff" % rotate,
    "cjb2 tmp1.tiff -clean %(fname)s.djvu",
    "rm tmp*.tiff",
]

pref="img"

d={}

import os
while i < 10000:
    ans=raw_input("Scanning page N '%i'.\n Press the <Enter> key or <ctrl>-<c> to stop scanning or press \"c\" for color page \n >" % i)
    color=0
    if ans.startswith('c'):
	print "!!!! Color scan !!!\n"
	color=1
    os.system("scanimage -L | grep usb > _")
    s=file("_").read().strip()
    s=s.split(":")[2:4]
    s0,s1=s
    s1=s1.split("'")[0]
    d={"s0":s0, "s1":s1}
    suff=""
    cmds=nocolor
    if color:
	suff="-color"
	cmds=color
    fname=( ("scan%04i"+suff) % i)
    d['fname']=fname
    # print d
    for cmd in cmds:
	try:
	    cmd_i=cmd % d
	except TypeError:
	    cmd_i=cmd
	print cmd_i
	os.system(cmd_i) 
    i+=1
    