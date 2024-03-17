<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Task extends Model
{             //////php artisan make:model Task -a
    use HasFactory;

    protected $fillable = ['name'];
}
