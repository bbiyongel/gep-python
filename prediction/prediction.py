from os import path
import math

d = []


def get_data(embed):
    global d
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

    output = list(map(int, output))
    d = output[:embed]

    return output


def formula(var, embed, i):
    global d
    element = d[i:embed]
    y = (((max(element[0],element[1])+(element[1]+element[0]))/2.0)+(pow(var[0],3.0)*pow(var[0],4.0)))
    y = (y + gep3Rt(((pow(var[1],5.0)*(element[0]*element[0]))-pow((element[1]-element[0]),3.0)))) / 2.0
    y = (y + (((var[2]*var[2])*(var[3]*var[3]))-((element[0]/var[4])+(var[5]-element[0])))) / 2.0
    y = (y + (((var[6]+element[1])-(element[0]*var[7]))+(max(var[8],var[9])*pow(var[10],5.0)))) / 2.0
    y = (y + max(((element[0]+element[0])+pow(var[11],5.0)),((element[1]+var[12])+min(element[1],element[1])))) / 2.0

    d.append(y)


def gep3Rt(x):
    if x < 0.0:
        return -pow(-x, (1.0/3.0))
    else:
        return pow(x, (1.0/3.0))


def prediction(var, embed):
    global d
    d = []
    optimal_rmse = 0
    i = 0
    del_embed = embed

    actual_data = get_data(embed)

    while embed < 25:
        formula(var, embed, i)
        i += 1
        embed += 1

    for i in range(0, del_embed):
        del d[i]
        del actual_data[i]

    for i in range(0, len(d)):
        optimal_rmse += math.pow(float(actual_data[i]) - float(d[i]), 2)

    optimal_rmse /= len(d)
    optimal_rmse = math.sqrt(optimal_rmse)

    return optimal_rmse
