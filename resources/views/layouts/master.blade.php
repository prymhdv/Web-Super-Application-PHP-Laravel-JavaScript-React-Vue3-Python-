<!DOCTYPE html>
<html class="no-js" lang="fa-IR" dir="rtl">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <!-- <title>{{ config('app.name', 'Laravel') }}</title> -->

    <!-- Fonts -->
    <link rel="dns-prefetch" href="//fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=Nunito" rel="stylesheet">

    <!-- Scripts -->
    @vite(['resources/sass/app.scss', 'resources/js/app.js'])
    <script src="http://localhost:8097"></script>

    <!-- Title -->
    <title>Shoping Center</title>

    <!-- Latest compiled and minified CSS -->
    <!-- Bootstrap -->
    <link rel="stylesheet" href="{{ asset('css/bootstrap.css') }}">
    <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"> -->

    <!-- Styles CSS-->
    <link rel="stylesheet" href="{{ asset('css/style.css') }}">
    <link rel="stylesheet" href="{{ URL::to('css/style.css') }}">
    <link rel="stylesheet" href="{{ asset('css/Single.css') }}">
    <link rel="stylesheet" href="{{ asset('css/JStest.css') }}">


    {{-- <link rel="stylesheet" href="css/animated.css" >--}}
    {{-- <script type="module"  href="js/animated.js" defer></script>--}}

    <!-- Scripts -->
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
    <script type="module" src="{{ asset('js/app.js') }}" defer></script>


    <link href="{{asset('css/1b-gallery.css')}}" rel="stylesheet">
    <link href="{{asset('css/2b-caption-gallery.css')}}" rel="stylesheet">

    <!-- (A) CSS & JS -->
    <script src="{{ asset('js/Own.js') }}"></script>

    <script type="module" src="{{asset('jq/jquery-3.7.1.min.js')}}"></script>
    <!-- script -->
    <script type="module" src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
    <script type="module" src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>

    <!-- Font -->
    <link href='http://fonts.googleapis.com/css?family=Arizonia' rel='stylesheet' type='text/css'>
    <link href="css/font-awesome.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ asset('css/font-awesome.css') }}">

    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script type="module"  src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
    <script type="module"  src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>
    <![endif]-->




</head>

<body>
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