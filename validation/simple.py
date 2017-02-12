def gep3Rt(x):
    if x < 0.0:
        return -pow(-x, (1.0/3.0))
    else:
        return pow(x, (1.0/3.0))

if __name__ == '__main__':
    element = [281302314, 292100226.35502815]
    var = [0.5, -39.79094706984965, 26.124753486432326, -37.990923056474514, -12.083442872530938, -34.70481139887839, 84.70952384970155, 1.8410407815910204, 61.780517311355254, 32.71718206757512, 14.950924850590155, 27.46239914460393, -63.96269468607023]

    y = (((max(element[0],element[1])+(element[1]+element[0]))/2.0)+(pow(var[0],3.0)*pow(var[0],4.0)))
    y = (y + gep3Rt(((pow(var[1],5.0)*(element[0]*element[0]))-pow((element[1]-element[0]),3.0)))) / 2.0
    y = (y + (((var[2]*var[2])*(var[3]*var[3]))-((element[0]/var[4])+(var[5]-element[0])))) / 2.0
    y = (y + (((var[6]+element[1])-(element[0]*var[7]))+(max(var[8],var[9])*pow(var[10],5.0)))) / 2.0
    y = (y + max(((element[0]+element[0])+pow(var[11],5.0)),((element[1]+var[12])+min(element[1],element[1])))) / 2.0

    print(y)