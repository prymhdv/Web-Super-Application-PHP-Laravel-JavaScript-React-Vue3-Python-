<?php

use Illuminate\Database\Seeder;

class TagTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $tag = new \App\Models\Tag();
        $tag->name = 'Tutorial';
        $tag->save();

        $tag = new \App\Models\Tag();
        $tag->name = 'Industry News';
        $tag->save();
    }
}
