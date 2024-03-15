<?php

namespace Database\seeders\Hottel;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;


class ClientTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        //
        DB::table('clients')->insert(
             [
            'title'=>'mr',
            'name'=>'John',
            'last_name'=>'Doe',
            'address'=>'Street 302',
            'zip_code'=>'06521',
            'city'=>'Tusla',
            'state'=>'Ok',
            'email'=>'John@example.com',
            ]
              
        );
        DB::table('clients')->insert(
            [
           'title'=>'mrs',
           'name'=>'jane',
           'last_name'=>'Doe',
           'address'=>'Another Street 334',
           'zip_code'=>'45451',
           'city'=>'Los Angeles',
           'state'=>'CA',
           'email'=>'Jane@example.com',
           ]
             
       );
        
    }
}
