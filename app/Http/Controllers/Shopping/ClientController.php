<?php

namespace App\Http\Controllers\Shopping;

use Illuminate\Http\Request;
use App\Models\Shopping\Title as Title;
use App\Models\Shopping\Client as Client;

use App\Http\Controllers\Controller;
class ClientController extends Controller
{ 
     
    protected $titles = [];
    protected $client = [];
    public function __construct(Title $titles, Client $client)
    {
        $this->titles = $titles->all();
        $this->client = $client;
    }
    public function di()
    {
        dd($this->titles);

    }
    public function index()
    {
        //dd($this->titles);
        // $data = [];

        // $obj = new \stdClass;
        // $obj->id = 1;
        // $obj->title = 'mr';
        // $obj->name = 'john';
        // $obj->last_name = 'doe';
        // $obj->email = 'john@domain.com';
        // $data['clients'][] = $obj;
    
        // $obj = new \stdClass;
        // $obj->id = 2;
        // $obj->title = 'ms';
        // $obj->name = 'jane';
        // $obj->last_name = 'doe';
        // $obj->email = 'jane@another-domain.com';
        // $data['clients'][] = $obj;
        // return view('hotel/client/index', $data);

        $data = [];

        $data['clients'] = $this->client->all();
        return view('Hottel/client/index', $data);

    }
    public function newClient(Request $request, Client $client)
    {
        
        // //return __FILE__;
        // //return __METHOD__;
        // $data = [];
        // $data['titles'] = $this->titles;
        // $data['modify'] = 0;
        // //return view('hotel/client/newClient',$data);
        // return view('hotel/client/form',$data);

        $data = [];

        $data['title'] = $request->input('title');
        $data['name'] = $request->input('name');
        $data['last_name'] = $request->input('last_name');
        $data['address'] = $request->input('address');
        $data['zip_code'] = $request->input('zip_code');
        $data['city'] = $request->input('city');
        $data['state'] = $request->input('state');
        $data['email'] = $request->input('email');

        // $data['modify'] = 0;
        // $data['titles'] = $this->titles;
        


        if( $request->isMethod('post') )
        {
            //dd($data);
            $this->validate(
                $request,
                [
                    'name' => 'required|min:5',
                    'last_name' => 'required',
                    'address' => 'required',
                    'zip_code' => 'required',
                    'city' => 'required',
                    'state' => 'required',
                    'email' => 'required',

                ]
            );
            
            $client->insert($data);

            return redirect('Hottel/client/');
        }
        
        return view('Hottel/client/form', $data);

    }
    
    public function create()
    {
        return __FILE__;
        return view('Hottel/client/create');

    }
    public function show($client_id)
    {

        // // return __FILE__;
        // //return __METHOD__ . ':' . $client_id;
        // $data = [];
        // $data['titles'] = $this->titles;
        // $data['modify'] = 1;
        // //return view('hotel/client/newClient',$data);
        // return view('hotel/client/form',$data);

        // //return view('hotel/client/show');
 
        $data = []; $data['client_id'] = $client_id;
        $data['titles'] = $this->titles;
        $data['modify'] = 1;
        $client_data = $this->client->find($client_id);
        $data['name'] = $client_data->name;
        $data['last_name'] = $client_data->last_name;
        $data['title'] = $client_data->title;
        $data['address'] = $client_data->address;
        $data['zip_code'] = $client_data->zip_code;
        $data['city'] = $client_data->city;
        $data['state'] = $client_data->state;
        $data['email'] = $client_data->email;
        
        return view('Hottel/client/form', $data);

    }
    public function modify( Request $request, $client_id, Client $client )
    {
        $data = [];

        $data['title'] = $request->input('title');
        $data['name'] = $request->input('name');
        $data['last_name'] = $request->input('last_name');
        $data['address'] = $request->input('address');
        $data['zip_code'] = $request->input('zip_code');
        $data['city'] = $request->input('city');
        $data['state'] = $request->input('state');
        $data['email'] = $request->input('email');
        


        if( $request->isMethod('post') )
        {
            //dd($data);
            $this->validate(
                $request,
                [
                    'name' => 'required|min:5',
                    'last_name' => 'required',
                    'address' => 'required',
                    'zip_code' => 'required',
                    'city' => 'required',
                    'state' => 'required',
                    'email' => 'required',

                ]
            );

            $client_data = $this->client->find($client_id);

            $client_data->title = $request->input('title');
            $client_data->name = $request->input('name');
            $client_data->last_name = $request->input('last_name');
            $client_data->address = $request->input('address');
            $client_data->zip_code = $request->input('zip_code');
            $client_data->city = $request->input('city');
            $client_data->state = $request->input('state');
            $client_data->email = $request->input('email');

            $client_data->save();

            return redirect('Hottel/client/');
        }
        
        return view('Hottel/client/form', $data);
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