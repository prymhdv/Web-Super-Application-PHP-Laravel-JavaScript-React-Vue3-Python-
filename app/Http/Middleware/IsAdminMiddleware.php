<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Symfony\Component\HttpFoundation\Response;

class IsAdminMiddleWare
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        if(!Auth::check()) return $next($request);
        $user = Auth::user();
        if(!$user->isAdmin()){
          //  echo "this is user Administrator";
            return redirect('/');
        }

        return redirect()->intended('/admin');
        return $next($request);
    }
}
