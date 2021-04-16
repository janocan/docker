CREATE TABLE IF NOT EXISTS numbers (
    id SERIAL PRIMARY KEY, 
    number VARCHAR(255),
    timestamp VARCHAR(255)
);
INSERT INTO numbers (number, timestamp) VALUES ('michal', 'awesome');
INSERT INTO numbers (number, timestamp) VALUES ('felipe', 'great');
INSERT INTO numbers (number, timestamp) VALUES ('jan', 'slow');
INSERT INTO numbers (number, timestamp) VALUES ('donald', 'duck');