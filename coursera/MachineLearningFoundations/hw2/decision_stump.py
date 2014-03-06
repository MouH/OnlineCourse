import random
import math

def generate_data(data_size):
    '''
    with the set data size, return a tuple of x,y
    '''

    # generate x
    x = [ random.uniform(-1,1) for i in range(0,data_size)]
    
    # generate y
    y = []
    for i in x:
        yi = 0
        if i > 0:
            yi = 1
        else:
            yi = -1

        flips = random.random()

        if flips < 0.2:
            yi = yi * -1
        y.append(yi)
    
    return x, y

def drange(start,stop,step):
    r = start
    while r <= stop:
        yield r
        r += step

def decision_stump(data_size):
    x, y = generate_data(data_size)

    # theta is between (-1,1)
    # s = 1 or -1
    result_theta1 = []
    e_in1 = 1

    for thetai in drange(-1,1,0.05):
        hx = [(xi - thetai) for xi in x]
        error_num = 0
        for i in range(data_size):
            h = hx[i] * y[i]
            if h < 0:
                error_num += 1
        error = error_num*1.0 / data_size
        # print thetai, error
        if error < e_in1:
            result_theta1 = [thetai]
            e_in1 = error
        elif error == e_in1:
            result_theta1.append(thetai)

    # print result_theta
    theta1 = result_theta1[len(result_theta1)/2]

    result_theta2 = []
    e_in2 = 1

    for thetai in drange(-1,1,0.05):
        hx = [(-xi + thetai) for xi in x]
        error_num = 0
        for i in range(data_size):
            h = hx[i] * y[i]
            if h < 0:
                error_num += 1
        error = error_num*1.0 / data_size
        # print thetai, error
        if error < e_in2:
            result_theta2 = [thetai]
            e_in2 = error
        elif error == e_in2:
            result_theta2.append(thetai)

    # print result_theta
    theta2 = result_theta2[len(result_theta2)/2]
    # print e_in1,e_in2
    # print theta1,theta2
    if e_in1 < e_in2:
        return e_in1, 1, theta1
    else:
        return e_in2, -1, theta2

def main():
    e_in_list = []
    e_out_list = []
    for i in range(5000):
        e_in, s, theta = decision_stump(10)
        e_in_list.append(e_in)

        e_out = 0.5 + 0.3 * s * ( math.fabs(theta) - 1 )
        e_out_list.append(e_out)
        
    avg_e_in = sum(e_in_list)*1.0 / len(e_in_list)
    avg_e_out = sum(e_out_list)*1.0 / len(e_out_list)
    print avg_e_in
    print avg_e_out


if __name__ == "__main__":
    main()
