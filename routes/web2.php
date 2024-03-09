<?php


use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PostController;
/*------------------------------------------------------------*/
Route::get('/', function () {
    return view('main.index2');
})->name('main.index2');
/*------------------------------------------------------------*/
Route::get('Products', function () {
    return view('Products.index');
})->name('Products.index');
/*------------------------------------------------------------*/
// Route::get('blog', 'PostController@getIndex')->name('blog.index');
Route::get('/blog', [
    'uses' => 'PostController@getIndex',
    'as' => 'blog.index'
]);
/*------------------------------------------------------------ */
Route::get('post/{id}', [
    'uses' => 'PostController@getPost',
    'as' => 'blog.post'
]);

/*------------------------------------------------------------*/
Route::get('about', function () {
    return view('other.about');
})->name('other.about');


Route::group(['prefix' => 'admin'], function() {
    Route::get('', [
        'uses' => 'PostController@getAdminIndex',
        'as' => 'admin.index'
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

    Route::post('edit', [
        'uses' => 'PostController@postAdminUpdate',
        'as' => 'admin.update'
    ]);

    
});

Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');
 

/*------------------------------------------------------------*/
/*
// Route::get('post/{id}', function () {
//     return view('blog.post');
// })->name('blog.post');

// Route::get('about-page', function () {
//     return view('other.about');
// })->name('other.about');

// Route::post('edit', function(\Illuminate\Http\Request  $request) {

    //     return redirect()->route('admin.index')
    //     ->with('info',Post edited,'new Title' . request->input('title'));
    // })->name('admin.update');




 return view('blog.post',['post'=>$post]);
    // return view('blog.post');
    // return $post['title'];




//Route::get('Online-Shopping', function () {
//    return view('Online-Shopping.index');
//})->name('Online-Shopping.index');



// [
//     'uses' => 'PostController@getIndex',
//     'as' => 'blog.index'
// ]

Route::get('about', function (\Illuminate\Http\Request $request
\Illuminate\Validation\Factory $validation)
 {  $validation = validator->make($request->all(), [
    'title'=>'required|min:5',
    'content'=>'required|min:10'
    ]);
    if($validation->fails())
    {
        return redirect()->back()->withErrors($validation)->withInput();
    }  
    return view('other.about');
})->name('other.about');

Route::get('blog', function () {
    return view('blog.index');
})->name('blog.index');

Route::get('blog', 'PostController@getIndex')->name('blog.index');

Route::get('post/{id}', function($id){
    if($id==1){
        $post=[
            'title' => 'learning laravel',
            'content' => 'this is the demo this is the demo this is the demo'
        ];
    }
    else{

        $post=[
            'title' => 'somthing else laravel',
            'content' => 'some other this is the demo'
        ];
    }
   
    return view('blog.post',['post'=>$post]);
  
})->name('blog.post');
*/
/*------------------------------------------------------------*/