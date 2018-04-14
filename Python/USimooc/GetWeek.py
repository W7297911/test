#coding = utf-8
weekstr = "一二三四五六七"
weekid = eval(input("请输入数字（1-7）："))
print("星期{}".format(weekstr[weekid-1]))