-- where are you my world
-- creates a trigger that decreases the
-- quantity of an item after adding a new order.
DELIMITER $$
DROP TRIGGER IF EXISTS DECREASE;
CREATE TRIGGER DECREASE
AFTER INSERT
ON orders
BEGIN
    UPDATE items
    set quantity = quantity - NEW.number
    WHERE name=NEW.item_name;
END $$
DELIMITER ;
