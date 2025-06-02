DROP TABLE IF EXISTS tracks;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS albums;

CREATE TABLE albums
( number    INT(5) AUTO_INCREMENT,
  title        VARCHAR(50) NOT NULL,
  producer     VARCHAR(50) NOT NULL,
  release_year YEAR NOT NULL,
  CONSTRAINT albums_PK PRIMARY KEY (number)
);


CREATE TABLE genre
( code        INT(10) AUTO_INCREMENT,
  description VARCHAR(100) NOT NULL,
  CONSTRAINT genre_PK PRIMARY KEY (code)
);


CREATE TABLE songs
( id        INT(5) AUTO_INCREMENT,
  title     VARCHAR(50) NOT NULL,
  duration  VARCHAR(20) NOT NULL,
  artist    VARCHAR(30) NOT NULL,
  genre_code INT(5)      NOT NULL,
  CONSTRAINT songs_PK PRIMARY KEY (id),
  CONSTRAINT songs_genre_FK FOREIGN KEY (genre_code) REFERENCES genre(code)
);


CREATE TABLE tracks
( song_id      INT(5),
  album_number INT(5) NOT NULL,
  track     INT(2) NOT NULL,
  CONSTRAINT tracks_PK PRIMARY KEY (song_id, album_number),
  CONSTRAINT tracks_songs_FK FOREIGN KEY (song_id) REFERENCES songs(id),
  CONSTRAINT tracks_albums_FK FOREIGN KEY (album_number) REFERENCES albums(number)
);