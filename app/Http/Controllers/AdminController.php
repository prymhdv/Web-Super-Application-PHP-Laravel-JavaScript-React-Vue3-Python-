<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use PHPUnit\Framework\Attributes\IgnoreFunctionForCodeCoverage;

class AdminController extends Controller
{
    //


    public function __construct()
    {

        $this->middleware('IsAdmin');
    }

    public function index()
    {

        return "you are an administrator because you are seeing this page";
    }
    public function Hello()
    {
        if (Auth::hasUser()) {

            $user = Auth::user();

            // some constrains based on the $user object
        }
        $user = new User;
        $user = auth()->user();
        $user = Auth::User(); //Unable to access methods on User model using Auth::user()
        /** @var App\Models\User $user */
        $user = Auth::user();

        $id = Auth::id();
        //$user = $request->user();
        if (!Auth::check()) {
            redirect()->back();
        }
        // if ($user !== null && $user instanceof App\Models\User) {
        //     $user->isAdmin();
        // }
        if ($user !== null && method_exists($user, 'isAdmin')) {
            $user->isAdmin(); //
            //dd('$user !== null && method_exists   $user->isAdmin();');
        }
        if ($user->isAdmin()) {
            //dd('$user->isAdmin()');
            return ' AdminControler:: $user->isAdmin() isAdmin hello midleware is here  && Heloo you are role administrator';
        }
        //dd('$user !== null && method_exists');
        return 'AdminControler:: hello midleware is here  && Heloo you are role administrator   $user !== null && method_exists';
    }
}
