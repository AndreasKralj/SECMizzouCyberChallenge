#!/bin/bash
#This script is used to check the timestamps in the log and automatically send an email if an action occurs before 8:00am and after 5:00pm.
awk '{print $2}' example.log > temp.log
RES=$(awk -F: '{print $1}' temp.log)
echo $RES | awk --field-separator=" " "{ print NF}"
for i in $RES
do
        if [ $i -lt 8 ] || [ $i -gt 17 ]; then
                echo "Sending log email!"
                ssmtp ankwdf@mail.missouri.edu < testfile

        fi
done
rm -f temp.log
