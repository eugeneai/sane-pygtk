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


try:
    i=int(sys.argv[1])
except (ValueError, IndexError):
    print info
    raise SystemExit, "Program exiting."

nocolor=[
    "scanimage --format tiff --mode LineArt -d snapscan:libusb:%(s0)s:%(s1)s --resolution 300 -y 240 -x 170 > tmp.tiff",
    "cjb2 tmp.tiff -clean %(fname)s.djvu",
    "rm tmp*.tiff",
]
colorcmds=[
    "scanimage --format pnm --mode Color -d snapscan:libusb:%(s0)s:%(s1)s --resolution 300 -y 240 -x 170 > %(fname)s.pnm",
    "c44 %(fname)s.pnm",
    "rm %(fname)s.pnm",
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
    elif ans.startswith('b'):
	print "!!!! B&W scan !!!\n"
	color=0
    else:
	print "Unknown scan!!!!"
	continue
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
	cmds=colorcmds
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
    