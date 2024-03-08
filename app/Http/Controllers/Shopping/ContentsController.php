<?php

namespace App\Http\Controllers\Shopping;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
class ContentsController extends Controller
{
    //
    public function index()
    {

        return __METHOD__;
    
        
    }
    public function home()
    {
        $data = [];
        $data['version'] = '0.1.2';
        return view('Hottel/contents/home', $data);
    }
}
