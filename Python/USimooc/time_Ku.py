#coding = utf-8
#时间获取：time()   ctime()    gmtime()
#时间格式化：strftime()   strptime()
#程序计时：sleep()   perf_counter()
import time
time.sleep(2)
start = time.perf_counter()
str = "现在时间是："
nowTime1 = time.time()
nowTime2 = time.ctime()
nowTime3 = time.gmtime()
nowTime4 = time.strftime("%Y-%m-%d  %H:%M:%S",nowTime3)
print("{0}{1}\n{0}{2}\n{0}{3}".format(str, nowTime1, nowTime2, nowTime4))
end = time.perf_counter()
print("程序执行时间：{}".format(end-start))
time.sleep(2)