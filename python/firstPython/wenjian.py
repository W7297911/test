#文件打开方式：open（name[,mode[buf]]）
#name:文件路径
#mode:打开方式
#buf:缓存buffering大小
#文件读取方式
#read([size]):读取文件（读取size个字节，默认读取全部）
#readline([size]):读取一行
#readlines([size]):读取完文件，返回每一行所组成的列表
#文件写入方式：
#write(str):将字符串写入文件
#writelines(sequence_of_strings):写多行到文件
txt = open('1.txt','a')
re = txt.write('www.baidu.com\n')
txt.close()
rw = open('1.txt', 'r')
rr = rw.read()
print(rr)
