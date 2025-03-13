-- Create table to store animals
CREATE TABLE Animals (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    name VARCHAR(100),
    age INT,
    favorite_food VARCHAR(100)
);

-- Create table to store the names history for each animal
CREATE TABLE AnimalNames (
    id SERIAL PRIMARY KEY,
    animal_id INT,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES Animals(id)
);

-- Sample insert statements for a cat
INSERT INTO Animals (type, name, age, favorite_food) VALUES ('Cat', 'Felix', 7, 'Salmon');
INSERT INTO AnimalNames (animal_id, name) VALUES (1, 'Felix');

-- Sample insert statements for a dog
INSERT INTO Animals (type, name, age, favorite_food) VALUES ('Dog', 'Rover', 8, 'Chicken');
INSERT INTO AnimalNames (animal_id, name) VALUES (2, 'Rover');

-- Sample insert statements for nameless cats
INSERT INTO Animals (type, name, age, favorite_food) VALUES ('Cat', NULL, 6, NULL);
INSERT INTO AnimalNames (animal_id, name) VALUES (3, NULL);

INSERT INTO Animals (type, name, age, favorite_food) VALUES ('Cat', NULL, 5, NULL);
INSERT INTO AnimalNames (animal_id, name) VALUES (4, NULL);

INSERT INTO Animals (type, name, age, favorite_food) VALUES ('Cat', NULL, 9, NULL);
INSERT INTO AnimalNames (animal_id, name) VALUES (5, NULL);

-- Sample insert statements for nameless dogs
INSERT INTO Animals (type, name, age, favorite_food) VALUES ('Dog', NULL, 7, NULL);
INSERT INTO AnimalNames (animal_id, name) VALUES (6, NULL);

INSERT INTO Animals (type, name, age, favorite_food) VALUES ('Dog', NULL, 6, NULL);
INSERT INTO AnimalNames (animal_id, name) VALUES (7, NULL);

INSERT INTO Animals (type, name, age, favorite_food) VALUES ('Dog', NULL, 8, NULL);
INSERT INTO AnimalNames (animal_id, name) VALUES (8, NULL);
