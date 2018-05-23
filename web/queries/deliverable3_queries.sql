--a) Print the names of the top 10 actors ranked by the average rating of their 3 highest-rated clips that where
--voted by at least 100 people. The actors must have had a role in at least 5 clips (not necessarily rated).
Select d.fullname
from (
  SELECT
    c.clip_id,
    p.person_id,
    p.fullname,

)
from clip_rating r where r.votes > 99

--b) Compute the average rating of the top-100 rated clips per decade in decreasing order.



--c) For any video game director, print the first year he/she directed a game, his/her name and all his/her
--game titles from that year.



--d) For each year, print the title, year and rank-in-year of top 3 clips, based on their ranking.
Select extract(year from c.clip_year), min(r.rank) as rank
from clip c, clip_rating r
where c.clip_id = r.clip_id
GROUP BY extract(year from c.clip_year)
-- ORDER BY c.clip_year, rank ASC

--e) Print the names of all directors who have also written scripts for clips, in all of which they were
--additionally actors (but not necessarily directors) and every clip they directed has at least two more
--points in ranking than any clip they wrote.



--f) Print the names of the actors that are not married and have participated in more than 2 clips that they
--both acted in and co-directed it.



--g) Print the names of screenplay story writers who have worked with more than 2 producers.



--h) Compute the average rating of an actor's clips (for each actor) when she/he has a leading role (first 3
--credits in the clip).



--i) Compute the average rating for the clips whose genre is the most popular genre.
Select g.


--j) Print the names of the actors that have participated in more than 100 clips, of which at least 60% where
--short but not comedies nor dramas, and have played in more comedies than double the dramas. Print
--also the number of comedies and dramas each of them participated in.



--k) Print the number of Dutch movies whose genre is the second most popular one.



--l) Print the name of the producer whose role is coord