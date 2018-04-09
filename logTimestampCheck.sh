#!/bin/bash
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
