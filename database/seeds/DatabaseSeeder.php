<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class DatabaseSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        // $this->call(PostTableSeeder::class);
        $this->call(TagTableSeeder::class);

        DB::unprepared("
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
                        ( '2027-01-01', '2027-01-05', (SELECT id FROM clients LIMIT 1), (SELECT id FROM rooms LIMIT 1) )
                        ");


        DB::unprepared("
            SELECT r.id, r.name 
                FROM rooms as r
                WHERE r.id NOT IN ( 
                        SELECT b.room_id 
                        FROM reservations b
                        WHERE NOT (
                                    b.date_out < '2017-01-02' OR
                                    b.date_in > '2017-01-03'
                                    )
                )
        ");
    }
}
 //if(!Schema::hasTable('users')) 

 
/// DB::statement("your query")
///  $cards = DB::select("SELECT
///         cards.id_card,
//         cards.hash_card,
//         cards.`table`,
//         users.name,
//         0 as total,
//         cards.card_status,
//         cards.created_at as last_update
//     FROM cards
//     LEFT JOIN users
//     ON users.id_user = cards.id_user
//     WHERE hash_card NOT IN ( SELECT orders.hash_card FROM orders )
//     UNION
//     SELECT
//         cards.id_card,
//         orders.hash_card,
//         cards.`table`,
//         users.name,
//         sum(orders.quantity*orders.product_price) as total, 
//         cards.card_status, 
//         max(orders.created_at) last_update 
//     FROM menu.orders
//     LEFT JOIN cards
//     ON cards.hash_card = orders.hash_card
//     LEFT JOIN users
//     ON users.id_user = cards.id_user
//     GROUP BY hash_card
//     ORDER BY id_card ASC");
