DROP TABLE if EXISTS movies;
create table movies
(
    movieid integer primary key,
    title         text,
    genres      text,
    year    integer
);

DROP TABLE if EXISTS tags;
create table tags
(
    id integer not null primary key autoincrement ,
    tag text,
    userid integer,
    movieid integer,
    time_tags datetime,
    FOREIGN KEY (movieid) REFERENCES movies
);

DROP TABLE if EXISTS ratings;
create table ratings
(
    id integer not null primary key autoincrement ,
    userid integer,
    movieid integer,
    rating real,
    time_rating datetime,
    FOREIGN KEY (movieid) REFERENCES movies
);

DROP TABLE if EXISTS links;
create table links
(
    id integer not null primary key autoincrement ,
    movieid integer,
    imdbid integer,
    tmdbid integer,
    FOREIGN KEY (movieid) REFERENCES movies
);

DROP TABLE if EXISTS genome_scores;
create table genome_scores
(
    id integer not null primary key autoincrement ,
    tagid integer,
    movieid integer,
    relevance real,
    FOREIGN KEY (movieid) REFERENCES movies,
    FOREIGN KEY (tagid) REFERENCES tags
);

DROP TABLE if EXISTS genome_tags;
create table genome_tags
(
    tagid integer primary key  ,
    tag text
);