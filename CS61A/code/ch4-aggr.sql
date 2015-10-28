create table animals as 
    select "dog" as kind, 4 as legs, 20 as weight union
    select "cat"        , 4        , 10           union
    select "ferret"     , 4        , 10           union
    select "parrot"     , 2        , 6            union
    select "penguin"    , 2        , 10           union
    select "t-rex"      , 2        , 12000; 

-- max(legs) 处理完后得到的是一个row
select max(legs) from animals;

select sum(weight) from animals;

select max(legs - weight) + 5 from animals;

-- 这个表有两列
select min(legs), max(weight) + 5 from animals;

select max(legs) + min(weight) from animals;

select count(legs) from animals;

select count(*) from animals;

-- distinct 是一个关键字，它和count结合，统计legs的值有多少种。
select count(distinct legs) from animals;

select kind, max(weight) from animals;

select legs, max(weight) from animals group by legs;

select weight/legs, count(*) from animals group by weight/legs;

select weight/legs, count(*) from animals group by weight/legs having count(*)>1;

select max(kind), legs, weight from animals group by legs, weight having max(weight) < 100;