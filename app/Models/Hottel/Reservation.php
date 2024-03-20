<?php

namespace App\Models\Hottel;

use Illuminate\Database\Eloquent\Model;

class Reservation extends Model
{
    //
    public function client()
    {
        return $this->belongsTo('App\Models\Hottel\Client', 'client_id', 'id');
    }

    public function room()
    {
        return $this->belongsTo('App\Models\Hottel\Room', 'room_id', 'id');
    }
}
