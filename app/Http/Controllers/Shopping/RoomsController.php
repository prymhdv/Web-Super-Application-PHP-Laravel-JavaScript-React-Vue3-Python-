<?php

namespace App\Http\Controllers\Shopping;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
class RoomsController extends Controller
{
    //
    public function checkAvailableRooms()
    {
        return view('Hottel/rooms/checkAvailableRooms');
    }
}
