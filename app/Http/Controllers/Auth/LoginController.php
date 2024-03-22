<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use App\Http\Requests\LoginRequest;
use App\Models\User;
use Illuminate\Foundation\Auth\AuthenticatesUsers;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\ValidationException;
use Response;

class LoginController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Login Controller
    |--------------------------------------------------------------------------
    |
    | This controller handles authenticating users for the application and
    | redirecting them to your home screen. The controller uses a trait
    | to conveniently provide its functionality to your applications.
    |
    */

    use AuthenticatesUsers;

    /**
     * Where to redirect users after login / registration.
     *
     * @var string
     */
    //protected $redirectTo = '/admin';
    //protected $redirectTo = '/hotel/clients';
    //protected $redirectTo = route('blog.index');Constant expression contains invalid operations
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    { 
        // return 'hello this is test2 login message';   not working with out function define
        $this->middleware('guest', ['except' => 'logout']);//default
       //dd('LoginController":__construct');
    }
    /// handel incoming request 
    public function __invoke(LoginRequest $request)//:Response       ///0--0 not working its gurded in constructor middleware!!!!!!!!!!!!!
    {
        $user = User::where('email',$request->email)->first();
        //dd('LoginController":__invoke');
        if(!$user || !Hash::check($request->password, $user->password))
        {
            throw ValidationException::withMessages([
                'email'=> ['The credentials you entered are inncorrect.']
            ]);

        }
        //dd('LoginController":__invoke');
    } 
    public function index(){
        return 'hello this is test2 login message';
    }
}
