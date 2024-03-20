<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class DummyServiceProvider extends ServiceProvider
{
    /**
     * Register services.
     */
    public function register(): void
    {
        //
       // echo 'Register'; //dont forget save app.php
    }

    /**
     * Bootstrap services.
     */
    public function boot(): void
    {
        //
       // echo 'Boot';
    }
}
