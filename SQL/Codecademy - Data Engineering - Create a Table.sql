-- First ever use of SQL! --

CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

SELECT * FROM friends;

-- Names altered for privacy concerns idk --
INSERT INTO friends (id, name, birthday)
VALUES (2, 'Jane Doe', '2003-07-09');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Noah Sebastian', '2003-10-10');

UPDATE friends
SET name = 'Storm'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

DELETE FROM friends
WHERE id = 1;

SELECT * FROM friends;