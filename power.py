def populate_resistances(rlist):
    '''This is meant to put together a list of resistances relevant
        to vaping. Intervals of .02 from .10 to .30, then intervals
        of .5 from .35 to 1.0, then intervals of .1 from 1.1 to 3.0'''
    rlist = []
    #generating a set of lists, then dividing by float...
    list1 = xrange(10, 31, 2)
    list2 = xrange(35, 100, 5)
    list3 = xrange(10, 30)
    #...to get the desired values. Then, appending to the list.
    for each in list1:
        rlist.append(each/100.)
    for each in list2:
        rlist.append(each/100.)
    for each in list3:
        rlist.append(each/10.)
    return rlist

