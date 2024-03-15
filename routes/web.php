<?php

use App\Http\Controllers\Auth2\AuthenticatedSessionController;
use App\Http\Controllers\Auth\LoginController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\Hottel\Auth as Hottel_Auth;
use Doctrine\DBAL\Schema\View;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Crypt;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Redirect;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\OrderController;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| This file is where you may define all of the routes that are handled
| by your application. Just tell Laravel the URIs it should respond
| to using a Closure or controller method. Build something great!
|
*/
/*------------------------------------------------------------*/
//                          main
/*------------------------------------------------------------*/
Route::group(['prefix'=>''],function(){

    Route::get('about', function ()     {   return view('other.about');})->name('other.about');
    Route::get('/', function ()         {   return view('main.index2');})->name('main.index2');
    Route::get('Products', function ()  {   return view('Products.index');})->name('Products.index');
});



/*------------------------------------------------------------*/
//                          Dev
/*------------------------------------------------------------*/
Route::group(['prefix'=>'dev'],function(){

    Route::get('testJS', function ()    {   return view('main.testJS');})->name('testJS');
    Route::get('VueJs', function ()     {   return view('main.VueJs');})->name('VueJs');
    Route::get('ReactJs', function ()   {   return view('main.ReactJs');})->name('ReactJs');
    
    Route::group(['prefix' => 'bootstrap'],function(){
        Route::get('/', function ()             {   return view('main.bootstrap');})->name('bootstrap');
        Route::get('/Dashboard', function ()    {   return view('main.bootstrap.Dashboard');})->name('bootstrap.Dashboard'); 
        Route::get('/Blog', function ()         {   return view('main.bootstrap.Blog');})->name('bootstrap.Blog');
        Route::get('/Pricing', function ()      {   return view('main.bootstrap.Pricing');})->name('bootstrap.Pricing');
    });
    /*------------------------------------------------------------*/
    //            Vite Vue3 app2     Vite react app1    
    /*------------------------------------------------------------*/
    Route::group(['prefix'=>'vite'],function(){

        Route::group(['prefix'=>'vue3'],function(){
            
            Route::group(['prefix'=>'app2'],function(){
                Route::get('/ViteVue3app2', 'HomeController@index');
                Route::any('/ViteVue3app2/spa/{any?}', 'SpaController@spa')->where(['any' => '.*']);
                Route::resource('project', 'ProjectController',['except' => ['create']]);
                Route::get('ViteVue3app2/projects/', 'ProjectController@projects');
                Route::resource('note', 'NoteController',['except' => ['create']]);
                Route::get('ViteVue3app2/notes/', 'NoteController@notes');
                Route::post('ViteVue3app2/contact', 'SpaController@addContact');
                Route::get('ViteVue3app2/contacts', 'SpaController@contacts');
                Route::get('ViteVue3app2/skills', 'SpaController@skills');
                Route::get('ViteVue3app2/languages', 'SpaController@languages');

            });
            Route::group(['prefix'=>'app3'],function(){
                Route::post('login', [AuthenticatedSessionController::class, 'login']);
                Route::post('register', [AuthenticatedSessionController::class, 'register']);
                Route::post('logout', [AuthenticatedSessionController::class, 'logout']);
                Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');
                Route::view('/ViteVue3App3views/{any?}', 'main-view')->name('dashboard')->where('any', '.*');
                Route::get('/main-view')->name('dashboard')->where('any', '.*');
            });
        });
        Route::group(['prefix'=>'react'],function(){


        });  
    });

});
/*------------------------------------------------------------*/
//                          Blog
/*------------------------------------------------------------*/
Route::get('/blog', [
    'uses' => 'PostController@getBlog',
    'as' => 'blog.index'
]);

Route::get('post/{id}', [
    'uses' => 'PostController@getPost',
    'as' => 'blog.post'
]);
Route::get('post/{id}/like', [
    'uses' => 'PostController@getLikePost',
    'as' => 'blog.post.like'
]);


// Route::group(['prefix' => 'admin','middleware' => ['auth' ,'guest']], function () {
Route::group(['prefix' => 'BlogPost', 'middleware' => ['auth']], function () {
    Route::get('', [
        'uses' => 'PostController@Index',
        'as' => 'BlogPost.index',
        // 'middleware' => 'auth'
    ]);

    Route::post('create', [
        'uses' => 'PostController@Create',
        'as' => 'BlogPost.create'
    ]);

    Route::get('edit/{id}', [
        'uses' => 'PostController@Edit',
        'as' => 'BlogPost.edit'
    ]);

    Route::get('delete/{id}', [
        'uses' => 'PostController@Delete',
        'as' => 'BlogPost.delete'
    ]);

    Route::post('edit', [
        'uses' => 'PostController@Update',
        'as' => 'BlogPost.update'
    ]);
});
/*------------------------------------------------------------*/
//                   Authentification
/*------------------------------------------------------------*/
Auth::routes();

Route::group(['prefix' => 'Sign'],function(){
    
    Route::get('register',[
        'uses' => 'SignController@signUp',
        'as'   => 'userSignUp.index'
    ]);
    Route::post('login', [
        'uses' => 'SignController@signIn',
        'as' => 'auth.signin'
    ]);

});

/*------------------------------------------------------------*/
//                          Servises
/*------------------------------------------------------------*/
//Route::patch('/shop', function () {return view('main.testHottel');})->name('testHottel');
// Route::get('/hotel/shop', function () {return view('main.testHottel');})->name('hotel_home');
//Route::middleware('auth')->
Route::group(['prefix'=>'service'],function(){  //controlpannel need login
    /*------------------------------------------------------------*/
    //                          Hottel
    /*------------------------------------------------------------*/
    Route::group(['prefix'=>'hotel'],function(){ 

    Route::get('/', 'Hottel\ContentsController@home')->name('hotel_home');
    Route::get('upload','Hottel\ContentsController@upload')->name('upload');
    Route::post('upload','Hottel\ContentsController@upload')->name('upload');

    Route::get('clients', 'Hottel\ClientController@index')->name('hotel_clients');
    Route::get('clients/delete/{client_id}', 'Hottel\ClientController@delete')->name('hotel_clients_delete');
    // Route::get('/hotel/clients', 'Hottel\ClientController@index')->name('hotel_clients')->middleware('auth');
    Route::get('clients/new', 'Hottel\ClientController@newClient')->name('hotel_new_client');
    Route::post('clients/new', 'Hottel\ClientController@newClient')->name('hotel_create_client');
    Route::get('clients/{client_id}', 'Hottel\ClientController@show')->name('hotel_show_client');
    Route::post('clients/{client_id}', 'Hottel\ClientController@modify')->name('hotel_update_client');
    //----------------
    Route::get('reservations/{client_id}', 'Hottel\RoomsController@checkAvailableRooms')->name('hotel_check_room');
    Route::post('reservations/{client_id}', 'Hottel\RoomsController@checkAvailableRooms')->name('hotel_check_room');
    
    Route::get('book/room/{client_id}/{room_id}/{date_in}/{date_out}', 'Hottel\ReservationsController@bookRoom')->name('hotel_book_room');

    Route::get('export','Hottel\ClientController@export');
   
    Route::get('di', 'Hottel\ClientController@di');
    });

    /*------------------------------------------------------------*/
    //                          Some utilis
    /*------------------------------------------------------------*/
    Route::group(['prefix'=>'Utilities'],function(){ 
        
        Route::get('/facades/db', function () {
            return DB::select('SELECT * FROM table');
        });
        Route::get('/facades/encrypt', function () {return Crypt::encrypt('123456789');
            //eyJpdiI6ImtESks3a3pLNEhLRnhRaFN6eTlsbHc9PSIsInZhbHVlIjoiS3hsd0RWT2YzaGZSV1R1aE1vSitYc0dlcmlna2NTZ096K04rNTlsRVhTUT0iLCJtYWMiOiJhYmQ0NzAzYjQ4ZWZhODg0ZDE0MWI0YTMxMTcxZjZjYjE3N2NiYzFlNDdlZTA3ZDVhOTc3NWVjNjEzNDExOGJkIiwidGFnIjoiIn0=
        });
        Route::get('/facades/decrypt', function () {
            return Crypt::decrypt('eyJpdiI6ImtESks3a3pLNEhLRnhRaFN6eTlsbHc9PSIsInZhbHVlIjoiS3hsd0RWT2YzaGZSV1R1aE1vSitYc0dlcmlna2NTZ096K04rNTlsRVhTUT0iLCJtYWMiOiJhYmQ0NzAzYjQ4ZWZhODg0ZDE0MWI0YTMxMTcxZjZjYjE3N2NiYzFlNDdlZTA3ZDVhOTc3NWVjNjEzNDExOGJkIiwidGFnIjoiIn0');
            //=
        });
        //Hottel_Auth::routes();
        Route::get('/generate/password', function() { return bcrypt('123456789'); } )->name('d');
    });

});
/*------------------------------------------------------------*/
//                          Api auth
/*------------------------------------------------------------*/
Route::prefix('auth')->group(function(){

    Route::post('/Login2',LoginController::class);

});
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
//                          main test
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
//Route::get('/address', ['controllerName','functionName'])->name('name');   
//Route::get('/address', functionInline)->name('name');  
Route::get('/root',  function () {  return 'hello pouriya';} )->name('root');  // in constructor cheacked auth
Route::get('/root/{id}',  function (string $id) {return 'User Code: '.$id;})->name('root{id}')->where('id', '[0-9]+');  // in constructor cheacked auth

Route::group(['test'],function(){
    Route::get('test', function ()              {   return view('main.bootstrap');})->name('bootstrap');
    Route::get('test/Dashboard', function ()    {   return view('main.bootstrap.Dashboard');})->name('bootstrap.Dashboard'); 
    Route::get('test/Blog', function ()         {   return view('main.bootstrap.Blog');})->name('bootstrap.Blog');
    Route::get('test/Pricing', function ()      {   return view('main.bootstrap.Pricing');})->name('bootstrap.Pricing');

});
Route::group(['prefix' => 'test'],function(){         //prefix make addres injected look like  test/root

    Route::get('/root',             function ()                 {return 'hello pouriya ' . Route::currentRouteName();} )->name('test_root');  // in constructor cheacked auth          http://127.0.0.1:8000/test/root/cyj
    Route::get('/root/{name}',      function (string $name,) {return 'User Name: '.$name;})->name('test_root{name}')->where('name', '[A-Za-z]+');  // in constructor cheacked auth
    Route::get('/root/{id}',        function (string $id) {return 'User Code: '.$id;})->name('test_root{id}')->where('id', '[1-9]+');  // in constructor cheacked auth
    Route::get('/root/{name}{id}',  function (string $name,string $id) {return 'User Name: '.$name . '     User Code: '.$id;})->name('test_root{name}{id}')->where(['id', '[1-9]','name', '[A-Za-z]']);  // in constructor cheacked auth

});
Route::prefix('admin2')->group(function(){

    Route::post('/login',LoginController::class);  ///just constructor work!!  not working with out function define
    Route::get('/login',[LoginController::class,'index'])->name('admin2_login');   

});
Route::get('/home', [HomeController::class, 'index'])->name('home');  // in constructor cheacked auth
//------> forece to auth
Route::middleware(['OrderController','auth'])->group(function(){
    Route::get('/root',             function ()                 {return 'hello pouriya ' . Route::currentRouteName();} )->name('test_root');  // in constructor cheacked auth          http://127.0.0.1:8000/test/root/cyj
    Route::get('/root/{name}',      function (string $name,) {return 'User Name: '.$name;})->name('test_root{name}')->where('name', '[A-Za-z]+');  // in constructor cheacked auth
    Route::get('/root/{id}',        function (string $id) {return 'User Code: '.$id;})->name('test_root{id}')->where('id', '[1-9]+');  // in constructor cheacked auth
    Route::get('/root/{name}{id}',  function (string $name,string $id) {return 'User Name: '.$name . '     User Code: '.$id;})->name('test_root{name}{id}')->where(['id', '[1-9]','name', '[A-Za-z]']);  // in constructor cheacked auth


});
Route::controller(OrderController::class)->group(function () {
    Route::get('/orders/{id}', 'show');
    Route::post('/orders', 'store');
});


Route::domain('{account}.example.com')->group(function () {
    Route::get('user/{id}', function (string $account, string $id) {
       return 'hello domain';
    });
});

Route::name('admin3.')->group(function () {
    Route::get('/users', function () {
        // Route assigned name "admin.users"... !!!!!!!!!!! admin.users  admin.users2  admin.users4
        //return 'admin3/users';
    })->name('users');

    Route::get('/users22', function () {
        // Route assigned name "admin.users"...
    })->name('users22');
});

Route::middleware(['throttle:uploads'])->group(function () {
    Route::post('/audio', function () {
        // ...
    });
 
    Route::post('/video', function () {
        // ...
    });
});
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
//                          main test
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/