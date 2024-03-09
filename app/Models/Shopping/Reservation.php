<?php

namespace App\Models\Shopping;

use Illuminate\Database\Eloquent\Model;

class Reservation extends Model
{
    //
    public function client()
    {
        return $this->belongsTo('App\Models\Shopping\Client', 'client_id', 'id');
    }

    public function room()
    {
        return $this->belongsTo('App\Models\Shopping\Room', 'room_id', 'id');
    }
}
