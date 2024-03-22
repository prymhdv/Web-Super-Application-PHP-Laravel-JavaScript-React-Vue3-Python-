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
        //echo "this is user Administrator";
        if (!Auth::check()) return $next($request);
        /** @var App\Models\User $user */
        $user = Auth::user();
        if (!$user->isAdmin()) {
            echo "this isnt user Administrator";
            return redirect('/');
        }

        //return redirect()->intended('/admin');
        //return 'Heloo you are role administrator';
        return $next($request);
    }
}
