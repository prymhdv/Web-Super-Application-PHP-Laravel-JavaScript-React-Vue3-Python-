<?php

namespace App\Http\Controllers\Hottel;

use Illuminate\Http\Request;
//use Illuminate\Support\Facades\Input; v.5 off
use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Request as Input;
class ContentsController extends Controller
{
    //
    public function index()
    {

        return __METHOD__;
    
        
    }
    public function home(Request $request)
    {
        $data = [];
        $data['version'] = '0.1.2';
        $last_updated = $request->session()->has('last_updated') ?
        $request->session()->pull('last_updated') : 'none';

        $data['last_updated'] = $last_updated;
        return view('Hottel/contents/home', $data);
    }

    public function upload(Request $request)
    {
        $data = [];
         if($request->isMethod('post'))
         {
            $this->validate(
                $request,[
                    'image_upload' =>'mimes:jpeg,bmp,png'
                ]
                );
                Input::file('image_upload')->move('Hottel\images','attractions.jpg');
                 
                return redirect('/');

         }
        return view('Hottel/contents/upload', $data);
    }
}
