-- this script will list all shows contained in hbtn_0d_tvshows without a genre linked
-- each record should display tv_shows.title, tv_shows_genres.genre_id
-- the result must be sorted in ascending order by title and genre_id
-- you can only use one select statement

SELECT tv_shows.title, tv_shows_genres.genre_id
from tv_shows
RIGHT JOIN tv_shows_genres
ON tv_shows.id = tv_show_genre.show_id
