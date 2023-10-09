DROP TABLE IF EXISTS activities;

CREATE TABLE activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    time TEXT NOT NULL,
    image TEXT NOT NULL,
    added BOOLEAN NOT NULL
);