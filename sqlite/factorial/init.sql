BEGIN TRANSACTION;
PRAGMA recursive_triggers = 1; 
CREATE TABLE factorials (n INTEGER PRIMARY KEY, n_factorial INTEGER); 
CREATE VIEW factorial AS SELECT n, n_factorial FROM factorials; 
CREATE TRIGGER factorial_ins INSTEAD OF INSERT ON factorial BEGIN 
    SELECT RAISE(FAIL, "n must be non-negative") WHERE NEW.n < 0; 
    SELECT RAISE(IGNORE) WHERE EXISTS (SELECT f.n FROM factorials f 
WHERE f.n = NEW.n); 
    INSERT INTO factorials SELECT NEW.n, 1 WHERE NEW.n < 2 AND NOT 
EXISTS (SELECT f.n FROM factorials f WHERE f.n = NEW.n); 
    INSERT INTO factorial SELECT NEW.n - 1, NULL WHERE NEW.n > 0 AND 
NOT EXISTS (SELECT f.n FROM factorials f WHERE f.n = NEW.n - 1); 
    INSERT INTO factorials SELECT NEW.n, NEW.n * (SELECT f.n_factorial 
FROM factorials f WHERE f.n = NEW.n - 1) WHERE NEW.n > 0 AND EXISTS 
(SELECT f.n FROM factorials f WHERE f.n = NEW.n - 1) AND NOT EXISTS 
(SELECT f.n FROM factorials f WHERE f.n = NEW.n); 
END; 
COMMIT;
