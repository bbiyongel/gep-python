from os import path


def control_excel():
    script_row = []
    script_output = []
    script_file = open(path.abspath("result(GEP).csv"), 'r')

    for line in script_file:
        script_row.append(line.strip('\n'))
    for i in range(1, len(script_row)):
        script_output.append(script_row[i].split(','))
    for i in range(0, len(script_output)):
        for j in range(0, len(script_output[i])):
            script_output[i][j] = script_output[i][j].strip()

    return script_output
