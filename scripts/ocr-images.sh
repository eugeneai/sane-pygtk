#!/bin/bash

tmp=tmp.bmp

echo $1

for file in *$1
do
    echo $file
    convert $file -define bmp:format=bmp3 $tmp
    bn=$(basename $file)
    cuneiform -l ruseng -f hocr -o $bn.html $tmp
done
rm -f $tmp
