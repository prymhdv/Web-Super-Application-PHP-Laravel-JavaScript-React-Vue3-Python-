<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;
use Illuminate\Support\Facades\Auth;

class SignController extends Controller
{
    public function signIn(Request $request)
    {   //dd('SignController other.about Our own auth!');
       
        //-------------------------------------
        $this->validate($request, [
            'email' => 'required|email',
            'password' => 'required'
        ]);
        //-------------------------------------
        if (Auth::attempt([
            'email' => $request->input('email'),
            'password' => $request->input('password')
        ], $request->has('remember'))) {
            //return redirect()->route('admin.index');
           // dd(" SignController hotel_clients");
           if(!Auth::check()) dd('SignController other.about Our own auth! not login');
           //else dd('SignController other.about Our own auth! logined');
           //--------------------------------------------------------------------------
            //return redirect()->route('other.about.Route');
            //return redirect()->back();
            //{{ url()->previous() }}
            return back();
        }
        return redirect()->back()->with('fail', 'Authentication failed!');
    }
    public function signUp(Request $request)
    { 
         
        if(!Auth::user())
        {
            return redirect()->route('register');
        }
        User::create([
            'name' => $request['name'],
            'email' => $request['email'],
            'password' => bcrypt($request['password']),
        ]);
        return redirect()->back()->with('Succesfully', 'Authentication Succesfully!');
    }
    public function logout(Request $request)
    { 
        Auth::guard('user')->logout();
        return redirect()->route('/');
    }
}
