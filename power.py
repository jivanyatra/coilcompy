def populate_resistances(list):
    list = []
    list_1to3 = xrange(10, 30, 2)
    list_3to10 = xrange(35, 100, 5)
    list_10to30 = xrange(10, 30)
    for each in list_1to3:
        list.append(list_1to3/100.)
    for each in list_3to10:
        list.append(list_3to10/100.)
    for each in list_10to30:
        list.append(list_10to30/10.)
    return list

