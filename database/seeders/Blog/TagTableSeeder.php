<?php
namespace Database\seeders\Blog;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
class TagTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $tag = new \App\Models\Blog\Tag();
        $tag->name = 'Tutorial';
        $tag->save();

        $tag = new \App\Models\Blog\Tag();
        $tag->name = 'Industry News';
        $tag->save();
    }
}
