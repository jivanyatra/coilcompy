def populate_resistances(list):
    reses = []
    list_1to3 = xrange(10, 30, 2)
    list_3to10 = xrange(35, 100, 5)
    list_10to30 = xrange(10, 30)
    for each in list_1to3:
        reses.append(list_1to3/100.)
    for each in list_3to10:
        reses.append(list_3to10/100.)
    for each in list_10to30:
        reses.append(list_10to30/10.)
    return reses
