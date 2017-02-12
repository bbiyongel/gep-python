from os import path
import math
import csv


def get_data(embed):
    script_row = []
    script_output = []
    output = []
    script_file = open(path.abspath("TimeSeries(GRDP).csv"), 'r')

    for line in script_file:
        script_row.append(line.strip('\n'))
    for i in range(1, len(script_row)):
        script_output.append(script_row[i].split(','))
    for i in range(0, len(script_output)):
        output.append(script_output[i][2])

    d = output[len(output) - embed:]
    d = list(map(int, d))

    return d


def formula(var, d):
    y = (d[5] + (((1.0 - d[5]) * math.atan(d[4])) +
                    ((d[8] * var[0]) + ((d[9] + d[9]) / 2.0))))

    y += (d[4] * ((((((d[0] + d[12]) / 2.0) - d[6]) + d[3]) / 2.0) *
                     (((var[1] + var[2]) / 2.0) - math.atan(d[13]))))

    y += (((d[7] * (d[0] - (d[1] - d[10]))) +
           (1.0 - ((d[4] + (d[1] + d[10])) / 2.0))) / 2.0)

    y += (d[0] - d[0])
    y += (d[0] - d[0])

    return y


def write_data():
    fields = [25, 2009, 281302314]
    fd = open(path.abspath("TimeSeries(GRDP).csv"), 'a')
    writer = csv.writer(fd)
    writer.writerow(fields)
