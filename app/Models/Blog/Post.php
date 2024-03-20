<?php

 namespace App\Models\Blog;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Session\Store;
use App\Models\User;
class Post extends Model
{
    use HasFactory;
    protected $fillable = ['title', 'content', 'user_name'];
    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function likes(){
        return $this->hasMany(Like::class,'post_id');
    }
    public function tags()
    {
        return $this->belongsToMany('App\Models\Blog\Tag', 'post_tag', 'post_id', 'tag_id')->withTimestamps();
    }
    public function comments(){
        return $this->hasMany(Comment::class,'comment');
    }
    public function commentsCount(){
        return $this->comments()->count();
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
	
	 public function setTitleAttribute($value) {
        $this->attributes['title'] = strtolower($value);
    }

    public function getTitleAttribute($value) {
        return strtoupper($value);
    }
}


/*
$posts = Post::select(DB::raw('posts.*, count(*) as `aggregate`'))
    ->join('views', 'posts.id', '=', 'views.post_id')
    ->groupBy('post_id')
    ->orderBy('aggregate', 'desc')
    ->get();
*/