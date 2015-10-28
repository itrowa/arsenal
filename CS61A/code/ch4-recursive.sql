---------------
-- Ancestors --
---------------

-- 这个表包含了一系列狗的名字，和他们之间的继承关系。以后做别的实验应该也能用得上这个数据吧.
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";


-- 介绍with clause: 放在select语句之前的，用于创建只有这个select语句才能使用的sub table
-- 我把我最喜欢的两只狗放在best子表best中,best只有1列，名字叫做dog。
-- 接着我筛选出我最喜欢的狗的parent并列出来。

-- 筛选我喜欢的两只狗eisenhower和barack的parent并列出。
with
    best(dog) as (
        select "eisenhower" union
        select "barack"
        )
select parent from parents, best where child=dog;
-- 解释: select parent from parents, best， 但是parent只在表parents中有。为什么还要加上best表呢，
-- 因为后面where后跟的表达式的col名是在parents 和best中寻找的.

-- 找出parents表中所有的nephew和uncle关系
with
  siblings(first, second) as (
      -- 创建一个'后代'表, 列出同一个祖先的后代的pairs
      select a.child, b.child
      from  parents as a, parents as b
      where a.parent = b.parent and a.child != b.child
    )
select child as nephew, second as uncle 
  from parents, siblings where parent = first;
  -- 可以根据ppt来理解。


---------------
-- Recursive local table --
---------------

-- ancestor的定义是parent,和parent的ancestor，这样可以找出所有的ancestor来。
-- 同时利用了local table可以递归定义的特性。

with
  ancestors(ancestor, descendent) as (
    select parent, child from parents union
    select ancestor, child
      from ancestors, parents
      where parent = descendent
      )
select ancestor from ancestors where descendent = "herbert";  


--------------
-- global names with recursive table
--------------

-- 创建recursive table的时候只能在local table中创建，但是要引用这个table
-- 的时候怎么办？ 只能这样干了：
create table odds_1_to_15 as 
  with
    odds_1_to_15(n) as (
        select 1 union
        select n+2 from odds where n < 15
      )
select n from odds_1_to_15;


--------------
-- Recursive sentences
--------------

create table nouns as
  select "the dog" as phrase union
  select "the cat"           union
  select "the bird";

-- 利用前面的nouns表造句 s + v + o 格式
select s.phrase || " chased " || o.phrase
  from nouns as s, nouns as o
  where s.phrase != o.phrase;

-- 利用nouns表造复合句
with 
  compounds(phrase, n) as (
      select phrase, 1 from nouns union     -- 1就是数字1，没别的意思
      select subject.phrase || " that chased " || object.phrase, n+1
        from compounds as subject, nouns as object
        where n < 2 and subject.phrase != object.phrase
    )
select subject.phrase || " ate " || object.phrase
  from compounds as subject, compounds as object
  where subject.phrase != object.phrase;

-- 解释： 
-- test上面↑↑↑↑↑↑↑↑这个复合句输出的啥？
with 
  compounds(phrase, n) as (
      -- result:
      -- the ____                         | 1
      -- the __                           | 1
      -- the ____ that chased the _____   | 1
      -- the ____ that chased the _____   | 1
      -- the ____ that chased the _____   | 2
      select phrase, 1 from nouns union
      select subject.phrase || " that chased " || object.phrase, n+1
        from compounds as subject, nouns as object
        where n < 2 and subject.phrase != object.phrase
    )
select * from compounds;



------------------
-- Number games
------------------

-- 利用local table 的递归特性创建一个奇数table
create table odds as
  with odds(n) as (
      select 1 union
      select n+2 from odds where n < 15
    )
select n from odds;

-- 创建毕达哥拉斯表。（勾股定理的三个数）
with 
  i(n) as(
    -- 创建从1~20的表
      select 1 union select n+1 from i where n < 20
    )
select a.n, b.n, c.n from i as a, i as b, i as c
  where a.n < b.n and  a.n*a.n +b.n*b.n = c.n * c.n;

-- Fibonacci sequence
create table fibs as 
  with
    fib(previous, current) as (
        select 0, 1 union
        select current, previous + current from fib
        where current <= 100
      )
  select previous from fib;

-- Arithmetic
create table pairs as
  with
    i(n) as (
        select 1 union select n+1 from i where n < 20
      )
    select a.n as x, b.n as y from i as a, i as b where a.n <= b.n;

select * from pairs where x+y = 24;
select * from pairs where x*y = 24;
select x from pairs where x = y and 24 % x = 0;

-- Interesting Number: 1729 is the smallest sum of 2 cubes in 2 ways 
create table interesting as 
  with
    cubes(x, y, cube) as (
        select x, y, x*x*x + y*y*y from pairs
      )
  select a.cube from cubes a, cubes b
    where a.cube = b.cube and a.x < b.x;