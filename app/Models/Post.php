<?php

 namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Session\Store;
class Post extends Model
{
    use HasFactory;
    protected $fillable = ['title', 'content'];
   
    public function likes(){
        return $this->hasMany(Like::class,'post_id');
    }
    public function tags()
    {
        return $this->belongsToMany('App\ModelS\Tag', 'post_tag', 'post_id', 'tag_id')->withTimestamps();
    }

    public function getIndex(Store $session)
    {
        $posts = Post::all();
        return view('blog.index', ['post' => $posts]);
    }
    
    public function getPosts($session)
    {
        if (!$session->has('posts')) {
            $this->createDummyData($session);
        }
        return $session->get('posts');
    }

    public function getPost($session, $id)
    {
        if (!$session->has('posts')) {
            $this->createDummyData($session);
        }
        return $session->get('posts')[$id];
    }

    public function addPost($session, $title, $content)
    {
        if (!$session->has('posts')) {
            $this->createDummyData($session);
        }
        $posts = $session->get('posts');
        array_push($posts, ['title' => $title, 'content' => $content]);
        $session->put('posts', $posts);
    }

    public function editPost($session, $id, $title, $content)
    {
        $posts = $session->get('posts');
        $posts[$id] = ['title' => $title, 'content' => $content];
        $session->put('posts', $posts);
    }

    private function createDummyData($session)
    {
        $posts = [
            [
                'title' => 'Learning Laravel',
                'content' => 'This blog post will get you right on track with Laravel!'
           
            ],
            [
                'title' => 'Something else',
                'content' => 'Some other content'
            ]
        ];
        $session->put('posts', $posts);
    }
}
