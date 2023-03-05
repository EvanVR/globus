DROP TABLE IF EXISTS 'bikes';

CREATE TABLE 'bikes' (
    id TEXT NOT NULL,
    name TEXT NOT NULL,
    wheels INTEGER,
    size INTEGER,
    motor BINARY,
    folding BINARY,
    image TEXT,
    available INTEGER
);

.mode csv
.import bikes.csv bikes