#!/bin/bash 

FLASKPID=`ps -ef | grep -v grep | grep flask | awk '{print $2}'`
echo $FLASKPID
kill $FLASKPID 
