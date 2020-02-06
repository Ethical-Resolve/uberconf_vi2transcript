import sys
import os
import csv
import datetime
import io
def hms_2_sec(t):
    h, m, s = [int(float(i)) for i in t.split(":")]
    return 3600*h + 60*m + s
file = input("Enter file path")
transcript_output = open(file + ".txt", "w")
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    firstline = next(csvreader)
    start = firstline[0].split(" ")[1]
    start = hms_2_sec(start)
    for row in csvreader:
        time = row[0].split(" ")[1]
        speaker = row[2]
        content = row[5]
        elapsed_seconds = hms_2_sec(time) - start
        timecode = str(datetime.timedelta(seconds=elapsed_seconds))
        transcript_output.write(timecode +"\n" + speaker + "\n" + content + "\n" + "\n")
