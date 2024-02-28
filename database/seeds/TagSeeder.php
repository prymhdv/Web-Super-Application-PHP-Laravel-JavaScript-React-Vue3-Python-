<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class TagSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        //
        $tag = new \App\Models\Tag();
        $tag->name = 'Tutorial';
        $tag->save();

        $tag = new \App\Models\Tag();
        $tag->name = 'Industry News';
        $tag->save();
    }
}
