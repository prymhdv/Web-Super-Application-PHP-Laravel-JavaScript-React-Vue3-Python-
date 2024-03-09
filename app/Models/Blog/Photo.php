<?php

namespace App\Models\Blog;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Photo extends Model
{
    use HasFactory;
    protected $fillable = [
        'title',
        'src', //the path you uploaded the image
        'mime_type',
        'description',
        'alt',
      ];
}
