def populate_resistances(rlist):
    rlist = []
    list1 = xrange(10, 31, 2)
    list2 = xrange(35, 100, 5)
    list3 = xrange(10, 30)
    for each in list1:
        rlist.append(each/100.)
    for each in list2:
        rlist.append(each/100.)
    for each in list3:
        rlist.append(each/10.)
    return rlist

