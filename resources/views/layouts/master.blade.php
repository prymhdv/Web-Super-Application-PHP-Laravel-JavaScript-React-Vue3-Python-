<!DOCTYPE html>
<html class="no-js" lang="fa-IR" dir="rtl">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Title -->
    <title>Laravel</title>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <!-- Styles -->
    <link rel="stylesheet" href="{{ asset('css/bootstrap.css') }}">

    <link rel="stylesheet" href="{{ asset('css/style.css') }}">
    <link rel="stylesheet" href="{{ asset('css/navLink.css') }}">
    <link rel="stylesheet" href="{{ asset('css/Single.css') }}">

    <link rel="stylesheet" href="{{ URL::to('css/style.css') }}">
    <link rel="stylesheet" href="{{ URL::to('css/navLink.css') }}">

    <link rel="stylesheet" href="css/style.css">        <!-- own folder -->
    <link rel="stylesheet" href="css/Single.css">       <!-- own folder -->
    <link rel="stylesheet" href="css/photoSlider.css" > <!-- own folder -->

{{--    <link rel="stylesheet" href="css/animated.css" >--}}
{{--    <script type="module"  href="js/animated.js" defer></script>--}}

    <!-- Scripts -->
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
    <script type="module"  src="{{ asset('js/app.js') }}" defer></script>
    <link rel="stylesheet" href="{{ asset('css/H2.css') }}">

    <link href="css/1b-gallery.css" rel="stylesheet">
    <link href="css/2b-caption-gallery.css" rel="stylesheet">
    <script type="module"  src="js/1c-gallery.js"></script>
    <!-- (A) CSS & JS -->

    <script type="module"  src="jq/jquery-3.7.1.min.js"></script>
    <!-- script -->
    <script type="module"  src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
    <script type="module"  src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>
    <!-- Bootstrap -->
    <link href="css/bootstrap.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ asset('css/bootstrap.css') }}">
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
{{--    <h1>Pure Css Animated Background</h1>--}}
{{--</div>--}}
{{--<div class="area" >--}}
{{--    <ul class="circles">--}}
{{--        <li></li>--}}
{{--        <li></li>--}}
{{--        <li></li>--}}
{{--        <li></li>--}}
{{--        <li></li>--}}
{{--        <li></li>--}}
{{--        <li></li>--}}
{{--        <li></li>--}}
{{--        <li></li>--}}
{{--        <li></li>--}}
{{--    </ul>--}}
{{--</div >--}}

</body>
</html>
