<?php

use App\Http\Controllers\Auth\LoginController;
use App\Http\Controllers\Hottel\Auth as Hottel_Auth;
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
Route::get('/', function ()         {   return view('main.index2');})->name('main.index2');
Route::get('Products', function ()  {   return view('Products.index');})->name('Products.index');
/*------------------------------------------------------------*/
Route::get('testJS', function ()    {   return view('main.testJS');})->name('testJS');
Route::get('VueJs', function ()     {   return view('main.VueJs');})->name('VueJs');
Route::get('ReactJs', function ()   {   return view('main.ReactJs');})->name('ReactJs');
/*------------------------------------------------------------*/
Route::get('about', function ()     {   return view('other.about');})->name('other.about');
/*------------------------------------------------------------*/
//                          Blog
/*------------------------------------------------------------*/
Route::get('/blog', [
    'uses' => 'PostController@getIndex',
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
Route::group(['prefix' => 'admin', 'middleware' => ['auth']], function () {
    Route::get('', [
        'uses' => 'PostController@getAdminIndex',
        'as' => 'admin.index',
        // 'middleware' => 'auth'
    ]);

    Route::get('create', [
        'uses' => 'PostController@getAdminCreate',
        'as' => 'admin.create'
    ]);

    Route::post('create', [
        'uses' => 'PostController@postAdminCreate',
        'as' => 'admin.create'
    ]);

    Route::get('edit/{id}', [
        'uses' => 'PostController@getAdminEdit',
        'as' => 'admin.edit'
    ]);

    Route::get('delete/{id}', [
        'uses' => 'PostController@getAdminDelete',
        'as' => 'admin.delete'
    ]);

    Route::post('edit', [
        'uses' => 'PostController@postAdminUpdate',
        'as' => 'admin.update'
    ]);
});
/*------------------------------------------------------------*/
//                   Authentification
/*------------------------------------------------------------*/
Auth::routes();
Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');
Route::post('login', [
    'uses' => 'SigninController@signin',
    'as' => 'auth.signin'
]);
/*------------------------------------------------------------*/
//                          Hottel
/*------------------------------------------------------------*/


Route::get('/facades/db', function () {
    return DB::select('SELECT * FROM table');
});

Route::get('/facades/encrypt', function () {
    return Crypt::encrypt('123456789');
    //eyJpdiI6ImtESks3a3pLNEhLRnhRaFN6eTlsbHc9PSIsInZhbHVlIjoiS3hsd0RWT2YzaGZSV1R1aE1vSitYc0dlcmlna2NTZ096K04rNTlsRVhTUT0iLCJtYWMiOiJhYmQ0NzAzYjQ4ZWZhODg0ZDE0MWI0YTMxMTcxZjZjYjE3N2NiYzFlNDdlZTA3ZDVhOTc3NWVjNjEzNDExOGJkIiwidGFnIjoiIn0=
});
Route::get('/facades/decrypt', function () {
    return Crypt::decrypt('eyJpdiI6ImtESks3a3pLNEhLRnhRaFN6eTlsbHc9PSIsInZhbHVlIjoiS3hsd0RWT2YzaGZSV1R1aE1vSitYc0dlcmlna2NTZ096K04rNTlsRVhTUT0iLCJtYWMiOiJhYmQ0NzAzYjQ4ZWZhODg0ZDE0MWI0YTMxMTcxZjZjYjE3N2NiYzFlNDdlZTA3ZDVhOTc3NWVjNjEzNDExOGJkIiwidGFnIjoiIn0');
    //=
});
/*------------------------------------------------------------*/
//Route::patch('/shop', function () {return view('main.testHottel');})->name('testHottel');
// Route::get('/hotel/shop', function () {return view('main.testHottel');})->name('hotel_home');
Route::middleware('auth')->group(function(){  //controlpannel need login

    Route::get('/hotel/shop', 'Hottel\ContentsController@home')->name('hotel_home');
    Route::get('/hotel/clients', 'Hottel\ClientController@index')->name('hotel_clients');
    // Route::get('/hotel/clients', 'Hottel\ClientController@index')->name('hotel_clients')->middleware('auth');
    Route::get('/hotel/clients/new', 'Hottel\ClientController@newClient')->name('hotel_new_client');
    Route::post('/hotel/clients/new', 'Hottel\ClientController@newClient')->name('hotel_create_client');
    Route::get('/hotel/clients/{client_id}', 'Hottel\ClientController@show')->name('hotel_show_client');
    Route::post('/hotel/clients/{client_id}', 'Hottel\ClientController@modify')->name('hotel_update_client');
    //----------------
    Route::get('/hotel/reservations/{client_id}', 'Hottel\RoomsController@checkAvailableRooms')->name('hotel_check_room');
    Route::post('/hotel/reservations/{client_id}', 'Hottel\RoomsController@checkAvailableRooms')->name('hotel_check_room');
    
    Route::get('/hotel/book/room/{client_id}/{room_id}/{date_in}/{date_out}', 'Hottel\ReservationsController@bookRoom')
    ->name('hotel_book_room');

    Route::get('export','Hottel\ClientController@export');
    Route::get('upload','Hottel\ContentsController@upload')->name('upload');
    Route::post('upload','Hottel\ContentsController@upload')->name('upload');
    
});
Route::get('/di', 'Hottel\ClientController@di');
// Route::get('/hotel/shop', 'Hottel\ContentsController@home')->name('hotel_home');
// Route::get('/hotel/clients', 'Hottel\ClientController@index')->name('hotel_clients');
// // Route::get('/hotel/clients', 'Hottel\ClientController@index')->name('hotel_clients')->middleware('auth');
// Route::get('/hotel/clients/new', 'Hottel\ClientController@newClient')->name('hotel_new_client');
// Route::post('/hotel/clients/new', 'Hottel\ClientController@newClient')->name('hotel_create_client');
// Route::get('/hotel/clients/{client_id}', 'Hottel\ClientController@show')->name('hotel_show_client');
// Route::post('/hotel/clients/{client_id}', 'Hottel\ClientController@modify')->name('hotel_update_client');
// //----------------
// Route::get('/hotel/reservations/{client_id}', 'Hottel\RoomsController@checkAvailableRooms')->name('hotel_check_room');
// Route::post('/hotel/reservations/{client_id}', 'Hottel\RoomsController@checkAvailableRooms')->name('hotel_check_room');

// Route::get('/hotel/book/room/{client_id}/{room_id}/{date_in}/{date_out}', 'Hottel\ReservationsController@bookRoom')
// ->name('hotel_book_room');
//Hottel_Auth::routes();
Route::get('/generate/password', function() { return bcrypt('123456789'); } )->name('d');
/*------------------------------------------------------------*/
//                          Api auth
/*------------------------------------------------------------*/
Route::prefix('auth')->group(function(){

    Route::post('/Login',LoginController::class);

});