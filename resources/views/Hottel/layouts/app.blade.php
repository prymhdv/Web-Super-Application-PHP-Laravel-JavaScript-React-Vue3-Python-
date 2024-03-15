<!DOCTYPE html>
<html data-whatinput="keyboard" data-whatintent="keyboard" class=" whatinput-types-initial whatinput-types-keyboard">
  <head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta name="csrf-token" content="{{ csrf_token() }}">
        <meta charset="UTF-8">
        <title>Landon Hotel App</title>
            <link rel="icon" type="image/x-icon" href="favicon.ico" />
            <link rel="stylesheet" href="{{ asset('Hottel/css/foundation.css') }}">
            <link rel="stylesheet" href="{{ asset('Hottel/css/app.css') }}">
            <link rel="stylesheet" href="{{ asset('Hottel/pickadate/lib/themes/default.css') }}">
            <link rel="stylesheet" href="{{ asset('Hottel/pickadate/lib/themes/default.date.css') }}">
    <meta class="foundation-mq">
    <link rel="stylesheet" href="{{ asset('css/bootstrap-4.1.3-css/bootstrap.css')}}">
    
  </head>
    <body>

        <!-- Start Top Bar -->
    <div class="top-bar">
      <div class="row">
        <div class="top-bar-left">
          <ul class="dropdown menu" data-dropdown-menu="tckp8q-dropdown-menu" role="menubar">
            <li role="menuitem"><a href="{{ route('main.index2') }}">main</a></li>
            <li role="menuitem"><a href="{{ route('hotel_home') }}">Home</a></li>
            <li role="menuitem"><a href="{{ route('hotel_clients') }}">Clients</a></li>.
            
          </ul>
        </div>
        <div class="top-bar-right">
        <ul class="dropdown menu" data-dropdown-menu="tckp8q-dropdown-menu" role="menubar">
           <li role="menuitem">
              <a href="{{ route('logout') }}"
              onclick="event.preventDefault(); document.getElementById('logout-form').submit();">{{ __('خروج') }}</a>
              <form id="logout-form" action="{{ route('logout') }}" method="POST" class="d-none"> {{ @csrf_field()  }}  </form> 
          </li>
           
        </ul>
      </div>
      </div>
    </div>
    <!-- End Top Bar -->

    <br>
    
    
    
@yield('content')
    

    <div class="row column text-bg-dark">
      <hr>
      <ul class="menu">
        <li class="float-right">Copyright 2017</li>
      </ul>
    </div>

    <script>
      $(document).foundation();
    </script>
      <script src="jquery-1.11.1.min.js"></script>
      <script>
      $(document).ready(function() {
          // your code
      });
      </script>
        <script src="{{ asset('Hottel/js/vendor/jquery.js') }}"></script>
        <script src="{{ asset('Hottel/js/vendor/what-input.js') }}"></script>
        <script src="{{ asset('Hottel/js/vendor/foundation.js') }}"></script>
        <script src="{{ asset('Hottel/js/app.js') }}"></script>
        <script src="{{ asset('Hottel/pickadate/lib/picker.js') }}"></script>
        <script src="{{ asset('Hottel/pickadate/lib/picker.date.js') }}"></script>
        <script>
            $('.datepicker').pickadate(
              { 
                format: 'yyyy-mm-dd',
                formatSubmit: 'yyyy-mm-dd' 
              }
              );
        </script>

    </body>
</html>