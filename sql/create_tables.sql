CREATE TABLE IF NOT EXISTS spotify_tracks (
    track_id VARCHAR(100) PRIMARY KEY,
    track_name VARCHAR(255),
    artist_name VARCHAR(255),
    album_name VARCHAR(255),
    release_date DATE,
    duration_ms INTEGER,
    duration_minutes NUMERIC(10,2),
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);