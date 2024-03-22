<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Symfony\Component\HttpFoundation\Response;

class AlwaysRedirect
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {   ///return "hello"; App\Http\Middleware\AlwaysRedirect::handle(): Return value must be of type Symfony\Component\HttpFoundation\Response, string returned
        // if($request->path() == "about")  //checking
        // {
        //     return redirect('/'); allways manage requestto what happane before go goal path
        // }
        if(!Auth::check() && $request->path() == "dev0")
        { 
            return redirect('/');
            $request->authenticate();
            $request->session()->regenerate();
        }
        // dd(route('blog.index'));
        //dd(($next($request)));
        return $next($request);  //--->> !!!'Blog\PostController@Post',  subfolders stricted
        //---------------------------------------------'web.php'>>>'Blog\PostController@Blog'>>'middleware AlwaysRedirect@handle'>>>'target address'
        if(0){ 
            //BeforeMiddleware----------------------------------------------------
            // Perform action
            return $next($request);
            //AfterMiddleware-----------------------------------------------------
            $response = $next($request);
            // Perform action
            return $response;
        }
    }
}
