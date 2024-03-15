<?php

namespace App\Http\Controllers\Hottel;

use Illuminate\Http\Request;
use App\Models\Hottel\Title as Title;
use App\Models\Hottel\Client as Client;
use Illuminate\Support\Facades\DB;

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
    //============================================================
    protected function destroyClient($id) //Destruir cliente y todo lo relacionado de la bbdd
    {
        $client = Client::find($id);
        $client->reservations()->delete();
        $client->delete();
        
        // DB::delete('DELETE FROM clients WHERE id = 1');
        //     // $client->registrations()->detach();
        // // $client->delete();
        // //DB::table('clients')->foreign('user_id')->references('id')->on('users')->onDelete('cascade');
        // //$affected = DB::table('clients')->where('id', '=', $id)->delete();
        // // $affected = DB::table('clients')->delete($id);
        // //$users_to_delete = array(1, 2, 3);
        // //DB::table('users')->whereIn('id', $users_to_delete)->delete(); 
        // // User::destroy(1);
        // // User::destroy(array(1, 2, 3));
        // // User::destroy(1, 2, 3);
        // DB::delete('DELETE FROM clients WHERE id = 1');
        // //dd($client);
        // $client->delete(); //delete the client
        // DB::table('clients')->where('client_id',$id)->delete(); //delete the client_project relations which field client_id is the same that the client i just deleted.

        // // DB::table('projects')->where('id',$project_id)->delete();
        // // DB::table('project_translations')->where('project_id',$project_id)->delete();

        //     //(case A) User fields indexed by number 0,1,2..
        //     // $users_to_delete = array(
        //     //     '0'=> array('1','Frank','Smith','Whatever'), 
        //     //     '1'=> array('5','John','Johnson','Whateverelse'),
        //     //  );
     
        //     //  $ids_to_delete = array_map(function($item){ return $item[0]; }, $users_to_delete);
     
        //     //  DB::table('users')->whereIn('id', $ids_to_delete)->delete(); 
     
        //     //  //(case B) User fields indexed by key
        //     //  $users_to_delete = array(
        //     //     '0'=> array('id'=>'1','name'=>'Frank','surname'=>'Smith','title'=>'Whatever'), 
        //     //     '1'=> array('id'=>'5','name'=>'John','surname'=>'Johnson','title'=>'Whateverelse'),
        //     //  );
     
        //     //  $ids_to_delete = array_map(function($item){ return $item['id']; }, $users_to_delete);
     
        //     //  DB::table('users')->whereIn('id', $ids_to_delete)->delete(); 

        //    // $affectedRows = User::where('votes', '>', 100)->delete();
        // return redirect()->route('hotel_clients');
    }
    //============================================================
    public function index()
    { 
        //$this->destroyClient($client_id);
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

        //dd('hello');


        $data = [];

        $data['clients'] = $this->client->all();

        return view('Hottel/client/index', $data);
        //return redirect()->route('hotel_clients', $data); error
        //return redirect()->route('hotel_clients', compact($data) ); error

    }
    public function delete($client_id)
    {   //dd('hello');
        $this->destroyClient($client_id);
        $data = [];
        $data['clients'] = $this->client->all();
        return view('Hottel/client/index', $data);
        //return redirect()->route('hotel_clients', compact($data) );  error
        //return view('your_reset_password_view', compact('token', 'email'));
    }
    //============================================================
    public function export()
    {
 
        $data = [];

        $data['clients'] = $this->client->all();
        header('Content-Disposition: attachment;filename=export.xls');
        return view('Hottel/client/export', $data);

    }
    //============================================================
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

            //return redirect('hotel/clients'); ///fromroots
            return redirect()->route('hotel_clients');
        }

        $data['modify'] = 0;
        $data['titles'] = $this->titles;
        return view('Hottel/client/form', $data);
        //return route('hotel_new_client'); //address

    }
    //============================================================
    public function create()
    {
        //return __FILE__;
        return view('Hottel/client/create');

    }
    //============================================================
    public function show($client_id,Request $request)
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
        
        $request->session()->put('last_updated',$client_data->name . ' ' . $client_data->last_name);
        return view('Hottel/client/form', $data);

    }
    //============================================================
    public function modify( Request $request, $client_id, Client $client )
    {   // dd($request['save']);
        if( $request->isMethod('get') )
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
            return view('Hottel/client/form', $data);
       }
      
        if( $request->isMethod('post') && $request['save'] == 'SAVE')
        {   //return dd(redirect()->route('hotel_clients'));
            //dd($request);
            $this->validate(
                $request,
                [
                    'name' => 'required|min:3',
                    'last_name' => 'required',
                    'address' => 'required',
                    'zip_code' => 'required',
                    'city' => 'required',
                    'state' => 'required',
                    'email' => 'required',

                ]
            );
            
            //return dd(redirect()->route('hotel_clients'));
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
            //-----------------------------------------------
            //return dd(redirect()->route('hotel_clients'));
            //return redirect('service/hotel/clients/');
            return redirect()->route('hotel_clients');
            //return redirect()->route('profile', ['id' => 1]);
           // return to_route('profile', ['id' => 1]);
           //return redirect()->route('profile', [$user]);
           //return redirect()->action([HomeController::class, 'index']);
           //return redirect('/dashboard')->with('status', 'Profile updated!');
           //return back()->withInput();
           //return redirect('/home/dashboard');
            return dd('ggggggggggggggggggggggggggggg');
        }
        
        if($request->isMethod('post') && $request['delete'] == 'DELETE'){
            $this->destroyClient($client_id);
            return redirect()->route('hotel_clients');
        }
        
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