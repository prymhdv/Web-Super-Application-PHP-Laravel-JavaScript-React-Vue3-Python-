<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class RoleSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        //
        $roles = [];

        // foreach (range(1, 2) as $index) {
        //     $roles[] = [
        //         'name' => "role $index",
        //         'name' => "administrator",
        //         'created_at' => now(),
        //         'updated_at' => now(),

        //     ];
        // }

        //>>>>the id index
        $roles[1] = [
               
                'name' => "administrator",
                'created_at' => now(),
                'updated_at' => now(),

            ];
        $roles[2] = [
           
            'name' => "subscriber",
            'created_at' => now(),
            'updated_at' => now(),

        ];
        DB::table('roles')->insert($roles);
    }
}
//php artisan db:seed --class RoleSeeder