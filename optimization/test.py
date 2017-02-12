from prediction.time_series import get_data
from prediction.time_series import formula
from prediction.time_series import write_data
from os import path

if __name__ == '__main__':
    d = get_data(14)
    list1 = [3.6, -3.2, 1.1]
    y = formula(list1, d)
    write_data()
