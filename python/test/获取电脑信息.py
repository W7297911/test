# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-12-15 14:01
# Author:Wangyafei

import psutil as cp

# 获取CPU逻辑逻辑数量
cpu1 = cp.cpu_count()
print("CPU逻辑数量为:%s" % cpu1)

# 获取CPU物理核心
cpu2 = cp.cpu_count(logical=False)
print("CPU物理核心为:%s" % cpu2)

# 统计CPU的用户/系统/空闲时间
kong = cp.cpu_times()
print("统计CPU用户信息如下：")
print(kong)

# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for x in range(2):
    print(cp.cpu_percent(interval=1, percpu=True))

# 获取内存信息
# 使用psutil获取物理内存和交换内存信息，分别使用
vm = cp.virtual_memory()
sm = cp.swap_memory()
print("物理内存如下：")
print(vm)
print("交换区内存为：")
print(sm)

# 获取磁盘信息
# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息
disk = cp.disk_partitions()  # 磁盘分区信息
print("硬盘信息如下：")
print(disk)

disk1 = cp.disk_usage('/') # 磁盘使用情况
print("硬盘使用情况：")
print(disk1)

disk3 = cp.disk_io_counters() # 磁盘IO
print("磁盘IO使用情况：")
print(disk3)

# 获取网络信息
# psutil可以获取网络接口和网络连接信息
net = cp.net_io_counters() # 获取网络读写字节／包的个数
print("获取网络读写字节：")
print(net)
net1 = cp.net_if_addrs() # 获取网络接口信息
print("获取网络接口信息：")
print(net1)
net2 = cp.net_if_stats()  # 获取网络接口状态
print("获取网络接口状态：")
print(net2)


# 获取进程信息
# 通过psutil可以获取到所有进程的详细信息：
ps = cp.pids()  # 所有进程ID
print("显示所有进程：")
print(ps)
p = cp.Process(ps[5]) # 获取指定进程ID=3776，其实就是当前Python交互环境
print(p.name()) # 进程名称
# print(p.exe())# 进程exe路径
# print(p.cwd())# 进程工作目录
# print(p.cmdline()) # 进程启动的命令行
print(p.ppid()) # 父进程ID
# print(p.parent()) # 父进程
# print(p.children()) # 子进程列表
# print(p.status())  # 进程状态
# print(p.username()) # 进程用户名
# print(p.create_time())  # 进程创建时间
# print(p.terminal()) # 进程终端
print(p.cpu_times()) # 进程使用的CPU时间
print(p.memory_info()) # 进程使用的内存
# print(p.open_files())  # 进程打开的文件
# print(p.connections()) # 进程相关网络连接
# print(p.num_threads()) # 进程的线程数量
# print(p.threads()) #
# print(p.environ()) # 所有线程信息 进程环境变量
#.terminate() # 结束进程'''
# pp = cp.test()

# print("显示test：")
# print(pp)