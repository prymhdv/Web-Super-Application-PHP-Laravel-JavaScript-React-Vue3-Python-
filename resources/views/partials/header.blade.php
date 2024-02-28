<script data-cfasync="false" type="text/javascript" src="https://code.jquery.com/jquery.min.js"></script>
<script>
    var $a= $.noConflict(true);
    $a(window).scroll(function(){
        if ($a(window).scrollTop() >= 300) {
            $a('.cg-menu-below').addClass('fixed-header');
        }
        else {
            $a('.cg-menu-below').removeClass('fixed-header');
        }
    });
</script>



<nav class="HeaderMenu">
    <div class="upper-Sec">
        <div class="container-fluid">
         <div class="col-md-8">
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#"><span class="glyphicon glyphicon-user"></span> عضویت</a></li>
                <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> ورود</a></li>
            </ul>
            <a href="{{ route('main.index2') }}" class="navbar-brand bran_bt" style="font-size: 30px">فروشگاه مصالح و تجهیزات ساختمانی </a>
            <ul class="nav navbar-nav">
                {{--                <li><a href="route('views.blog.index.blade.php')">Blog</a></li>--}}
                {{--                <li><a href="{{ route('other.about') }}">about</a></li>--}}
                <li><a href="{{route('main.index2')}}">صفحه اصلی</a></li>
                <li><a href="{{route('Products.index')}}">محصولات</a></li>
{{--                <li><a href="{{route('Online-Shopping.index')}}">فروشگاه</a></li>--}}
                <li><a href="{{route('blog.index')}}">وبلاگ</a></li>
                <li><a href="{{route('other.about')}}">درباره ما</a></li>
                {{--                <li><a href="{!!   route('other.about')  !!}">About !! </a></li>--}}
            </ul>
         </div>
        <div class="col-md-auto">
            <img src="{{ asset('img/Logo/logo.png') }}" alt="" class="site-Brand">
        </div>
    </div>
    </div>
    <div class="below-Sec">
    <div class="container-fluid">
        <div class="Search_box center-block">
                <form action="">
                    <input type="text" name="" placeholder="جستجو کنید...">
                    <button type="submit" class="fa fa-search"></button>
                </form>
            </div>
        <div class="col-md-8 center-block">
            <i class="fa fa-map-marker "> <a>آذربایجان شرقی، تبریز ، ما بین لاله و ابوریجان ، میدان ابوذر (داش ساختمان)</a> </i>
        </div>
        <div class="col-md-auto center-block">
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

