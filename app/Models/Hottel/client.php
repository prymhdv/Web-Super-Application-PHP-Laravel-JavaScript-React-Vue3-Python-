<?php

namespace App\Models\Hottel;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Client  extends Model
{
    use HasFactory;


    public function reservations()
    {
        return $this->hasMany('App\Models\Hottel\Reservation');
    }
}


