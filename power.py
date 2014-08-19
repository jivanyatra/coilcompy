def populate_resistances(rlist):
    rlist = []
    list1 = xrange(10, 30, 2)
    list2 = xrange(35, 100, 5)
    list3 = xrange(10, 30)
    for each1 in list1:
        rlist.append(each1/100.)
    for each2 in list2:
        rlist.append(each2/100.)
    for each3 in list3:
        rlist.append(each3/10.)
    return rlist

