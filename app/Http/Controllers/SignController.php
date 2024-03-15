<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests;
use Illuminate\Support\Facades\Auth;

class SignController extends Controller
{
    public function signIn(Request $request)
    {   //dd('Our own auth!');
        $this->validate($request, [
            'email' => 'required|email',
            'password' => 'required'
        ]);
        if (Auth::attempt([
            'email' => $request->input('email'),
            'password' => $request->input('password')
        ], $request->has('remember'))) {
            //return redirect()->route('admin.index');
            return redirect()->route('hotel_clients');
            
        }
        return redirect()->back()->with('fail', 'Authentication failed!');
    }
    public function signUp(Request $request)
    {

        $this->validate($request, [
            'email' => 'required|email',
            'password' => 'required'

        ]);
        return redirect()->back();
    }
}
