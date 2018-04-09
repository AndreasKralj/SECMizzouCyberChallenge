#!/bin/bash

tail -n 1 example.log > tmp.log #Get the last line of the log file
awk '{print $2}' tmp.log > temp.log #Get the time
awk '{print $3}' tmp.log > temp2.log #Get the error specification
RES_TIME=$(awk -F: '{print $1}' temp.log)
RES_ERROR=$(awk -F: '{print $1}' temp2.log)
#echo $RES_TIME
#echo $RES_ERROR
#echo $RES | awk --field-separator=" " "{ print NF}"
for i in $RES_TIME
do
        if [ $i -lt 8 ] || [ $i -gt 17 ]; then
                if [ $RES_ERROR == 'ERROR' ] || [ $RES_ERROR == 'WARNING' ] || [ $RES_ERROR == 'DEBUG' ]; then
                        echo "Sending log email!"
                        ssmtp ankwdf@mail.missouri.edu < testfile
                fi
        fi
done
rm -f temp.log
