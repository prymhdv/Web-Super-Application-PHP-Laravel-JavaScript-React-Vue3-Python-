<?php

namespace Database\seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
class RoomTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        //
        DB::table('rooms')->insert(
            [
                'name'=>'201',
                'floor'=>1,
                'description'=>'201'
            ]
            );
        DB::table('rooms')->insert(
            [
                'name'=>'202',
                'floor'=>1,
                'description'=>'202'
            ]);
        DB::table('rooms')->insert(
            [
                'name'=>'303',
                'floor'=>1,
                'description'=>'303'
            ]
            );
    }
}
