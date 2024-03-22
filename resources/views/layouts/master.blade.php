<!DOCTYPE html>
<html class="no-js" lang="fa-IR" dir="ltr">

{{--  --}}
{{--  --}}

<head>

    {{-- <meta http-equiv="X-UA-Compatible" content="IE=edge"> --}}
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <!-- Title -->
    <title>SuperWebApp Center</title>
    <!-- <title>{{ config('app.name', 'Laravel') }}</title> -->


    <!-- Fonts -->
    <link rel="dns-prefetch" href="//fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=Nunito" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Arizonia' rel='stylesheet' type='text/css'>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    {{-- <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous">
    </script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous">
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous">
    </script> --}}
    {{-- "scripts":["node_modules/bootstrap/dist/js/bootstrap.min.js",
     "node_modules/bootstrap/dist/js/bootstrap.bundle.js"] --}}
    {{-- ------------------------------------------------------------------------------------------------------------ --}}
  

    <link rel="stylesheet" href="{{ asset('css/main.css') }}">
   
   
    <script src="{{ asset('js/fontawesome-free-6.5.1-web/fontawesome.js') }}"></script>

    <script src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>

    <script type="text/javascript" src="{{ asset('js/Main.js') }}"></script> 
    <link rel="stylesheet" href="{{ asset('fonts/mainfont.css') }}"> 
    
    <script src="{{ asset('js/Pure.js') }}"></script>
   
      <script src="{{ asset('jq/jquery-3.7.1.js') }}"></script>
    <script src="{{ asset('jq/jquery-3.7.1.min.js') }}"></script>
    
    {{-- <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script> --}}
    <script src="{{ asset('js\popperjs-core-2.11.8\popper-base.js') }}"></script>
    <script src="{{ asset('js\bootstrap-5.3.3-dist\js\bootstrap.js') }}"></script>
     {{-- <script src="{{ asset('js\bootstrap-5.3.3-dist\js\bootstrap.bundle.js') }}"></script> --}}
    <link rel="stylesheet" href="{{ asset('css\bootstrap-5.3.3-dist\css\bootstrap.css') }}">
    {{-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>   --}}

 

 
    {{-- <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.6/umd/popper.min.js"></script> --}}
 
    {{-- ------------------------------------------------------------------------------------------------------------ --}}
   {{-- ------------------------------------------------------------------------------------------------------------ --}}
    {{-- THE Error Boot Strap not worked before decline! --}}
    <!-- <script src="https://cdn.jsdelivr.net/npm/vue"></script> -->
    @viteReactRefresh
    {{-- @vite(['resources/css/app.css']) --}}
    @vite(['resources/js/app.js'])
    {{-- @vite(['resources/js/appViteVue3_app1.js']) --}}
   {{-- ------------------------------------------------------------------------------------------------------------ --}}
  

</head>
{{--  --}}
{{--  --}}
{{-- <body class="antialiased" > --}}
{{-- <body style="direction: rtl;"> --}}
<body class= "d-flex flex-column min-vh-100" >
    {{-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>   --}}

    {{-- <p lang="fa">سایت آموزشی فری لرن</p>
    <p lang="en">This Text Is English</p> --}}
    @include('partials.header')

    <div id="yields"  class="container">
        @yield('content')
    </div>

    @include('partials.footer')

    {{-- <div class="context"> --}}
    {{-- <h1>Pure Css Animated Background</h1> --}}
    {{-- </div> --}}
    {{-- <div class="area" > --}}
    {{-- <ul class="circles"> --}}
    {{-- <li></li> --}}
    {{-- <li></li> --}}
    {{-- <li></li> --}}
    {{-- <li></li> --}}
    {{-- <li></li> --}}
    {{-- <li></li> --}}
    {{-- <li></li> --}}
    {{-- <li></li> --}}
    {{-- <li></li> --}}
    {{-- <li></li> --}}
    {{-- </ul> --}}
    {{-- </div > --}}
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    {{-- <script src="js/bootstrap-4.1.3-js/bootstrap.js"></script> --}}
    {{-- <script src="{{asset('js\bootstrap-5.3.3-dist\js\bootstrap.js')}}"></script>
    <script src="{{ asset('js\bootstrap-5.3.3-dist\js\bootstrap.bundle.js') }}"></script> --}}
</body>

</html>
