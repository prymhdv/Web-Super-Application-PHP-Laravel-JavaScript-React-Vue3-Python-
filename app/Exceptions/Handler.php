<?php

namespace App\Exceptions;

use Exception;
use Illuminate\Auth\AuthenticationException;
use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;
<<<<<<< HEAD
use App\Exceptions\MethodNotAllowedHttpException;
 

=======
 
>>>>>>> 06324b5bcdda1012c4969ab7f28d91444a0d5d74

class Handler extends ExceptionHandler
{
    /**
     * The list of the inputs that are never flashed to the session on validation exceptions.
     *
     * @var array<int, string>
     */
    protected $dontFlash = [
        'current_password',
        'password',
        'password_confirmation',
    ];
     /**
     * A list of the exception types that should not be reported.
     *
     * @var array
     */
     /**
     * Report or log an exception.
     *
     * This is a great spot to send exceptions to Sentry, Bugsnag, etc.
     *
     * @param  \Exception  $e
     * @return void
     */
    //Exception $e
<<<<<<< HEAD
    public function report($exception)
    {
        parent::report($exception);
=======
    public function report($e)
    {
        parent::report($e);
>>>>>>> 06324b5bcdda1012c4969ab7f28d91444a0d5d74
    }
    protected $dontReport = [
        \Illuminate\Auth\AuthenticationException::class,
        \Illuminate\Auth\Access\AuthorizationException::class,
        \Symfony\Component\HttpKernel\Exception\HttpException::class,
        \Illuminate\Database\Eloquent\ModelNotFoundException::class,
        \Illuminate\Validation\ValidationException::class,
    ];
    /**
     * Render an exception into an HTTP response.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Exception  $e
     * @return \Illuminate\Http\Response
     */
    //Exception $e
    public function render($request,$e)
    {
        return parent::render($request, $e);
    }
    /**
     * Register the exception handling callbacks for the application.
     */
    //Throwable
    public function register(): void
    {
<<<<<<< HEAD
        $this->reportable(function (MethodNotAllowedHttpException $e) {
=======
        $this->reportable(function ($e) {
>>>>>>> 06324b5bcdda1012c4969ab7f28d91444a0d5d74
            //
        });
    }
    /**
     * Convert an authentication exception into an unauthenticated response.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Illuminate\Auth\AuthenticationException  $e
     * @return \Illuminate\Http\Response
     */
    protected function unauthenticated($request, AuthenticationException $e)
    {
        if ($request->expectsJson()) {
            return response()->json(['error' => 'Unauthenticated.'], 401);
        } else {
            return redirect()->guest('login');
        }
    }
}
