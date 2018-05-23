#coding = utf-8
#测试
for i in range(0,8):

    for j in range(0,8):
        OA = int(abs(1 - i) + abs(7 - j))
        OB = int(abs(8 - i) + abs(6 - j))
        OC = int(abs(6 - i) + abs(3 - j))
        OD = int(abs(2 - i) + abs(0 - j))
    sum = int(OA +OB +OC +OD)
    print ("sum = %d"%sum)
    print("*"*40)
print("$"*40)
for feiers in range(1,10):
    print(type(feiers))
    print("上面的计算过程好像是错误的 %2d"%feiers)

