<?php

namespace App\Models\Blog;

use Illuminate\Database\Eloquent\Model;

class Tag extends Model
{
    public function posts()
    {
        return $this->belongsToMany('App\Models\Blog\Post', 'post_tag', 'tag_id', 'post_id')->withTimestamps();
    }
}
