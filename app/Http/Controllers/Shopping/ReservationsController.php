<?php

namespace App\Http\Controllers\Shopping;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
class ReservationsController extends Controller
{
    //
    public function bookRoom()
    {
        return view('Hottel/reservations/bookRoom');
    }
}
