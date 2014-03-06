import random

def parse_data(train_file):
    # parse date into array format
    x = []
    y = []
    for line in open(train_file):
        a = line.strip().split()
        b = [float(i) for i in a]
        x.append([-1] + b[:-1])
        y.append(b[-1])
    return x,y

def PLA_naive_cycle(x, y, w0=0, u=1):

    still_mistake = True
    update_times = 0
    w1 = w0

    while still_mistake:
        still_mistake = False
        for i in range(len(x)):
            modi = sum([ w1[j] * x[i][j] for j in range(len(w1))])
            if modi == 0 and y[i] == -1:
                continue
            if modi * y[i] > 0:
                continue
            else:
                w1 = [w1[j] + u * y[i] * x[i][j] for j in range(len(w1))]
                
                update_times += 1
                still_mistake = True

    return update_times, w1

def pocket_pla(x, y, w0, update_times):
    iter_times = 0
    w2 = w0
    w1 = w0
    sequence = range(len(x))
    
    while iter_times < update_times:
        iter_times += 1
        print iter_times
        random.shuffle(sequence)


        for i in sequence:
            modi = sum([ w1[j] * x[i][j] for j in range(len(w1))])

            if modi == 0 and y[i] == -1:
                continue
            if modi * y[i] > 0:
                continue
            else:
                print i, y[i]
                w2 = [w1[j] + y[i] * x[i][j] for j in range(len(w1))]
                print w1, w2
                
                y1 =  [ sum([ w1[j] * m[j] for j in range(len(w1))]) for m in x ]
                y2 =  [ sum([ w2[j] * m[j] for j in range(len(w2))]) for m in x ]

                count_y1 = sum( [ 1 for i in range(len(y1)) if (y[i]==-1 and y1[i] == 0) or y1[i]*y[i]>0] )
               
                count_y2 = sum( [ 1 for i in range(len(y2)) if (y[i]==-1 and y2[i] == 0) or y2[i]*y[i]>0] )
                
                if count_y1 >= count_y2:
                    
                    print count_y1, count_y2
                    print "not change"
                    break
                else:
                    w1 = w2
                    print "change"
                    break
    return w1

def hw1_15_17():
    # hw 1  15-17

    x, y = parse_data("hw1_16_train.dat")

    w0 = [0,0,0,0,0]
    u = 0.5

    update_times, learned_w = PLA_naive_cycle(x, y, w0, u)

    print "update_times is :" + str(update_times)
    print learned_w

    

def hw1_18_20():   
    # hw 1 18-20

    x_train, y_train = parse_data("hw1_18_train.dat")
    x_test, y_test = parse_data("hw1_18_test.dat")

    # print len(y_train), sum(y_train)
    w0 = [-1.0, -0.153722, -0.25810999999999995, 0.67295, 0.69363]
    update_times = 50
    w = pocket_pla(x_train, y_train, w0, update_times)
    print w

def main():
    hw1_15_17()



if __name__ == "__main__":
    main()
    
