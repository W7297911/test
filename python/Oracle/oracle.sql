select * from emp;
--分组函数
select min(sal), avg(sal), max(sal), deptno from emp group by deptno;

--二级分组

select min(sal), avg(sal), max(sal), deptno，job
  from emp
 group by deptno, job
 order by deptno;

select deptno, job, min(sal), avg(sal), max(sal)
  from emp
 group by deptno, job
 order by deptno;

select deptno, job, min(sal), avg(sal), max(sal)
  from emp
 group by deptno, job
having avg(sal) > 2000;

select deptno, job, min(sal), avg(sal), max(sal)
  from emp
 group by deptno, job
having avg(sal) > 2000
 order by deptno;

--多表查询

select * from dept;
select * from emp;

select a1.ename, a1.sal, a2.dname from emp a1, dept a2;

select a1.ename, a1.sal, a2.dname from emp a1, dept a2 where a1.;
select * from emp;
select sysdate, systimestamp from dual;
create table student(id number(2), name varchar2(20), sex char(4));
alter table student add(classid number(2), classname varchar2(20));
select * from student;
alter table student modify(id number(2));
insert into student values (1, '张珊', '男', 2, '二年级');
insert into student values (2, '张珊2', '女', 1, '一年级');
insert into student values (3, '张珊3', '男', 2, '二年级');
insert into student values (4, '张珊4', '女', 1, '一年级');
insert into student values (5, '张珊5', '男', 2, '二年级');

select *
  from student
       
       create table INFOS(STUID VARCHAR2(7) NOT NULL, --学号  学号="S"+班号+2位序列号
       STUNAME VARCHAR2(10) NOT NULL, --姓名
       GENDER VARCHAR2(2) NOT NULL, --性别
       AGE NUMBER(2) NOT NULL, --年龄
       SEAT NUMBER(2) NOT NULL, --座号
       ENROLLDATE DATE, --入学时间
       STUADDRESS VARCHAR(20) DEFAULT '地址不详', --住址
       CLASSNO VARCHAR2(4) NOT NULL --班号  班号=学期序号+班级序号
       );
SELECT * FROM INFOS;
alter table infos add constraint pk_infos primary key(STUID);
alter table infos add constraint ck_infos_gender check(GENDER = '男' OR
                                                       GENDER = '女');

alter table infos add constraint ck_infos_SEAT check(SEAT >= 0 and
                                                     SEAT <= 50);

alter table infos add constraint ck_infos_AGE check(AGE >= 0 and
                                                    AGE <= 100);

alter table infos add constraint ck_infos_CLASSNO check((CLASSNO >= '1001' AND
                                                        CLASSNO <= '1999') OR
                                                        (CLASSNO >= '2001' and
                                                        CLASSNO <= '2999'));

ALTER TABLE INFOS ADD CONSTRAINT UN_STUNAME UNIQUE(STUNAME);

CREATE TABLE SCORES(ID NUMBER,
                    TERM VARCHAR2(2),
                    STUID VARCHAR2(7) NOT NULL,
                    EXAMNO VARCHAR2(7) NOT NULL,
                    WRITTENSCORE NUMBER(4, 1) NOT NULL,
                    LABSCORE NUMBER(4, 1) NOT NULL);

select *
  from INFOS alter table SCORES add constraint ck_scores_term check(TERM = 'S1' OR TERM = 'S2');
alter table SCORES add constraint fk_scores_infos_stuid foreign key(stuid) references infos(stuid);

select * from infos;
select * from scores;

create table infos1 as
  select * from infos;
select * from infos1;
create table infos2 as
  select * from infos where 1 = 2;
select * from infos2;
drop table infos2;
insert into infos
values
  ('S100102',
   '林冲',
   '男',
   22,
   2,
   to_date('2018-08-12 06:30:10', 'YYYY-MM-DD HH24:MI:SS'),
   '西安',
   '1001');
insert into infos
values
  ('S100104', '阮小二', '男', 26, 3, sysdate, default, '1001');
commit;
select * from infos1;

INSERT INTO INFOS1
  SELECT * FROM INFOS;
SELECT * FROM INFOS1;
DELETE FROM INFOS1;
UPDATE INFOS1
   SET CLASSNO = '1001', STUADDRESS = '山东莱芜'
 where stuname = '阮小二';
COMMIT;
--算数运算
select * from scores;
select stuid, examno, (writtenscore + labscore) / 2 as avg
  from scores
 where (writtenscore + labscore) / 2 > 90;

--字符串连接
select (ename || ' is a ' || job) as "employee details"
  from emp
 where sal > 2000;

--消除重复行
select distinct deptno from emp;

select * from emp;

-- null值查询
select ename, job, sal, comm
  from emp
 where sal < 2000
   and comm is null;

--集合运算
/*
INTERSECT(交集)，返回两个查询共有的记录。
UNION  ALL（并集），返回各个查询的所有记录，包括重复记录。
UNION (并集)，返回各个查询的所有记录，不包括重复记录。
MINUS(补集)，返回第一个查询检索出的记录减去第二个查询检索出的记录之后剩余的记录。
*/
select deptno from emp union all select deptno from dept;
select deptno from emp intersect select deptno from dept;
select deptno from emp minus select deptno from dept;

insert into dept
  select 50, '公关部', '台湾'
    from dual
  union
  select 60, '研发部', '西安'
    from dual
  union
  select 70, '培训部', '西安'
    from dual;
select * from dept;
select * from infos;

--连接查询
-- 1.内连接
select e.ename, e.job, e.sal, d.dname
  from emp e, dept d
 where e.deptno = d.deptno
   and e.sal > 2000;
select e.ename, e.job, e.sal, d.dname
  from emp e
 inner join dept d
    on e.deptno = d.deptno
 where e.sal > 2000;

--2.外连接
select e.ename, e.job, e.sal, d.dname
  from emp e, dept d
 where e.deptno(+) = d.deptno;
select e.ename, e.job, e.sal, d.dname
  from emp e
 right outer join dept d
    on e.deptno = d.deptno;
select * from emp;
--子查询
select ename, job, sal
  from emp
 where deptno = (select deptno from dept where dname = 'SALES');
select ename, job, sal
  from emp
 where sal < (select max(sal) from emp where job = 'SALESMAN');
select ename, job, sal
  from emp
 where sal < any (select sal from emp where job = 'SALESMAN');
--伪列
select rowid, ename from emp;
select rownum, ename from emp;

--单行函数
--1.字符函数：对字符串操作
--2.数字函数：对数字进行计算，返回一个数字
--3.转换函数：可以将一种数据类型转换为另外一个数据类型
--4.日期函数：对日期和时间进行处理
--聚合函数：聚合函数同时可以对多行数据进行操作，并返回一个结果

SELECT SYSDATE, ADD_MONTHS(SYSDATE, 5) AS "AFTER FIVE MONTHS" FROM DUAL;

SELECT SYSDATE, LAST_DAY(SYSDATE) FROM DUAL;

SELECT SYSDATE,
       ROUND(SYSDATE),
       ROUND(SYSDATE, 'DAY'),
       ROUND(SYSDATE, 'MONTH'),
       ROUND(SYSDATE, 'YEAR')
  FROM DUAL;

SELECT * FROM EMP;

SELECT ENAME, JOB, (SAL + NVL(COMM, 0)), NVL(COMM, 0) FROM EMP;

SELECT ENAME AS "姓名",
       JOB AS "职位",
       (SAL * 2 + NVL2(COMM, 0, 1000)) AS "工资",
       NVL2(COMM, 0, 1000) AS "奖金"
  FROM EMP;

SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO;

--创建视图
CREATE OR REPLACE VIEW EMPDETAIL AS
  SELECT EMPNO, ENAME, JOB, HIREDATE, EMP.DEPTNO, DNAME
    FROM EMP
    JOIN DEPT
      ON EMP.DEPTNO = DEPT.DEPTNO WITH READ ONLY;

select * from empdetail;
select * from scott_view;

select * from empdetail;
--创建索引
create unique index UQ_ENAME_IDX ON EMP(ENAME);
create index IDX_SAL ON EMP(SAL);
create index IDX_JOB_LOWER ON EMP(LOWER(JOB));

--逻辑清晰
--1.查询出各个部门的平均工资和部门号

select deptno, avg(sal) mysal from emp group by deptno;

--2.把上面的查询看作是一张子表

select a2.ename, a2.sal, a2.deptno, a1.mysal
  from emp a2, (select deptno, avg(sal) mysal from emp group by deptno) a1
 where a2.deptno = a1.deptno
   and a2.sal > a1.mysal

--oracle分页一共有三种方式
--1.rownum分页
  select a1.*, rownum from (select * from emp) a1 where rownum <= 10;


select *
  from (select a1.*, rownum from (select * from emp) a1 where rownum <= 10)
 where rownum < 6;
--2.几个查询变化
--a.指定查询列，只需修改最里层的子查询
select *
  from (select a1.*, rownum
          from (select ename, sal from emp) a1
         where rownum <= 10)
 where rownum < 6;
--b.如何排序
select *
  from (select a1.*, rownum
          from (select ename, sal from emp order by sal desc) a1
         where rownum <= 10)
 where rownum < 6;

--重新建立新表
create table emp_12(id, ename, sal) as
  select empno, ename, sal from emp;

select * from emp_12;

--合并查询
--有时在实际应用中，为了合并多个select语句的结果，可以使用集合操作符号 union，union all， intersect，miuns;
--union 该操作符用于取得两个结果集的并集，当使用该操作符时，会自动去掉结果集中重复行；

select ename,sal,job from emp where sal>2500 union 
select ename,sal,job from emp where job='MANAGER'

--union all 该操作赋予union相似，但是它不会取消重复行而且不会排序
select ename,sal,job from emp where sal>2500 union all 
select ename,sal,job from emp where job='MANAGER'

--intersect 该操作符用于取得两个结果集的交集
select ename,sal,job from emp where sal>2500 intersect 
select ename,sal,job from emp where job='MANAGER'

--minus 使用该操作符用于取得两个结果集的差集，它只会显示存在第一个集合中，而不存在第二个集合中的数据
select ename,sal,job from emp where sal>2500 minus 
select ename,sal,job from emp where job='MANAGER'


--to_date 转换日期格式
insert into emp values(8866,'qq','MANAGER',7788,to_date('1988-12-12','yyyy-mm-dd'),8000,'',10);



--插入子查询结果
create table emp_t (myid number(4),myname varchar2(20), mydept number(5));
insert into emp_t(myid,myname,mydept) select emp.empno,emp.ename,emp.deptno from emp where deptno=10;
select * from emp_t;


--更新子查询结果
update emp set (job,sal,comm)=(select job,sal,comm from emp where ename='SMITH') where ename='SCOTT';
select * from emp;

--事务
--事务是保证数据一致性，它由一组相关的dml语句组成，该组的dml语句要么全部成功，要么全部失败。
--锁 当执行事务时（dml语句），Oracle会在被作用的表上加锁，防止其他用户改表表的结构。

--提交事务 使用commit语句可以提交事务，当执行了commit语句后，会确认事务的变化、结束事务、删除保存点、释放锁，当使用commit语句结束
--事务后，其他会话将可以查看到事务变化后的新数据；
  
--回退事务 先理解保存点（savepoint）的概念和作用。保存点是事务的一个点，用于取消部分事务，当结束事务时，会自动的删除该事物所定义的所有保存点
--当执行rollback时，通过指定保存点可以回退到指定的点；
--如果保存点之后已经commit提交事务时，该保存点就失效；

--设置保存点a1
savepoint a1;

delete from emp where ename='小李';
select * from emp;
insert into emp values(8826,'qq1','MANAGER',7788,to_date('1988-12-12','yyyy-mm-dd'),8000,'',10);

--设置保存点a2
savepoint a2;

delete from emp where ename='小爱';

select * from emp;

--取消部分事务
rollback to a2;

--取消全部事务
rollback;



--SQL函数使用
--字符函数：
--lower（char）:将字符串转化为小写的格式
--upper（char）:将字符串转化为大写的格式
--length（char):返回字符串的长度
--substr（char,m,n）:取字符串的子串

select lower(emp.ename) as 小写 from emp;
select upper(ename) as 大写 from emp;
select length(ename) from emp;
select substr(ename,2,2) from emp;
select * from emp where length(ename)=5;
select upper(substr(e.ename,1,1))||lower(substr(e.ename,2,length(ename)-1))as 首字母大写 from emp e;

--replace(char1,search_string,replce_string)
--instr(char1,char2,[,n[,m]])取子串在字符串中的位置

select replace(ename,'A','a') from emp;


--数学函数
--round(n,[m]):四舍五入，m小数位
--trunc(n,[m])：截取位数，m小数位
--mod(n)：
--floor(n)：返回小于或等于n的最大整数
--ceil(n): 返回大于或是等于n的最小整数

select e.sal,e.comm, (round(e.sal)+round(e.comm))*13 from emp e;


select trunc(sal,1) from emp;

select mod(10，2) from dual;

/*avg() :  求平均值，计算并返回表达式的平均值
count（） :统计数目，返回一个集合中的项数
max （）:求最大值，返回表达式中的最大值
min（）: 求最小值，返回表达式中的最小值
sum（） :求和，计算并返回表达式各项之和
stddev（）： 求标准差
stddev_pop（）：求总体标准差
聚合函数常与select语句中的group by子句一起使用，除了count（）函数，其他都会忽略null
用法 select 函数名 （列名） from 表名 或加上 group by 列名 having 函数式
select sum(nl)  xb from a group by xb having sum(nl)>40 ;
意为  在xb相同情况下， 求出总和大于40的xb，并输出来
select stddev_pop(nl),xb from a group by xb  ;
求   在xb相同情况下，求标准差
当group by 与 order by 同时使用时，order by 子句中的列必须包含在聚合函数中或group by 子句中
select sum(nl),xb from a  group by xb,nl order by nl  ; 
输出 nl 的总和并排序
abs（n）：用于返回n的绝对值       sqrt（n）：返回n的平方
acos(n):反余弦函数，用于返回-1--1之间的数，n表示弧度
asin（n）:反正弦函数，用于返回-1--1之间的数，n表示弧度
atan（n）：反正切函数，用于返回n的反正切值，n表示弧度
ceil（n）：用于返回等于n的最小整数
cos（n）：用于返回n的余弦值，n为弧度
cosh（n）：用于返回n的双曲余弦值，n为数字
exp（n）：用于返回e的n次幂，e=2.71828183
floor（n）：用于返回小于或等于n的最大整数
ln（n）：用于返回n的自然对数，n>0
log(n1，n2)：用于返回以n1为底，n2的对数
mod(n1，n2):用于返回n1除以n2的余数
power（n1，n2）：用于返回n1的n2次方
round（n1，n2）：四舍五入，n2为小数点后的剩余几位，n2为整数
sign（n）：若n<0 返回-1 ,n>0 返回1 ,n=0 返回0
sin（n）：用于返回n的正弦值，n为弧度
sinh（n）：用于返回n的双曲正弦值，n为弧度
tan（n）：用于返回n的正切值，n为弧度
tanh（n）：用于返回n的双曲正切值，n为弧度
trunc（n1，n2）：当n2为0，n1的小数去除，n2不为0，小数留下相应的n2位
*/


--日期函数

--sysdate 系统日期
--add_months
--
select * from emp where sysdate>add_months(hiredate,300);
select ename,trunc(sysdate-hiredate) as 入职天数 from emp;
