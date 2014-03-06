#!/usr/bin/python

import sys

salesTotal = 0
salesNumber = 0


# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    thisSale = line.strip()

    salesTotal += float(thisSale)
    salesNumber += 1

print salesTotal, "\t", salesNumber

