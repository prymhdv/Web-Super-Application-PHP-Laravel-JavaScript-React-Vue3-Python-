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
        //
        DB::table('users')->insert(
            [
                'name'      =>'admin',
                'email'     =>'admin@example.com',
                'password'  =>bcrypt('admin'),
                  
           ]
             
       );
        
    }
}
