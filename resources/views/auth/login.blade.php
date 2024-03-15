@extends('layouts.master')

@section('content')

<div class="container LoginAtt" style="padding: 20px;">
    @if(Session::has('fail'))
    <div class="alert alert-danger">
        {{ Session::get('fail') }}
    </div>
    @endif
    <div class="d-flex justify-content-center h-100">
        <div class="card">
            <div class="card-header">
                <h3>{{ __('Sign In') }}</h3>
                <div class="d-flex justify-content-end social_icon">
                    <span><i class="fab fa-facebook-square"></i></span>
                    <span><i class="fab fa-google-plus-square"></i></span>
                    <span><i class="fab fa-twitter-square"></i></span>
                </div>
            </div>
            <div class="card-body">
                <form method="POST" action="{{ route('login') }}">
                    @csrf
                    <div class="input-group form-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text"><i class="fas fa-user"></i></span>
                        </div>
                        <!-- <label for="email">{{ __('Email Address') }}</label> -->

                        <input id="email" type="email" class="form-control @error('email') is-invalid @enderror" name="email" value="{{ old('email') }}" required autocomplete="email" autofocus placeholder="username ">
                        @error('email')
                        <span class="invalid-feedback" role="alert">
                            <strong>{{ $message }}</strong>
                        </span>
                        @enderror


                    </div>
                    <div class="input-group form-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text"><i class="fas fa-key"></i></span>
                        </div>
                        <!-- <label for="password" class="col-md-4 col-form-label text-md-end">{{ __('Password') }}</label> -->
                        <input id="password" type="password" class="form-control @error('password') is-invalid @enderror" name="password" required autocomplete="current-password" placeholder="password">

                        @error('password')
                        <span class="invalid-feedback" role="alert">
                            <strong>{{ $message }}</strong>
                        </span>
                        @enderror
                    </div>
                    <div class="row align-items-center remember" style="padding: 20px;">
                        <input type="checkbox">Remember Me
                        <input class="form-check-input" type="checkbox" name="remember" id="remember" {{ old('remember') ? 'checked' : '' }}>
                        <!-- <label class="form-check-label" for="remember"> {{ __('Remember Me') }}</label> -->

                    </div>
                    <div class="form-group ">
                        <input type="submit" value="Login" class="btn float-right login_btn">

                    </div>
                </form>
            </div>
            <div class="card-footer">
                <div class="d-flex justify-content-center links" style="padding: 20px;">
                   <a href="{{route('register')}}">{{ __('Sign Up') }}</a>      ?Don't have an account  
                </div>
                <div class="d-flex justify-content-center">
                    @if (Route::has('password.request'))
                    <a class="btn btn-link" href="{{ route('password.request') }}">
                        {{ __('Forgot Your Password?') }}
                    </a>
                    @endif
                </div>
            </div>
        </div>
    </div>
</div>
@endsection