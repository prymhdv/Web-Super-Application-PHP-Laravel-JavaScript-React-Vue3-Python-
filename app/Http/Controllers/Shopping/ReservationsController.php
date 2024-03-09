<?php

namespace App\Http\Controllers\Shopping;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
///should go affter name space
use App\Models\Shopping\Client as Client;
use App\Models\Shopping\Room as Room;
use App\Models\Shopping\Reservation as Reservation;

class ReservationsController extends Controller
{
    //
    public function bookRoom($client_id, $room_id, $date_in, $date_out)
    {
        dd($client_id, $room_id, $date_in, $date_out);
      
        $reservation = new Reservation();
        $client_instance = new Client();
        $room_instance = new Room();

        $client = $client_instance->find($client_id);
        $room = $room_instance->find($room_id);
        $reservation->date_in = $date_in;
        $reservation->date_out = $date_out;

        $reservation->room()->associate($room);
        $reservation->client()->associate($client);
        if ($room_instance->isRoomBooked($room_id, $date_in, $date_out)) {
            abort(405, 'Trying to book an already booked room');
        }
        $reservation->save();

        //return redirect()->rout('hotel_client');
        return redirect()->route('hotel_clients');
        //return view('Hottel/reservations/bookRoom');
    }
}
