<?php

use App\Http\Controllers\AjaxController;
use App\Http\Controllers\Auth2\AuthenticatedSessionController;
use App\Http\Controllers\Auth\LoginController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\hottel\Auth as hottel_Auth;
use Doctrine\DBAL\Schema\View;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Crypt;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Redirect;
use App\Http\Middleware\Authenticate;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\OrderController;
use App\Http\Middleware\RoleMiddleware;
use Illuminate\Http\Request;
//-----------------------------------------------
Route::get('/token', function (Request $request) {  ///the erroe in session driver loccal host
    $token = $request->session()->token();
    echo $token;
    echo '----------------';
    $token = csrf_token();
    echo $token;
});
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
Route::group(['prefix' => '', 'middleware' => ['AlwaysRedirect']], function () {

    Route::get('about', function () {
        return view('other.about');
    })->name('other.about.Route');
    Route::get('/', function () {
        return view('main.index2');
    })->name('main.index2.Route');
    Route::get('Products', function () {
        return view('Products.index');
    })->name('Products.index.Route');

    /*------------------------------------------------------------*/
    //                          Blog
    //Route::post('/saveToken', [FcmController::class, 'saveToken'])->name('saveToken');
    /*------------------------------------------------------------*/
    Route::group(['prefix' => 'blog'], function () {


        Route::get('/', [
            'uses' => 'Blog\PostController@Blog',
            'as' => 'blog.post.index.Route'
        ]);

        Route::get('post/{id}', [
            'uses' => 'Blog\PostController@Post',
            'as' => 'blog.post.id.Route'
        ]);
        Route::get('post/{id}/like', [
            'uses' => 'Blog\PostController@LikePost',
            'as' => 'blog.post.like.Route'
        ]);

        // Route::group(['prefix' => 'admin','middleware' => ['auth' ,'guest']], function () {
        Route::group(['prefix' => 'user', 'middleware' => ['auth']], function () {
            Route::get('', [
                'uses'       => 'Blog\PostController@Index',
                'as'         => 'Blog.User.index.Route',
                //'middleware' => 'auth'
            ]);

            Route::get('new', [
                'uses' => 'Blog\PostController@New',
                'as' => 'Blog.User.new.Route',
                //'middleware' => 'auth'
            ]);

            Route::get('edit/{id}', [
                'uses' => 'Blog\PostController@Edit',
                'as' => 'Blog.User.edit.Route',
                //'middleware' => 'auth'
            ]);

            Route::get('delete/{id}', [
                'uses' => 'Blog\PostController@Delete',
                'as' => 'Blog.User.delete.Route',
                //'middleware' => 'auth'
            ]);

            Route::post('edit', [
                'uses' => 'Blog\PostController@Update',
                'as' => 'Blog.User.update.Route',
                //'middleware' => 'auth'
            ]);

            Route::post('create', [
                'uses' => 'Blog\PostController@Create',
                'as'    => 'Blog.User.create.Route',
                //'middleware' => 'auth'
            ]);
        });
    });
    /*------------------------------------------------------------*/
    //                          Servises
    /*------------------------------------------------------------*/
    //Route::patch('/shop', function () {return view('main.testhottel');})->name('testhottel');
    // Route::get('/hotel/shop', function () {return view('main.testhottel');})->name('hotel_home');
    //Route::middleware('auth')->
    Route::group(['prefix' => 'service'], function () {
        /*------------------------------------------------------------*/
        //                          hottel
        /*------------------------------------------------------------*/
        Route::group(['prefix' => 'hottel'], function () {

            Route::get('/', 'hottel\ContentsController@home')->name('hotel_home.Route');
            Route::get('upload', 'hottel\ContentsController@upload')->name('upload.Route');
            Route::post('upload', 'hottel\ContentsController@upload')->name('upload.Route');

            Route::get('clients', 'hottel\ClientController@index')->name('hotel_clients.Route');
            Route::get('clients/delete/{client_id}', 'hottel\ClientController@delete')->name('hotel_clients_delete.Route');
            // Route::get('/hotel/clients', 'hottel\ClientController@index')->name('hotel_clients')->middleware('auth');
            Route::get('clients/new', 'hottel\ClientController@newClient')->name('hotel_new_client.Route');
            Route::post('clients/new', 'hottel\ClientController@newClient')->name('hotel_create_client.Route');
            Route::get('clients/{client_id}', 'hottel\ClientController@show')->name('hotel_show_client.Route');
            Route::post('clients/{client_id}', 'hottel\ClientController@modify')->name('hotel_update_client.Route');
            //----------------
            Route::get('reservations/{client_id}', 'hottel\RoomsController@checkAvailableRooms')->name('hotel_check_room.Route');
            Route::post('reservations/{client_id}', 'hottel\RoomsController@checkAvailableRooms')->name('hotel_check_room.Route');

            Route::get('book/room/{client_id}/{room_id}/{date_in}/{date_out}', 'hottel\ReservationsController@bookRoom')->name('hotel_book_room.Route');

            Route::get('export', 'hottel\ClientController@export')->name('hotel_export.Route');

            Route::get('di', 'hottel\ClientController@di');
        });

        /*------------------------------------------------------------*/
        //                          Some utilis
        /*------------------------------------------------------------*/
        Route::group(['prefix' => 'Utilities'], function () {

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
            //hottel_Auth::routes();
            Route::get('/generate/password', function () {
                return bcrypt('123456789');
            })->name('d.Route');
        });
    });
    /*------------------------------------------------------------*/
    //In Laravel 5.5 you can now do:    Route::view('/page', 'dir.page'); ==== Route::get("/page", function () {return View::make("dir.page");});
    // Dashboard        http://127.0.0.1:8000/Dashboard not defined 
    /*------------------------------------------------------------*/
    Route::group(['prefix' => 'DashboardOneUI'], function () {
        //Route::get('/eee', 'hottel\ContentsController@home')->name('Dashboard_home.Route');
        //Route::view('/', 'DashboardOneUI.landing')->name('DashboardOneUI_home.Route');          !!no need
        Route::match(['get', 'post'], '/dashboard', function () {
            return view('DashboardOneUI.dashboard');
        })->name('DashboardOneUI_home.Route');
        Route::view('/pages/slick', 'pages.slick');
        Route::view('/pages/datatables', 'pages.datatables');
        Route::view('/pages/blank', 'pages.blank');
    });
    /*------------------------------------------------------------*/
    //                          Dev
    /*------------------------------------------------------------*/
    Route::group(['prefix' => 'dev'], function () {

        Route::get('testJS', function () {
            return view('main.testJS');
        })->name('testJS.Route');
        Route::get('VueJs', function () {
            return view('main.VueJs');
        })->name('VueJs.Route');
        Route::get('ReactJs', function () {
            return view('main.ReactJs');
        })->name('ReactJs.Route');

        Route::group(['prefix' => 'bootstrap'], function () {
            Route::get('/', function () {
                return view('main.bootstrap');
            })->name('bootstrap.Route');
            Route::get('/Dashboard', function () {
                return view('main.bootstrap.Dashboard');
            })->name('bootstrap.Dashboard.Route');
            Route::get('/Blog', function () {
                return view('main.bootstrap.Blog');
            })->name('bootstrap.Blog.Route');
            Route::get('/Pricing', function () {
                return view('main.bootstrap.Pricing');
            })->name('bootstrap.Pricing.Route');
        });
        Route::group(['prefix' => 'ajax'], function () {

            Route::get('/2', function () {
                return view('message');
            });
            Route::post('/2/getmsg', 'AjaxController@index');
            //---------------------------
            Route::get('/', [AjaxController::class, 'index'])->name('dev.ajax');
            Route::resource('ajaxes', AjaxController::class);
        });

        //--------------------------------------------------------------------------------------------------------------------------
        //                                   MiddleWares
        //--------------------------------------------------------------------------------------------------------------------------
        Route::middleware([RoleMiddleware::class])->group(function () {
            Route::get('/', function () {
                // ...
            });

            Route::get('/profile', function () {
                // ...
            })->withoutMiddleware([RoleMiddleware::class]);
        });
        Route::withoutMiddleware([RoleMiddleware::class])->group(function () {
            Route::get('/profile', function () {
                // ...
            });
        });
        //---------------------------
        Route::get('/', function () {
            // ...
        })->middleware('web');

        Route::middleware(['web', 'auth'])->group(function () {
            Route::get('/Dashboard', function () {
                return view('main.bootstrap.Dashboard');
            })->name('bootstrap.Dashboard');
            Route::get('/Blog', function () {
                return view('main.bootstrap.Blog');
            })->name('bootstrap.Blog.Route');
        });

        Route::put('/post/{id}', function (string $id) {
            // ...
        })->middleware('role:editor');


        Route::get('/middleware', ['middleware' => ['role', 'auth', 'web'], function () {
            return "hello midleware is here";
        }]);
        Route::get('/middleware2', function () {

            $user = Auth::user();

            if ($user->isAdmin()) {
                echo "this is user is a administrator";
            }
            return "hello midleware is here";
        });
        Route::get('/admin', 'AdminController@index');
        Route::get('/middleware', ['middleware' => ['IsAdmin'], function () {
            return "hello midleware is here";
        }]);
    });

    /*------------------------------------------------------------*/ //['middleware'=> ['role','auth','web'],
    //            Vite Vue3 app2     Vite react app1    
    /*------------------------------------------------------------*/
    Route::group(['prefix' => 'vite'], function () {

        Route::group(['prefix' => 'vue3'], function () {

            Route::group(['prefix' => 'app2'], function () {
                Route::get('/ViteVue3app2', 'HomeController@index');
                Route::any('/ViteVue3app2/spa/{any?}', 'SpaController@spa')->where(['any' => '.*']);
                Route::resource('project', 'ProjectController', ['except' => ['create']]);
                Route::get('ViteVue3app2/projects/', 'ProjectController@projects');
                Route::resource('note', 'NoteController', ['except' => ['create']]);
                Route::get('ViteVue3app2/notes/', 'NoteController@notes')->middleware(['auth', 'verified']);
                Route::post('ViteVue3app2/contact', 'SpaController@addContact')->middleware(Authenticate::class);
                Route::get('ViteVue3app2/contacts', 'SpaController@contacts')->middleware([Authenticate::class, DB::class]);
                Route::get('ViteVue3app2/skills', 'SpaController@skills');
                Route::get('ViteVue3app2/languages', 'SpaController@languages');
            });
            Route::group(['prefix' => 'app3'], function () {
                Route::post('login', [AuthenticatedSessionController::class, 'ViteVue3app3_login']);
                Route::post('register', [AuthenticatedSessionController::class, 'ViteVue3app3_register']);
                Route::post('logout', [AuthenticatedSessionController::class, 'ViteVue3app3_logout']);
                Route::get('/home', [App\Http\Controllers\HomeController::class, 'ViteVue3app3_index'])->name('ViteVue3app3_home.Route');
                Route::view('/ViteVue3App3views/{any?}', 'main-view')->name('dashboard.Route')->where('any', '.*');
                Route::get('/main-view')->name('dashboard.Route')->where('any', '.*');
            });
        });
        Route::group(['prefix' => 'react'], function () {
        });
    });
});
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
//                          main Auther
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

Route::group(['prefix' => 'Auther'], function () {

    /*------------------------------------------------------------*/
    //                   Authentification
    /*------------------------------------------------------------*/
    Auth::routes();
    //--------------------------Self Controler!! replaced laravel path----------------- matched name
    Route::group(['prefix' => ''], function () {
        // dd('main Auther    Authentification Self Controler'); 
        Route::get('register2', [
            'uses' => 'SignController@signUp',
            'as'   => 'auth.signup.Route' ///nameof route
        ]);
        Route::post('login', [
            'uses' => 'SignController@signIn',
            'as'   => 'auth.signin.Route'
        ]);
        Route::post('logout2', [
            'uses' => 'SignController@logout',
            'as'   => 'auth.logout.Route'
        ]);
    });
    /*------------------------------------------------------------*/
    //                          Api auth
    /*------------------------------------------------------------*/
    Route::prefix('auth2')->group(function () {

        Route::post('/Login2', LoginController::class);
    });
});
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
//                          main test
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
Route::group(['prefix' => 'testing'], function () {

    //Route::get('/address', ['controllerName','functionName'])->name('name');   
    //Route::get('/address', functionInline)->name('name');  
    Route::get('/root',  function () {
        return 'hello pouriya';
    })->name('root.Route');  // in constructor cheacked auth
    Route::get('/root/{id}',  function (string $id) {
        return 'User Code: ' . $id;
    })->name('root{id}.Route')->where('id', '[0-9]+');  // in constructor cheacked auth

    Route::group(['test'], function () {
        Route::get('test', function () {
            return view('main.bootstrap');
        })->name('bootstrap.Route');
        Route::get('test/Dashboard', function () {
            return view('main.bootstrap.Dashboard');
        })->name('bootstrap.Dashboard.Route');
        Route::get('test/Blog', function () {
            return view('main.bootstrap.Blog');
        })->name('bootstrap.Blog.Route');
        Route::get('test/Pricing', function () {
            return view('main.bootstrap.Pricing');
        })->name('bootstrap.Pricing.Route');
    });
    Route::group(['prefix' => 'test'], function () {         //prefix make addres injected look like  test/root

        Route::get('/root',             function () {
            return 'hello pouriya ' . Route::currentRouteName();
        })->name('test_root.Route');  // in constructor cheacked auth          http://127.0.0.1:8000/test/root/cyj
        Route::get('/root/{name}',      function (string $name,) {
            return 'User Name: ' . $name;
        })->name('test_root{name}.Route')->where('name', '[A-Za-z]+');  // in constructor cheacked auth
        Route::get('/root/{id}',        function (string $id) {
            return 'User Code: ' . $id;
        })->name('test_root{id}.Route')->where('id', '[1-9]+');  // in constructor cheacked auth
        Route::get('/root/{name}{id}',  function (string $name, string $id) {
            return 'User Name: ' . $name . '     User Code: ' . $id;
        })->name('test_root{name}{id}.Route')->where(['id', '[1-9]', 'name', '[A-Za-z]']);  // in constructor cheacked auth

    });
    Route::prefix('admin2')->group(function () {

        //Route::post('/login',LoginController::class);  ///just constructor work!!  not working with out function define
        Route::get('/login', [LoginController::class, 'index'])->name('admin2_login');
    });
    Route::get('/home', [HomeController::class, 'index'])->name('home');  // in constructor cheacked auth
    //------> forece to auth
    Route::middleware(['OrderController', 'auth'])->group(function () {
        Route::get('/root',             function () {
            return 'hello pouriya ' . Route::currentRouteName();
        })->name('test_root.Route');  // in constructor cheacked auth          http://127.0.0.1:8000/test/root/cyj
        Route::get('/root/{name}',      function (string $name,) {
            return 'User Name: ' . $name;
        })->name('test_root{name}.Route')->where('name', '[A-Za-z]+');  // in constructor cheacked auth
        Route::get('/root/{id}',        function (string $id) {
            return 'User Code: ' . $id;
        })->name('test_root{id}.Route')->where('id', '[1-9]+');  // in constructor cheacked auth
        Route::get('/root/{name}{id}',  function (string $name, string $id) {
            return 'User Name: ' . $name . '     User Code: ' . $id;
        })->name('test_root{name}{id}.Route')->where(['id', '[1-9]', 'name', '[A-Za-z]']);  // in constructor cheacked auth


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
        })->name('users.Route');

        Route::get('/users22', function () {
            // Route assigned name "admin.users"...
        })->name('users22.Route');
    });

    Route::middleware(['throttle:uploads'])->group(function () {
        Route::post('/audio', function () {
            // ...
        });

        Route::post('/video', function () {
            // ...
        });
    });
});
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/
//                          main test
/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------*/