#! /usr/bin/python

__author__="Mou Hao <muhaocd@gmail.com>"
__date__ ="$Nov 6 2013"

gt_count = []

#read counts into a dict
f = file('gene.counts','r')
while True:
    line = f.readline()
    sss = [a for a in line.split(' ') if a != '']
    # print sss[3]
    if sss[1] == 'WORDTAG':
    	if int(sss[0]) > 4:
    	    gt_count.append(sss[3])
    	else:
    		continue
    else:
    	break

f.close
# print gt_count[1]
# print len(gt_count)

#read gene.train
f1 = file('gene.train','r')
f2 = file('gene.train.change', 'w')

while True:
    line = f1.readline():
    if len(line) < 2:
    	continue
    else:
            sss = [a for a in line.split(' ') if a != '']
            if sss[0] in gt_count:
            	f2.write(line)
            else:
            	new_line = sss[0] + ' ' + '_RARE_' + '\n'
            	f2.write(new_line)
    else:
    	break

f1.close
f2.close






    	