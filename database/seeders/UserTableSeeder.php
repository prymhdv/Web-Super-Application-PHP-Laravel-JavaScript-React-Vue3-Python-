<?php

namespace Database\seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class UserTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
         
        $users = [];

        foreach (range(1, 5) as $index) {
            $users[] = [
                'name' => "users $index",
                'email'     => "admin".$index."@example.com",
                'password'  => bcrypt('admin'),
                'created_at' => now(),
                'updated_at' => now(),
                'role_id' => '2',          //--<<<<<forigen must declined!!!

            ];
        }
        DB::table('users')->insert($users);


        DB::table('users')->insert(
            [
                'role_id' => '1',
                'name' => 'admin',
                'email' => 'admin@admin.com',
                'password' => bcrypt('123456'),
                'created_at' => now(),
                'updated_at' => now(),
            ]
        );
        DB::table('users')->insert(
            [
                'role_id' => '2',
                'name' => 'qqq',
                'email' => 'qqq@qqq.com',
                'password' => bcrypt('123456'),
                'created_at' => now(),
                'updated_at' => now(),
            ]
        );
    }
}
