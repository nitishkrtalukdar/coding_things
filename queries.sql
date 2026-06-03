


/* 
Scenario: currently showing, book 2 tickets, snacks, seat a row, show timing is afternoon

movies> m
shows> sh
show seats> ss
seats > se
*/

select m.title,
    ss.show_id,
    sh.show_datetime,
    sc.screen_id,
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

