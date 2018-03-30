
i=0
while (i<8):
    j=0
    while (j<8):
        OA = int(abs(1 - i) + abs(7 - j))
        OB = int(abs(8 - i) + abs(6 - j))
        OC = int(abs(6 - i) + abs(3 - j))
        OD = int(abs(2 - i) + abs(0 - j))
        j += 1
    i += 1
    sum = int(OA +OB +OC +OD)
    print ("sum = %d"%sum)