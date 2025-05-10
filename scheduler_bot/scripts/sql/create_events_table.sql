CREATE TABLE events (
    event_id serial PRIMARY KEY,
    event_time TIME,
    event_date DATE NOT NULL,
    -- use limited length here (?)
    event_summary TEXT NOT NULL
);