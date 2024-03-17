<?php

namespace App\Providers;
use Illuminate\Support\Facades\Artisan;
use Illuminate\Support\Facades\ParallelTesting;
use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\Schema;
//use Illuminate\Database\Events\MigrationsStarted;
//use Illuminate\Support\Facades\Event;
use App\Http\Middleware\TerminatingMiddleware;

class AppServiceProvider extends ServiceProvider
{
    //  /**
    //  * The event listener mappings for the application.
    //  *
    //  * @var array
    //  */
    // protected $listen = [
    //         MigrationsStarted::class => [
    //         DeleteUnitsImagesFromAws::class,
    //     ]
    // ];
    /**
     * Bootstrap any application services.
     */
     public function boot()
     {

//            $mainPath       = database_path('migrations');
//            $directories    = glob($mainPath . '/*' , GLOB_ONLYDIR);
//            $paths          = array_merge([$mainPath], $directories);
//
//            $this->loadMigrationsFrom($paths);  $mainPath = database_path('migrations');
//            $directories = glob($mainPath . '/*' , GLOB_ONLYDIR);
//            $paths = array_merge([$mainPath], $directories);
//
//            $this->loadMigrationsFrom($paths);
//
//
//            Event::listen(MigrationsStarted::class, function($event) {
//
//            Schema::defaultStringLength(191);
//        });

        Schema::defaultStringLength(191);

        /*---------------------------MIGRATION----------------------------*/
        $migrationsPath = database_path('migrations');
        $directories    = glob($migrationsPath.'/*', GLOB_ONLYDIR);
        $paths          = array_merge([$migrationsPath], $directories);

        $this->loadMigrationsFrom($paths);
        /*---------------------------MIGRATION----------------------------*/



        ParallelTesting::setUpTestDatabase(function (string $database, int $token) {
            Artisan::call('db:seed');
        });
     }



    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
        $this->app->singleton(TerminatingMiddleware::class);
    }




}
