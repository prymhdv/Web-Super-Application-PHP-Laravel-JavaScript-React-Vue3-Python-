 
<nav class="HeaderMenu">
    <div class="upper-Sec">
        <div class="container-fluid">
            <div class="col-md-8">
                <ul class="navbar-right">
                    <!-- Authentication Links -->
                    <!-- <span class="glyphicon glyphicon-log-in"> -->
                    <!-- @guest
                            @if (Route::has('login'))  
                            <li> <a href="{{ route('login') }}">{{ __('ورود') }}</a> </li>
                            @endif
                            @if (Route::has('register'))
                            <li> <a href="{{ route('register') }}"><span class="glyphicon glyphicon-user"></span> {{ __('عضویت') }}</a> </li>
                            @endif
                            @else
                            <li class="nav-item dropdown">
                                <a id="navbarDropdown" class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" v-pre>
                                    {{ Auth::user()->name }}
                                </a>

                                <div class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                                    <a class="dropdown-item" href="{{ route('logout') }}" onclick="event.preventDefault();
                                                     document.getElementById('logout-form').submit();">
                                        {{ __('Logout') }}
                                    </a>

                                    <form id="logout-form" action="{{ route('logout') }}" method="POST" class="d-none">
                                        @csrf
                                    </form>
                                </div>
                            </li>
                            @endguest -->
                    <!-- Authentication Links 2 -->
                    @if(!Auth::check())
                    <li> <a href="{{ route('login') }}">{{ __('ورود') }}</a> </li>
                    <li> <a href="{{ route('register') }}"><span class="glyphicon glyphicon-user"></span> {{ __('عضویت') }}</a> </li>
                    @else
                    <!-- <a class="dropdown-item" href="{{ route('logout') }}" onclick="event.preventDefault();
                                                     document.getElementById('logout-form').submit();">
                                        {{ __('خروج') }}
                                    </a>

                                    <form id="logout-form" action="{{ route('logout') }}" method="POST" class="d-none">
                                        @csrf
                                    </form> -->
                    <li class="nav-item dropdown">
                        <a id="navbarDropdown" class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" v-pre>
                            {{ Auth::user()->name }}
                        </a>

                        <div class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" 
                               href="{{ route('logout') }}" 
                               onclick="event.preventDefault(); document.getElementById('logout-form').submit();">
                                {{ __('خروج') }}
                            </a>
                            <form id="logout-form" action="{{ route('logout') }}" method="POST" class="d-none">@csrf</form>
                        </div>
                    </li>
                    @endif
                </ul>
                <!-- 
				<li><a href="{{ url('/login') }}">Login</a></li>
                <li><a href="{{ url('/register') }}">Register</a></li>
				
				  <li>
                    <a href="{{ url('/logout') }}"
                       onclick="event.preventDefault();
                                                 document.getElementById('logout-form').submit();">
                        Logout
                    </a>

                    <form id="logout-form" action="{{ url('/logout') }}" method="POST" style="display: none;">
                        {{ csrf_field() }}
                    </form>
                </li>
				-->
                <a href="{{ route('main.index2') }}" class="navbar-brand bran_bt" style="font-size: 30px">فروشگاه مصالح و تجهیزات ساختمانی </a>
                <ul class="nav navbar-left">
                    {{-- <li><a href="route('views.blog.index.blade.php')">Blog</a></li>--}}
                    {{-- <li><a href="{{ route('other.about') }}">about</a></li>--}}
                    <li><a href="{{route('main.index2')}}">صفحه اصلی</a></li>
                    <li><a href="{{route('Products.index')}}">محصولات</a></li>
                    {{-- <li><a href="{{route('Online-Shopping.index')}}">فروشگاه</a></li>--}}
                    <li><a href="{{route('blog.index')}}">وبلاگ</a></li>
                    <li><a href="{{route('other.about')}}">درباره ما</a></li>
                    <li><a href="{{route('testJS')}}">JS</a></li>
                    <li><a href="{{route('hotel_home')}}">Hottel</a></li>
                    {{-- <li><a href="{!!   route('other.about')  !!}">About !! </a></li>--}}

                </ul>
            </div>
            <div class="col-md-auto">
                <img src="img/Logo/logo.png" alt="" class="site-Brand">
            </div>
        </div>
    </div>
    <div class="below-Sec center-block">
        <div class="container-fluid">
            <div class="Search_box ">
                <form action="">
                    <input type="text" name="" placeholder="جستجو کنید...">
                    <button type="submit" class="fa fa-search"></button>
                </form>
            </div>
            <div class="col-md-8">
                <i class="fa fa-map-marker "> <a>آذربایجان شرقی - تبریز</a> </i>
                <i class="fa fa-telegram"> <a>0914 555 44 88 </a></i>
                <i class="fa fa-whatsapp"></i>
                <i class="fa fa-instagram"></i>
            </div>
        </div>
    </div>
</nav>


<div class="main-menu fixed-header2">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="menu-item">
                    <ul>
                        <li><a href="#">تجهیزات آشپزخانه</a></li>
                        <li><a href="#">سرویس بهداشتی</a></li>
                        <li><a href="#">پارتیشن بندی</a></li>
                        <li><a href="#">شیرآلات</a></li>
                        <li><a href="#">کلید پریز</a></li>
                        <li><a href="#">کاشی و سرامیک</a></li>
                        <li><a href="#">دکور و سنگ نما</a></li>
                        <li><a href="#">وان جکوزی</a></li>
                        <li><a href="#">آینه و روشویی</a></li>
                        <li><a href="#">لوله و اتصالات</a></li>
                        <li><a href="#">یراق آلات</a></li>
                        <li><a href="#">درب و پنجره</a></li>
                        <li><a href="#">کناف و سقف کاذب</a></li>
                        <li><a href="#">سیم و کابل</a></li>
                        <li><a href="#">کفپوش و پارکت</a></li>
                        <li><a href="#">کامپوزیت‌</a></li>
                        <li><a href="#">گچ پلیمری</a></li>
                        <li><a href="#">لوازم فضای باز</a></li>
                        <li><a href="#">قیرگونی</a></li>
                        <li><a href="#">دیوار گچی</a></li>
                        <li><a href="#">چراغ و روشنایی</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>