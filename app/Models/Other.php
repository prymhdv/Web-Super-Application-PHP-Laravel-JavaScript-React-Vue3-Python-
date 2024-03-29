<?php

namespace App\Models;

use App\Models\Blog\Photo;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Other extends Model
{
    use HasFactory;
    public function photo()
    {
        return $this->belongsTo(Photo::class,'photo_id');
    }
}
