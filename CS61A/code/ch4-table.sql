-- 知识点： 每一个select语句都添加一行, 每一列都有名字(parent, child)；union把所有行都连在一个表中；create table为表命名.
-- create table parents as
--     select "abraham" as parent, "barack" as child union
--     select "abraham"          , "clinton"         union
--     select "delano"           , "herbert"         union
--     select "fillmore"         , "abraham"         union
--     select "fillmore"         , "delano"          union
--     select "fillmore"         , "grover"          union
--     select "eisenhower"       , "fillmore";


----------
-- Dogs --
----------

-- Parents
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

-- Fur
create table dogs as
  select "abraham" as name, "long" as fur union
  select "barack"         , "short"       union
  select "clinton"        , "long"        union
  select "delano"         , "long"        union
  select "eisenhower"     , "short"       union
  select "fillmore"       , "curly"       union
  select "grover"         , "short"       union
  select "herbert"        , "curly";

-- join table: join parents和dogs两张表。得到的结果会是parents的每一行和dogs的每一行的组合。
-- (join后的表的某一行由parents表的某一行和dogs的某一行(就在其后)组成)
select parent, child, name, fur
  from parents, dogs;

-- select all pairs of siblings
-- 找出有相同parent的狗，而且以成对的方式输出。
select a.child as first, b.child as second
  from parents as a, parents as b
  where a.parent = b.parent and a.child < b.child;

-- Joining Multiple Tables
create table grandparents as
    select a.parent as grandog, b.child as granpup
    from parents as a, parents as b
    where b.parent = a.child;

select grandog from grandparents, dogs as c, dogs as d
    where c.fur = d.fur and
    c.name = grandog and
    d.name = grandpup;


------------
-- Cities --
------------

create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,              71,              "Cambridge"        union
  select 45,              93,              "Minneapolis"      union
  select 33,             117,              "San Diego"        union
  select 26,              80,              "Miami"            union
  select 90,               0,              "North Pole";

-- 找出cities 表中维度大于43的所有城市
create table cold as 
    select name from cities where latitude >= 43;

create table distances as
    select a.name as first, b.name as second,
    60 * (b.latitude - a.latitude) as distance
    from cities as a, cities as b;



---------------
-- Sentences --
---------------

create table nouns as
  select "the dog" as phrase union
  select "the cat"           union
  select "the bird";

-- join 表和它自己，但是要剔除重复部分
select subject.phrase || " chased " || object.phrase
  from nouns as subject, nouns as object
  where subject.phrase != object.phrase;

create table ands as 
  select phrase from nouns union
  select first.phrase || " and " || second.phrase
  from nouns as first, nouns as second
  where first.phrase != second.phrase;

select subject.phrase || " chased " || object.phrase
  from ands as subject, ands as object
  where subject.phrase != object.phrase;