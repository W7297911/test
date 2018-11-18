# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-11-18 20:37
# Author:Wangyafei

# 1、文件打开方法：open(name[,mode[buf]])
# name:文件路径
# mode:打开方式
# buf:缓冲buffering大小

# r	只读	 文件必须存在
# w	只写	 文件不存在时创建文件，存在则清空文件内容
# a	追加	 文件不存在时创建文件
# r+	打开文件会保持原文件内容不变，同样可以同时对文件进行读写
# w+	打开文件会将原文件内容删除，可以同时对文件进行读写
# a+	追加和读写方式
# rb,wb,ab,rb+,wb+,ab+	二进制方式打开(读取图片等。)。


# 2、文件读取方式：
# read([size]):读取文件（读取size个字节，默认读取全部）
# readline([size]):读取一行
# readlines([size]):读取完文件，返回每一行所组成的列表


# 3、文件写入方式：
# write(str):将字符串写入文件
# writelines(sequence_of_strings):写多行到文件

# f.write(),写完之后，写在了文件缓冲；要执行f.close() or f.flush(),才可以真写入到文件中。
# 写缓冲和文件不一致：
# 1、主动f.close() 或者 f.flush()
# 2、写入数据量大于或者等于写缓存，写缓存同步到磁盘

# 文件指针操作：
# python 文件指针 os_SEEK_SET:相对文件起始位置;
# os.SEEK_CUR：相对文件当前位置;
# os.SEEK_END:相对文件结尾位置;
# seek(offset[,whence]):移动文件指针;offset:偏移量,可以为负数;whence:偏移相对位置;
# os.SEEK_SET:相对文件起始位置 ；f.seek(0,os.SEEK_SET)使文件指针回到开始位置；使有f.tell()查看文件指针位置
# f.seek(-5,os.SEEK_CUR)：从后向前移动5个字节
# f.seek(0,os.SEEK_END):将文件指针移到最后


# file.fileno（）文件的描述
# file.mode 文件的打开权限
# file.encoding() 文件的编码
# file.closed 文件是否关闭


# os模块
# os.open(filename,flag[,mode]): 打开文件
# flag:打开文件方式
# os.O_CREAT:创建方式打开
# os.O_RDONLY:只读方式打开
# os.O_WRONLY:只写方式打开
# os.O_RDWR:读写方式打开
# os.read(fd,buffersize): 读取文件
# os.write(fd,string): 写入文件
# os.lseek(fd,pos,how): 文件指针操作
# os.close(fd): 关闭文件

# f = open('config.ini', 'a+')
#
# f.write('this is first wenajian')
# c = f.readline()
# print(c)
# f.close()

import configparser

cfg=configparser.ConfigParser()

con1 = cfg.read('config.ini')
print(con1)
con2 = cfg.sections()

print('-'*35+'修改密码前'+'-'*35)
# 修改前
for se in con2:
    print(se)
    print(cfg.items(se))

cfg.set('userinfo', 'pwd', '12345678')  # 修改用户密码
print('-'*35+'修改密码后'+'-'*35)
for se in con2:
    print(se)
    print(cfg.items(se))
print('-' * 35 + '插入邮箱后' + '-' * 35)
cfg.set('userinfo', 'email', 'abcd@qq.com') # 插入邮箱
for se in con2:
    print(se)
    print(cfg.items(se))
print('-' * 35 + '删除邮箱后' + '-' * 35)
cfg.remove_option('userinfo', 'email') # 删除邮箱
for se in con2:
    print(se)
    print(cfg.items(se))
print('-'*78)

fp = open('config.ini', 'w')
cfg.write(fp)
fp.close()