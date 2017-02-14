def gep3Rt(x):
    if x < 0.0:
        return -pow(-x, (1.0/3.0))
    else:
        return pow(x, (1.0/3.0))

if __name__ == '__main__':
    element = [279045512, 281302314]
    var = [5.219355308043999, 6.955211107944737, 47.273310771341585, 80.86404850836641, 19.738063453502548, 5.281304907097628, 28.35940238883633, 1.883494110264678, 13.226945703104384, 98.92787793319971, 11.4855469677468, 3.414203041535899, 60.60839018909146]

    y = (((max(element[0],element[1])+(element[1]+element[0]))/2.0)+(pow(var[0],3.0)*pow(var[0],4.0)))
    y = (y + gep3Rt(((pow(var[1],5.0)*(element[0]*element[0]))-pow((element[1]-element[0]),3.0)))) / 2.0
    y = (y + (((var[2]*var[2])*(var[3]*var[3]))-((element[0]/var[4])+(var[5]-element[0])))) / 2.0
    y = (y + (((var[6]+element[1])-(element[0]*var[7]))+(max(var[8],var[9])*pow(var[10],5.0)))) / 2.0
    y = (y + max(((element[0]+element[0])+pow(var[11],5.0)),((element[1]+var[12])+min(element[1],element[1])))) / 2.0

    print(y)