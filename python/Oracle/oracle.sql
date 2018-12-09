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
