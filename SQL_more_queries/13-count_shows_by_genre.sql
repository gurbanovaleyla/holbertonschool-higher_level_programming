-- 12-no_genre.sql
-- lists all shows without a genre linked

SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows,
    tv_show_genres
WHERE
    tv_shows.id = tv_show_genres.show_id
    AND tv_shows.id NOT IN (
        SELECT show_id
        FROM tv_show_genres
    )
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;
