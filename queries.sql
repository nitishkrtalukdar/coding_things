


/* 
Scenario: currently showing, book 2 tickets, snacks, seat a row, show timing is afternoon

movies> m
shows> sh
show seats> ss
seats > se
*/

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

/*ADD AVATAR 3 AS A NEW MOVIE INTO MOVIE TABLE*/
insert into movies(title,genre,rating,status)
    values('Avatar 3','Sci-Fi','9.1','Now Showing');
update movies 
    set movie_id=(select max(movie_id)+ 1 from movies) where title='Avatar 3';

select * from movies where title='Avatar 3';

/*ADD NEW IMAX SCREEN SCENARIO*/
insert into screens
    (screen_id,name,class_type,capacity)
    values
    ((select max(screen_id)+1 from screens),'IMAX','Premium',120)

/*inserting new user into user table*/
insert into users
    values((select max(user_id)+1 from users),
            'Priya Nair',
            'priyanair@gmail.com',
            8892829211);

/*add booking details*/
insert into bookings(booking_id,user_id)
    values(
            (select max(booking_id)+1 from bookings),
            (select user_id from users where name='Priya Nair')
            )
update bookings set show_id=(select show_id from shows where movie_id=(select movie_id from movies where title='Avatar 3'))


update users set phone='8272920092' where name='Priya Nair'
select * from users where name='Priya Nair'

/*ADDING SHOW DETAILS OF AVATAR 3*/
insert into shows(show_id,movie_id)
    VALUES((select max(show_id)+1 from shows),
            (select movie_id from movies where title='Avatar 3'))

select * from bookings b
    JOIN users u 
    on b.user_id=u.user_id
    where u.name='Priya Nair';

/*ADD 1000 POINTS TO THOSE USERS WHO HAD A BOOKING ABOVE 1000*/
update memberships set current_points=current_points+1000
    WHERE user_id in (select user_id from bookings where total_cost>=1000)