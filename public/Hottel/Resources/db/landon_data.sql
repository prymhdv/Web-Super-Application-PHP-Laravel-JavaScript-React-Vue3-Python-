INSERT INTO rooms (name, floor, description) VALUES ( '101', 1, '');
INSERT INTO rooms (name, floor, description) VALUES ( '102', 1, '');
INSERT INTO rooms (name, floor, description) VALUES ( '201', 2, '');
INSERT INTO rooms (name, floor, description) VALUES ( '202', 2, '');

INSERT INTO clients (title, name, last_name, address, zip_code, city, state, email)
VALUES
('mr', 'Vincent', 'Vega', 'Fake Street 123', '11820', 'Tulsa', 'OK', 'john@email.com');

INSERT INTO clients (title, name, last_name, address, zip_code, city, state, email)
VALUES
('mrs', 'Mia', 'Wallace', 'Another Fake Street 234', '06030', 'McAlester', 'OK', 'jane@email.com');

 
 INSERT INTO reservations ( date_in, date_out, client_id, room_id )
 VALUES
 ( '2017-01-01', '2017-01-05', (SELECT id FROM clients LIMIT 1), (SELECT id FROM rooms LIMIT 1) )