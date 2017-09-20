def opposite(str):
    org = str
    opp = ""
    i = 0
    for i in range(0, len(org)):
        opp += org[(-1-i)]
    return opp

print opposite("stressed")
