<?php

namespace App\Http\Controllers\Shopping;

use Illuminate\Http\Request;
use App\Models\Shopping\Title as Title;
use App\Http\Controllers\Controller;
class ClientController extends Controller
{ 
     
    protected $titles = [];
    public function __construct(Title $titles)
    {
        $this->titles = $titles->all();
    }
    public function di()
    {
        dd($this->titles);

    }
    public function index()
    {
        //dd($this->titles);
        $data = [];

        $obj = new \stdClass;
        $obj->id = 1;
        $obj->title = 'mr';
        $obj->name = 'john';
        $obj->last_name = 'doe';
        $obj->email = 'john@domain.com';
        $data['clients'][] = $obj;
    
        $obj = new \stdClass;
        $obj->id = 2;
        $obj->title = 'ms';
        $obj->name = 'jane';
        $obj->last_name = 'doe';
        $obj->email = 'jane@another-domain.com';
        $data['clients'][] = $obj;
        return view('Hottel/client/index', $data);

    }
    public function newClient()
    {
        
        //return __FILE__;
        //return __METHOD__;
        return view('Hottel/client/newClient');

    }
    
    public function create()
    {
        //return __FILE__;
        return view('Hottel/client/create');

    }
    public function show($client_id)
    {

        // return __FILE__;
        //return __METHOD__ . ':' . $client_id;
        return view('Hottel/client/show');

    }
}




/*
<?php
namespace App\Http\Controllers\test;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;

class TestController extends Controller
{
    public function getTest()
    {
        return "Yes";
    }
}
Route::get('/test','test\TestController@getTest');

*/