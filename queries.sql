


/* 
Scenario: currently showing, book 2 tickets, snacks, seat a row, show timing is afternoon

movies> m
shows> sh
show seats> ss
seats > se
*/
/*
select m.title,
    ss.show_id,
    date(sh.show_datetime) as show_date,
    time(sh.show_datetime) as show_time,
    sc.name as screen_name,
    sc.class_type,
    count(st.seat_number like 'A%') as available_seats

    from movies m
join shows sh
    on m.movie_id=sh.movie_id
JOIN show_seats ss 
    on sh.show_id=ss.show_id
join seats st 
    on ss.seat_id=st.seat_id
join screens sc
    on st.screen_id=sc.screen_id
where time(sh.show_datetime) between '12:00:00' and '17:00:00'
    and ss.is_available is 'True'
    and st.seat_number like 'A%'
    and m.status='Now Showing'
group by sh.show_id 
having count(st.seat_number like 'A%')>=2
order by m.title
;



PRAGMA table_info(bookings);

/*ADD AVATAR 3 AS A NEW MOVIE INTO MOVIE TABLE
insert into movies(title,genre,rating,status)
    values('Avatar 3','Sci-Fi','9.1','Now Showing');
update movies 
    set movie_id=(select max(movie_id)+ 1 from movies) where title='Avatar 3';

select * from movies where title='Avatar 3';

/*ADD NEW IMAX SCREEN SCENARIO
insert into screens
    (screen_id,name,class_type,capacity)
    values
    ((select max(screen_id)+1 from screens),'IMAX','Premium',120)

/*inserting new user into user table
insert into users
    values((select max(user_id)+1 from users),
            'Priya Nair',
            'priyanair@gmail.com',
            8892829211);

/*add booking details
insert into bookings(booking_id,user_id)
    values(
            (select max(booking_id)+1 from bookings),
            (select user_id from users where name='Priya Nair')
            )
update bookings set show_id=(select show_id from shows where movie_id=(select movie_id from movies where title='Avatar 3'))


update users set phone='8272920092' where name='Priya Nair'
select * from users where name='Priya Nair'

/*ADDING SHOW DETAILS OF AVATAR 3
insert into shows(show_id,movie_id)
    VALUES((select max(show_id)+1 from shows),
            (select movie_id from movies where title='Avatar 3'))

select * from bookings b
    JOIN users u 
    on b.user_id=u.user_id
    where u.name='Priya Nair';

/*ADD 1000 POINTS TO THOSE USERS WHO HAD A BOOKING ABOVE 1000
update memberships set current_points=current_points+1000
    WHERE user_id in (select user_id from bookings where total_cost>=1000)
*/



/* JUNE 3 SQL QUERIES*/

select * from movies;

select title,genre,rating from movies;

select title as 'movie name',
        genre as 'movie genre',
        rating as 'movie rating' from movies;


select * from screens; 

select name,capacity from screens;

select * from screens where capacity > 150;




select name,email from users;

SELECT user_id as 'USER ID',
name as 'NAME',
email as'EMAIL ID',
phone as 'PHONE NUMBER' from users; 

select * from users where phone is not NULL;




select * from movies where title like "A%";

select * from movies where genre in ('Action','Comedy');

select * from movies where rating between 7.5 and 9.0;




select * from shows where date(show_datetime)>'2025-02-10';

select * from shows where screen_id not in (1,2);

select * from shows where movie_id is NULL;



select * from users where user_id IN 
(select user_id from memberships 
    WHERE current_points between 100 and 500);

select * from memberships where user_id is null;

select * from users where user_id in 
    (select user_id from memberships where email like '%@gmail.com' 
        and current_points>0);


select genre,count(*) as count from movies group by genre;

select genre,count(*),avg(rating) as count from movies group by genre;

select genre,count(*),avg(rating) as count from movies group by genre order by avg(rating);



select user_id,count(*) as booking_count from bookings group by user_id;







/* JUNE 4 SQL QUERIES*/

SELECT m.title,m.genre,r.content,r.rating FROM MOVIES m
    Inner JOIN reviews r 
    ON m.movie_id=r.movie_id
    WHERE r.rating>(select AVG(rating) from reviews)
    group by m.movie_id
    order by genre;

SELECT 
    u.user_id,u.email,u.phone, 
    b.show_id,b.booking_datetime,
    m.title,m.status
    from users u 
    JOIN bookings b ON
        b.user_id=u.user_id
    JOIN shows sh ON
        sh.show_id=b.show_id
    JOIN movies m ON
        m.movie_id=sh.movie_id
    where u.user_id in (SELECT user_id from bookings) 
    and m.status='Now Showing';

select * from users 
    WHERE user_id in 
    (SELECT user_id from bookings 
        WHERE show_id in (
            select show_id from shows 
                WHERE movie_id in (
                    SELECT movie_id from movies where status='Now Showing')));

select title from movies
    where movie_id in (
        SELECT movie_id from reviews
        group by movie_id
        HAVING count(*)>=(
            SELECT count(*) from reviews 
                WHERE movie_id in (
                    select movie_id from movies 
                        where genre='Action')
                GROUP BY movie_id));


select avg(select count(rating) as r_count from reviews group by movie_id) from reviews;

select count(rating) as r_count from reviews group by movie_id;


SELECT m.title
FROM movies m
JOIN reviews r
    ON m.movie_id = r.movie_id
GROUP BY m.movie_id
HAVING COUNT(*) >= (
    SELECT AVG(review_count)
    FROM (
        SELECT COUNT(*) AS review_count
        FROM reviews
        GROUP BY movie_id
    ) t
);


SELECT title FROM movies m where EXISTS(SELECT 1 from reviews r where r.movie_id=m.movie_id);

select title from movies where movie_id not in (SELECT movie_id from reviews);

select user_id,name, email,phone from users 
where user_id in (select user_id from bookings WHERE show_id in 
                        (select show_id from shows where movie_id IN
                            (select movie_id from reviews where rating>2)));


SELECT title from movies where genre in 
(select genre from movies GROUP by genre HAVING avg(rating)>2);

select m.title from movies m
join reviews r ON
m.movie_id=r.movie_id
where m.genre in (select m2.genre from movies m2
                    join reviews r2 ON
                    m2.movie_id=r2.movie_id
                     group by m2.genre having avg(r2.rating)>=2 )
group by m.title;


select u.user_id,u.name,u.email from users u 
JOIN bookings b 
ON b.user_id=u.user_id
JOIN shows s 
ON s.show_id=b.show_id
JOIN reviews r 
ON r.movie_id=s.movie_id
WHERE r.movie_id in 
(select movie_id from reviews group by movie_id having count(*)>20);

select m.title,s.show_datetime from movies m
inner join shows s on s.movie_id=m.movie_id;

select user_id,name,email from users
where user_id in (select user_id from bookings);



select * from users u 
join memberships m 
on m.user_id=u.user_id;