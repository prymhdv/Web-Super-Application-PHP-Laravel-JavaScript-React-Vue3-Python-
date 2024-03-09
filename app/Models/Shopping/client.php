<?php

namespace App\Models\Shopping;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class client  extends Model
{
    use HasFactory;


    public function reservations()
    {
        return $this->hasMany('App\Reservation');
    }
}


