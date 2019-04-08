CREATE TABLE tbl_artists (
  artist_id INTEGER PRIMARY KEY,
  artist_name TEXT
);

CREATE TABLE tbl_albums (
  album_id INTEGER PRIMARY KEY,
  album_name TEXT,
  artist_id INTEGER
);

CREATE TABLE tbl_songs (
  song_id INTEGER PRIMARY KEY,
  album_id INTEGER,
  track_position INTEGER,
  song_name TEXT,
  song_length_sec INTEGER
);
