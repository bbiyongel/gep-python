from os import path
import math

###########################
# From Training to Prediction
NUMBER_OF_ELEMENTS = 46
###########################
d = []


def get_data(starting_prediction):
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
    prediction_output = output[:starting_prediction]

    return prediction_output, output


def formula(actual_data, var, starting_prediction, embed):
    global d
    element = actual_data[starting_prediction - embed:starting_prediction]
    y = (((max(element[0],element[1])+(element[1]+element[0]))/2.0)+(pow(var[0],3.0)*pow(var[0],4.0)))
    y = (y + gep3Rt(((pow(var[1],5.0)*(element[0]*element[0]))-pow((element[1]-element[0]),3.0)))) / 2.0
    y = (y + (((var[2]*var[2])*(var[3]*var[3]))-((element[0]/var[4])+(var[5]-element[0])))) / 2.0
    y = (y + (((var[6]+element[1])-(element[0]*var[7]))+(max(var[8],var[9])*pow(var[10],5.0)))) / 2.0
    y = (y + max(((element[0]+element[0])+pow(var[11],5.0)),((element[1]+var[12])+min(element[1],element[1])))) / 2.0

    actual_data.append(y)
    d.append(y)


def gep3Rt(x):
    if x < 0.0:
        return -pow(-x, (1.0/3.0))
    else:
        return pow(x, (1.0/3.0))


def prediction(fitness, embed):
    global d
    d = []
    #########################
    starting_prediction = 25
    #########################

    actual_data = get_data(starting_prediction)[0]

    while starting_prediction < NUMBER_OF_ELEMENTS:
        formula(actual_data, fitness, starting_prediction, embed)
        starting_prediction += 1

    ########################
    starting_prediction = 25
    ########################
    actual_data = get_data(starting_prediction)[1]

    print("-----------------------5. Prediction-----------------------")
    for i in range(0, len(d)):
        print('{}년 : '.format(i + 2010), d[i])

    print("-----------------------6. Prediction Error-----------------------")
    for i in range(0, 6):
        print('{}년 : '.format(i + 2010), abs(((actual_data[i + 25] - d[i]) / actual_data[i + 25] * 100)))
