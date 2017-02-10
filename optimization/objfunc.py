from excel.excel import control_excel
import math


def calculate_fitness(var_list):
    optimal_fitness = 0
    optimal_rmse = 0
    optimal_mape = 0
    optimal_u = 0
    temp1 = 0
    temp2 = 0
    script_output = control_excel()

    elements = [0 for _ in range(14)]
    predict_data = [0 for _ in range(22)]
    actual_data = [0 for _ in range(22)]

    for i in range(1, 23):
        for j in range(1, 16):
            if j == 15:
                actual_data[i - 1] = script_output[i - 1][j]
            else:
                elements[j - 1] = float(script_output[i - 1][j])
        predict_data[i - 1] = function(var_list, elements)

    for i in range(0, 21):
        optimal_fitness += abs(float(actual_data[i]) - float(predict_data[i]))
        optimal_rmse += math.pow(float(actual_data[i]) - float(predict_data[i]), 2)
        optimal_mape += abs((float(actual_data[i]) - float(predict_data[i])) / float(actual_data[i]))
        temp1 = math.sqrt(math.pow(float(actual_data[i]), 2))
        temp2 = math.sqrt(math.pow(float(predict_data[i]), 2))

    optimal_rmse /= 22
    optimal_rmse = math.sqrt(optimal_rmse)

    optimal_mape /= 22
    optimal_mape *= 100

    temp1 /= 22
    temp1 = math.sqrt(temp1)
    temp2 /= 22
    temp2 = math.sqrt(temp2)

    optimal_u = optimal_rmse / (temp1 + temp2)

    return optimal_fitness, optimal_rmse, optimal_mape, optimal_u

"""
def function(var_list, elements):
    var0 = 0
    var1 = 0
    var2 = 0
    for var in var_list:
        var0 = var[0]
        var1 = var[1]
        var2 = var[2]

    y = (elements[5] + (((1.0 - elements[5]) * math.atan(elements[4])) +
                    ((elements[8] * var0) + ((elements[9] + elements[9]) / 2.0))))

    y += (elements[4] * ((((((elements[0] + elements[12]) / 2.0) - elements[6]) + elements[3]) / 2.0) *
                     (((var1 + var2) / 2.0) - math.atan(elements[13]))))

    y += (((elements[7] * (elements[0] - (elements[1] - elements[10]))) +
           (1.0 - ((elements[4] + (elements[1] + elements[10])) / 2.0))) / 2.0)

    y += (elements[0] - elements[0])
    y += (elements[0] - elements[0])

    return y
"""


def calculate_fitness(var, algorithm_type):
    optimal_fitness = 0
    optimal_rmse = 0
    optimal_mape = 0
    optimal_u = 0
    temp1 = 0
    temp2 = 0
    script_output = control_excel()

    elements = [0 for _ in range(14)]
    predict_data = [0 for _ in range(22)]
    actual_data = [0 for _ in range(22)]

    for i in range(1, 23):
        for j in range(1, 16):
            if j == 15:
                actual_data[i - 1] = script_output[i - 1][j]
            else:
                elements[j - 1] = float(script_output[i - 1][j])
        predict_data[i - 1] = function(var, elements, algorithm_type)

    for i in range(0, 21):
        optimal_fitness += abs(float(actual_data[i]) - float(predict_data[i]))
        optimal_rmse += math.pow(float(actual_data[i]) - float(predict_data[i]), 2)
        optimal_mape += abs((float(actual_data[i]) - float(predict_data[i])) / float(actual_data[i]))
        temp1 = math.sqrt(math.pow(float(actual_data[i]), 2))
        temp2 = math.sqrt(math.pow(float(predict_data[i]), 2))

    optimal_rmse /= 22
    optimal_rmse = math.sqrt(optimal_rmse)

    optimal_mape /= 22
    optimal_mape *= 100

    temp1 /= 22
    temp1 = math.sqrt(temp1)
    temp2 /= 22
    temp2 = math.sqrt(temp2)

    optimal_u = optimal_rmse / (temp1 + temp2)

    return optimal_fitness, optimal_rmse, optimal_mape, optimal_u


def function(var, elements, algorithm_type):
    if algorithm_type == 1:
        temp1 = 0
        temp2 = 0
        temp3 = 0
        for var_ in var:
            temp1 = var_[0]
            temp2 = var_[1]
            temp3 = var_[2]

        var = [temp1, temp2, temp3]

    y = (elements[5] + (((1.0 - elements[5]) * math.atan(elements[4])) +
                    ((elements[8] * var[0]) + ((elements[9] + elements[9]) / 2.0))))

    y += (elements[4] * ((((((elements[0] + elements[12]) / 2.0) - elements[6]) + elements[3]) / 2.0) *
                     (((var[1] + var[2]) / 2.0) - math.atan(elements[13]))))

    y += (((elements[7] * (elements[0] - (elements[1] - elements[10]))) +
           (1.0 - ((elements[4] + (elements[1] + elements[10])) / 2.0))) / 2.0)

    y += (elements[0] - elements[0])
    y += (elements[0] - elements[0])

    return y
