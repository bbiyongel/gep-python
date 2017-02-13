def gep3Rt(x):
    if x < 0.0:
        return -pow(-x, (1.0/3.0))
    else:
        return pow(x, (1.0/3.0))

if __name__ == '__main__':
    element = [281302314, 292100226.35502815]
    var = [-12.044035396896772, 81.49352027660869, 1.7598475530044397, 15.389723395785193, -20.45039560319437, 47.12173285508684, -83.13551165256523, 2.411310207227713, -39.4772926117209, 16.500237600355284, 5.775191656507074, 22.536319798961078, -2.3472218948080297]

    y = (((max(element[0],element[1])+(element[1]+element[0]))/2.0)+(pow(var[0],3.0)*pow(var[0],4.0)))
    y = (y + gep3Rt(((pow(var[1],5.0)*(element[0]*element[0]))-pow((element[1]-element[0]),3.0)))) / 2.0
    y = (y + (((var[2]*var[2])*(var[3]*var[3]))-((element[0]/var[4])+(var[5]-element[0])))) / 2.0
    y = (y + (((var[6]+element[1])-(element[0]*var[7]))+(max(var[8],var[9])*pow(var[10],5.0)))) / 2.0
    y = (y + max(((element[0]+element[0])+pow(var[11],5.0)),((element[1]+var[12])+min(element[1],element[1])))) / 2.0

    print(y)