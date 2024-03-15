<!DOCTYPE html>
<html class="no-js" lang="fa-IR" dir="rtl">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">
<!-- //////////////////////////////////////////////////////////////////////////////////////////////////////////////// -->
    <!-- <script src="https://cdn.jsdelivr.net/npm/vue"></script> -->
    <!-- @viteReactRefresh -->
    @vite(['resources/css/app.css'])
    @vite(['resources/js/app.js'])              
    <!-- @vite(['resources/js/appViteVue3_app1.js'])  -->
<!-- //////////////////////////////////////////////////////////////////////////////////////////////////////////////// -->
    <!-- Title -->
    <title>Shoping Center</title>
    <!-- <title>{{ config('app.name', 'Laravel') }}</title> -->


 <!-- Fonts -->
    <link rel="dns-prefetch" href="//fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=Nunito" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Arizonia' rel='stylesheet' type='text/css'>
    

    <!-- <script src="{{ asset('jq/jquery-3.7.1.js') }}"></script> -->
    <script src="{{ asset('jq/jquery-3.7.1.min.js') }}"></script>
   <link rel="stylesheet" href="{{ asset('css/main.css') }}"> 
   <!-- <script type="text/javascript" src="{{ asset('js/Main.js') }}"></script> -->
   <!-- <link rel="stylesheet" href="{{ asset('fonts/mainfont.css') }}">  -->
   <script src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
   <script src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>
   <script src="{{asset('jq/jquery-3.7.1.min.js')}}"></script>
   <!-- <script type="module" src="{{asset('js/animated.js')}}"></script> -->
   <script src="{{asset('js/Pure.js')}}"></script>

  
   <script src="{{asset('js/fontawesome-free-6.5.1-web/fontawesome.js')}}"></script>
 
</head>

<body class="antialiased">
  
    @include('partials.header')
   
    <div class="container">
    @yield('content')
    </div>

    @include('partials.footer')
  
    {{--<div class="context">--}}
    {{-- <h1>Pure Css Animated Background</h1>--}}
    {{--</div>--}}
    {{--<div class="area" >--}}
    {{-- <ul class="circles">--}}
    {{-- <li></li>--}}
    {{-- <li></li>--}}
    {{-- <li></li>--}}
    {{-- <li></li>--}}
    {{-- <li></li>--}}
    {{-- <li></li>--}}
    {{-- <li></li>--}}
    {{-- <li></li>--}}
    {{-- <li></li>--}}
    {{-- <li></li>--}}
    {{-- </ul>--}}
    {{--</div >--}}

</body>

</html>