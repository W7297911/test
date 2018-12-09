select * from emp;
--���麯��
select min(sal), avg(sal), max(sal), deptno from emp group by deptno;

--��������

select min(sal), avg(sal), max(sal), deptno��job
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

--����ѯ

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
insert into student values (1, '��ɺ', '��', 2, '���꼶');
insert into student values (2, '��ɺ2', 'Ů', 1, 'һ�꼶');
insert into student values (3, '��ɺ3', '��', 2, '���꼶');
insert into student values (4, '��ɺ4', 'Ů', 1, 'һ�꼶');
insert into student values (5, '��ɺ5', '��', 2, '���꼶');

select *
  from student
       
       create table INFOS(STUID VARCHAR2(7) NOT NULL, --ѧ��  ѧ��="S"+���+2λ���к�
       STUNAME VARCHAR2(10) NOT NULL, --����
       GENDER VARCHAR2(2) NOT NULL, --�Ա�
       AGE NUMBER(2) NOT NULL, --����
       SEAT NUMBER(2) NOT NULL, --����
       ENROLLDATE DATE, --��ѧʱ��
       STUADDRESS VARCHAR(20) DEFAULT '��ַ����', --סַ
       CLASSNO VARCHAR2(4) NOT NULL --���  ���=ѧ�����+�༶���
       );
SELECT * FROM INFOS;
alter table infos add constraint pk_infos primary key(STUID);
alter table infos add constraint ck_infos_gender check(GENDER = '��' OR
                                                       GENDER = 'Ů');

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
   '�ֳ�',
   '��',
   22,
   2,
   to_date('2018-08-12 06:30:10', 'YYYY-MM-DD HH24:MI:SS'),
   '����',
   '1001');
insert into infos
values
  ('S100104', '��С��', '��', 26, 3, sysdate, default, '1001');
commit;
select * from infos1;

INSERT INTO INFOS1
  SELECT * FROM INFOS;
SELECT * FROM INFOS1;
DELETE FROM INFOS1;
UPDATE INFOS1
   SET CLASSNO = '1001', STUADDRESS = 'ɽ������'
 where stuname = '��С��';
COMMIT;
--��������
select * from scores;
select stuid, examno, (writtenscore + labscore) / 2 as avg
  from scores
 where (writtenscore + labscore) / 2 > 90;

--�ַ�������
select (ename || ' is a ' || job) as "employee details"
  from emp
 where sal > 2000;

--�����ظ���
select distinct deptno from emp;

select * from emp;

-- nullֵ��ѯ
select ename, job, sal, comm
  from emp
 where sal < 2000
   and comm is null;

--��������
/*
INTERSECT(����)������������ѯ���еļ�¼��
UNION  ALL�������������ظ�����ѯ�����м�¼�������ظ���¼��
UNION (����)�����ظ�����ѯ�����м�¼���������ظ���¼��
MINUS(����)�����ص�һ����ѯ�������ļ�¼��ȥ�ڶ�����ѯ�������ļ�¼֮��ʣ��ļ�¼��
*/
select deptno from emp union all select deptno from dept;
select deptno from emp intersect select deptno from dept;
select deptno from emp minus select deptno from dept;

insert into dept
  select 50, '���ز�', '̨��'
    from dual
  union
  select 60, '�з���', '����'
    from dual
  union
  select 70, '��ѵ��', '����'
    from dual;
select * from dept;
select * from infos;

--���Ӳ�ѯ
-- 1.������
select e.ename, e.job, e.sal, d.dname
  from emp e, dept d
 where e.deptno = d.deptno
   and e.sal > 2000;
select e.ename, e.job, e.sal, d.dname
  from emp e
 inner join dept d
    on e.deptno = d.deptno
 where e.sal > 2000;

--2.������
select e.ename, e.job, e.sal, d.dname
  from emp e, dept d
 where e.deptno(+) = d.deptno;
select e.ename, e.job, e.sal, d.dname
  from emp e
 right outer join dept d
    on e.deptno = d.deptno;
select * from emp;
--�Ӳ�ѯ
select ename, job, sal
  from emp
 where deptno = (select deptno from dept where dname = 'SALES');
select ename, job, sal
  from emp
 where sal < (select max(sal) from emp where job = 'SALESMAN');
select ename, job, sal
  from emp
 where sal < any (select sal from emp where job = 'SALESMAN');
--α��
select rowid, ename from emp;
select rownum, ename from emp;

--���к���
--1.�ַ����������ַ�������
--2.���ֺ����������ֽ��м��㣬����һ������
--3.ת�����������Խ�һ����������ת��Ϊ����һ����������
--4.���ں����������ں�ʱ����д���
--�ۺϺ������ۺϺ���ͬʱ���ԶԶ������ݽ��в�����������һ�����

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

SELECT ENAME AS "����",
       JOB AS "ְλ",
       (SAL * 2 + NVL2(COMM, 0, 1000)) AS "����",
       NVL2(COMM, 0, 1000) AS "����"
  FROM EMP;

SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO;

--������ͼ
CREATE OR REPLACE VIEW EMPDETAIL AS
  SELECT EMPNO, ENAME, JOB, HIREDATE, EMP.DEPTNO, DNAME
    FROM EMP
    JOIN DEPT
      ON EMP.DEPTNO = DEPT.DEPTNO WITH READ ONLY;

select * from empdetail;
select * from scott_view;

select * from empdetail;
--��������
create unique index UQ_ENAME_IDX ON EMP(ENAME);
create index IDX_SAL ON EMP(SAL);
create index IDX_JOB_LOWER ON EMP(LOWER(JOB));

--�߼�����
--1.��ѯ���������ŵ�ƽ�����ʺͲ��ź�

select deptno, avg(sal) mysal from emp group by deptno;

--2.������Ĳ�ѯ������һ���ӱ�

select a2.ename, a2.sal, a2.deptno, a1.mysal
  from emp a2, (select deptno, avg(sal) mysal from emp group by deptno) a1
 where a2.deptno = a1.deptno
   and a2.sal > a1.mysal

--oracle��ҳһ�������ַ�ʽ
--1.rownum��ҳ
  select a1.*, rownum from (select * from emp) a1 where rownum <= 10;


select *
  from (select a1.*, rownum from (select * from emp) a1 where rownum <= 10)
 where rownum < 6;
--2.������ѯ�仯
--a.ָ����ѯ�У�ֻ���޸��������Ӳ�ѯ
select *
  from (select a1.*, rownum
          from (select ename, sal from emp) a1
         where rownum <= 10)
 where rownum < 6;
--b.�������
select *
  from (select a1.*, rownum
          from (select ename, sal from emp order by sal desc) a1
         where rownum <= 10)
 where rownum < 6;

--���½����±�
create table emp_12(id, ename, sal) as
  select empno, ename, sal from emp;

select * from emp_12;

--�ϲ���ѯ
--��ʱ��ʵ��Ӧ���У�Ϊ�˺ϲ����select���Ľ��������ʹ�ü��ϲ������� union��union all�� intersect��miuns;
--union �ò���������ȡ������������Ĳ�������ʹ�øò�����ʱ�����Զ�ȥ����������ظ��У�

select ename,sal,job from emp where sal>2500 union 
select ename,sal,job from emp where job='MANAGER'

--union all �ò�������union���ƣ�����������ȡ���ظ��ж��Ҳ�������
select ename,sal,job from emp where sal>2500 union all 
select ename,sal,job from emp where job='MANAGER'

--intersect �ò���������ȡ������������Ľ���
select ename,sal,job from emp where sal>2500 intersect 
select ename,sal,job from emp where job='MANAGER'

--minus ʹ�øò���������ȡ������������Ĳ����ֻ����ʾ���ڵ�һ�������У��������ڵڶ��������е�����
select ename,sal,job from emp where sal>2500 minus 
select ename,sal,job from emp where job='MANAGER'


--to_date ת�����ڸ�ʽ
insert into emp values(8866,'qq','MANAGER',7788,to_date('1988-12-12','yyyy-mm-dd'),8000,'',10);



--�����Ӳ�ѯ���
create table emp_t (myid number(4),myname varchar2(20), mydept number(5));
insert into emp_t(myid,myname,mydept) select emp.empno,emp.ename,emp.deptno from emp where deptno=10;
select * from emp_t;


--�����Ӳ�ѯ���
update emp set (job,sal,comm)=(select job,sal,comm from emp where ename='SMITH') where ename='SCOTT';
select * from emp;

--����
--�����Ǳ�֤����һ���ԣ�����һ����ص�dml�����ɣ������dml���Ҫôȫ���ɹ���Ҫôȫ��ʧ�ܡ�
