<?php
namespace Database\seeders\Blog;


use Illuminate\Support\Facades\DB;
use Illuminate\Database\Seeder;

class PostTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        // $post = new \App\Models\Blog\Post([
        //     'title' => 'Learning Something',
        //     'content' => 'This blog post will get you right on track with Something!'
        // ]);
        // $post->save();

        // $post = new \App\Models\Blog\Post([
        //     'title' => 'Something else',
        //     'content' => 'Some other content'
        // ]);
        // $post->save();

        DB::table('posts')->insert(
            [
           'title'=>'Learning Something Learning Something',
           'content'=>'This blog post will get you right on track with Something! This blog post will get you right on track with Something!',
           ]
             
       ); 
       
    }
}
