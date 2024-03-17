<!--Header ------------------------------------------------------------------------------------------------ -->
<!--Header ------------------------------------------------------------------------------------------------ -->
<div class= "d-flex flex-column min-vh-0" style="direction: rtl;">
    {{-- ------------------------------------------------------------------------------------------- navbar navbar-dark justify-content-cente fixed-top sticky-top --}}
    {{-- ------------------------------------------------------------------------------------------- --}}
    {{--  --}}
    {{--  --}}
    {{--  --}}
    <!-- Modal Form -->

    <div class=" modal fade  " id="ModalForm" tabindex="-1" aria-hidden="true"style="direction: ltr;">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <!-- Login Form -->
                <form method="POST" role="form" id="login_form" action="{{ route('auth.signin.Route') }}">
                    {{ csrf_field() }}
                    <div class="modal-header">
                        <h5 class="modal-title">Modal Login Form</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <input id="email" type="email" class="form-control @error('email') is-invalid @enderror"
                            name="email" value="{{ old('email') }}" required autocomplete="email" autofocus
                            placeholder="username ">
                        @error('email')
                            <span class="invalid-feedback" role="alert">
                                <strong>{{ $message }}</strong>
                            </span>
                        @enderror
                        </div>

                        <div class="mb-3">
                            <label for="Password">Password<span class="text-danger">*</span></label>
                            <input id="password" type="password"
                                class="form-control @error('password') is-invalid @enderror" name="password" required
                                autocomplete="current-password" placeholder="password">

                            @error('password')
                                <span class="invalid-feedback" role="alert">
                                    <strong>{{ $message }}</strong>
                                </span>
                            @enderror
                        </div>
                        <div class="mb-3">
                            {{-- <input class="form-check-input" type="checkbox" value="" id="remember" required> --}}
                           
                            <input class="form-check-input" type="checkbox" name="remember" id="remember"
                                {{ old('remember') ? 'checked' : '' }}> Remember Me
                                {{-- ----------------------- --}}
                            <a href="#" class="float-end text-warning">Forgot Password?</a>
                        </div>
                    </div>
                    <div class="modal-footer pt-4">
                       
                         <button type="submit" value="Login" class="btn btn-success mx-auto w-100">Login</button>
                      
                    </div>
                    <p class="text-center text-warning">Not yet account, <a class="text-center text-primary"
                            href="#">Signup</a></p>
                </form>
            </div>
        </div>
    </div>
    {{--  --}}
    {{--  --}}
    {{--  --}}
    <div class="Main_Header">
        <!-- ---------------------------------------------------------------------------------------------------- -->
        <nav class=" navbar navbar-expand-sm navbar-dark bg-primary fixed-top p-0 m-0  mb-0">


            <button class=" navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggle">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="col-5 collapse navbar-collapse text-center" id="navbarToggle">
                <ul class="nav nav-list nav navbar-nav m-auto ">
                    {{-- <li><a href="route('views.blog.index.blade.php')">Blog</a></li> --}}
                    {{-- <li><a href="{{ route('other.about') }}">about</a></li> --}}
                    <li class="nav-item"><a class="nav-link " href="{{ route('main.index2.Route') }}">صفحه
                            اصلی</a></li>
                    <li class="nav-item"><a class="nav-link " href="{{ route('Products.index.Route') }}">محصولات</a>
                    </li>
                    {{-- <li><a href="{{route('Online-Shopping.index')}}">فروشگاه</a></li> --}}
                    <li class="nav-item"><a class="nav-link " href="{{ route('blog.post.index.Route') }}">وبلاگ</a></li>
                    <li class="nav-item"><a class="nav-link " href="{{ route('other.about.Route') }}">درباره ما</a>
                    </li>

                    <li class="nav-item"><a class="nav-link " href="{{ route('bootstrap.Route') }}">bootstrap</a>
                    </li>
                    <li class="nav-item"><a class="nav-link " href="{{ route('testJS.Route') }}">JS</a></li>
                    <li class="nav-item"><a class="nav-link " href="{{ route('VueJs.Route') }}">Vue.JS</a></li>
                    <li class="nav-item"><a class="nav-link " href="{{ route('ReactJs.Route') }}">React.JS</a></li>
                    <li class="nav-item"><a class="nav-link " href="{{ route('hotel_home.Route') }}">Hottel</a></li>
                    {{-- <li><a href="{!!   route('other.about')  !!}">About !! </a></li> --}}
                </ul>
            </div>

            <!-- ---------------------------------------------------------- -->
            <div class="col-6 m-auto Authentication" style="display: inline-block; right:0; color:black;">
                <!-- Authentication Links -->

                <ul class="m-1 m-auto">
                    <!-- Authentication Links 2 -->
                    <!-- <span class="glyphicon glyphicon-log-in"> -->
                    {{-- @if (Route::has('register'))     @if (Route::has('login')) --}}
                    {{-- @dd(Route::has('register')); --}}
                    {{-- @dd(Route::has('blog.index'));   name of route existed or not --}}
                    {{-- @dd(Auth::attemp(['email'=>$email ,'password'=>$password, ....])); --}}
                    {{-- @dd(Auth::check()); --}}
                    {{-- @dd(Auth::user()->name); --}}
                    {{-- @dd(Auth::logout()->name); exit user --}}
                    {{-- @dd(route('logout')); --}}


                    {{-- @if (Auth::check())   @dd('ok ---------');   @endif --}}
                    {{-- @if (!Auth::check())   @dd('no ---------');   @endif --}}
                    @guest
                        {{-- ----------------------------------------------------------------------------------------- --}}
                        {{-- {{ route('auth.signin.Route') }} --}}
                        @if (!Auth::check())
                            <li class="m-1 p-1"> <a id="myBtn" href="#" data-bs-toggle="modal"
                                    data-bs-target="#ModalForm"><span class="fas fa-sign-in fa-sm fa-fw"></span>
                                    {{ __('ورود') }}</a> </li>
                            <li class="m-1 p-1"> <a href="{{ route('register') }}" data-bs-toggle="modal"
                                    data-bs-target="#exampleModalCenter"><span class="fas fa-user  fa-sm"></span>
                                    {{ __('عضویت') }}</a> </li>
                            {{-- @elseif(Auth::check())   @dd('ok ---------');        --}}
                            <!-- Trigger the modal with a button -->
                            {{-- <button type="button" class="btn btn-dark btn-lg" id="myBtn">Login</button> --}}
                        @endguest
                        {{-- ----------------------------------------------------------------------------------------- --}}
                    @else
                        <li class=" ">
                            <div class="dropdown-center">
                                <button class="btn btn-warning dropdown-toggle" type="button"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    user: {{ Auth::user()->name }}
                                </button>
                                <ul class="dropdown-menu bg-dark">

                                    {{-- {{ route('Auther/logout') }} cant name clas auth --}}
                                    <a href="{{ url('Auther/logout') }}"
                                        onclick="event.preventDefault();  document.getElementById('logout-form').submit();">
                                        Logout
                                    </a>

                                    <form id="logout-form" action="{{ url('Auther/logout') }}" method="POST"
                                        class="d-none">
                                        {{ csrf_field() }}
                                    </form>
                                </ul>
                            </div>

                        </li>
                    @endif
                    {{-- ----------------------------------------------------------------------------------------- --}}

                </ul>





            </div>
        </nav>


        <section class="" style="direction: ltr;">

            <div class="BoxUp ">
                <a href="{{ route('main.index2.Route') }}" class="bran_bt" style="font-size: 4vh">فروشگاه مصالح و
                    تجهیزات
                    ساختمانی </a>
                <img src="{{ asset('img/Logo/s.png') }}" alt="" class="site-Brand-Logo">

                {{-- ------------------------------------------------------------------------------------------- --}}
                <div class="Search_box ">
                    <form action="">
                        <input type="text" name="" placeholder="جستجو کنید...">
                        <button type="submit" class="fa-solid fa-search  fa-fw"
                            style="font-size:24x;color:rgb(255, 255, 255)"></button>
                    </form>
                </div>

                <div class="Information" style="direction: rtl;">
                    <ul>
                        <li style="display: inline-block;"> <i class="fas           fa-location-dot "
                                style="font-size:24px; "></i> </li>
                        <li style="display: inline-block;"> <a style="font-weight: 100">آذربایجان شرقی - تبریز</a>
                        </li>
                        <li style="display: inline-block;"> <i class="fab fa-brands fa-telegram  "
                                style="font-size:24px; "></i> </li>
                        <li style="display: inline-block;"> <i class="fab fa-brands fa-whatsapp  "
                                style="font-size:24px; "></i></li>
                        <li style="display: inline-block;"> <i class="fab fa-brands fa-instagram "
                                style="font-size:24px; "></i></li>
                        <li style="display: inline-block;"> <a style=>0914-999-99-99</a></li>
                    </ul>

                </div>
            </div>
        </section>

        <!-- ------------------------------------------------------------------------------------------------- -->
        <div class="main-menu fixed-header2">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="menu-item">
                            <ul>
                                <li><a href="{{ route('main.index2.Route') }}">تجهیزات آشپزخانه</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">سرویس بهداشتی</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">پارتیشن بندی</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">شیرآلات</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">کلید پریز</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">کاشی و سرامیک</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">دکور و سنگ نما</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">وان جکوزی</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">آینه و روشویی</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">لوله و اتصالات</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">یراق آلات</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">درب و پنجره</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">کناف و سقف کاذب</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">سیم و کابل</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">کفپوش و پارکت</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">کامپوزیت‌</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">گچ پلیمری</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">لوازم فضای باز</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">قیرگونی</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">دیوار گچی</a></li>
                                <li><a href="{{ route('main.index2.Route') }}">چراغ و روشنایی</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- ------------------------------------------------------------------------------------------------ -->
    </div>
    <!-- ---------------------------------------------------------- -->

</div>

<!--Header ------------------------------------------------------------------------------------------------ -->
<!--Header ------------------------------------------------------------------------------------------------ -->
<div>

    <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog"
        aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-body py-0 p-0">
                    <div class="d-flex main-content">
                        <div class="  mx-auto bg-image promo-img mr-0"
                            style="background-image: url('{{ asset('img/compass/documentation.jpg') }}');  width: 500px; height: auto;">
                        </div>
                        <div class="content-text p-4">
                            <h3>Registration form</h3>
                            <p>All their equipment and instruments are alive. The sky was cloudless and of a deep dark
                                blue.</p>
                            <form method="POST" role="form" id="register_form"
                                action="{{ route('register') }}"> {{ csrf_field() }}
                                <div class="form-group">
                                    <label for="country">Country</label>

                                    <select id="country" name="country" class="custom-select">
                                        <option value="Afghanistan">Afghanistan</option>
                                        <option value="Åland Islands">Åland Islands</option>
                                        <option value="Albania">Albania</option>
                                        <option value="Algeria">Algeria</option>
                                        <option value="American Samoa">American Samoa</option>
                                        <option value="Andorra">Andorra</option>
                                        <option value="Angola">Angola</option>
                                        <option value="Anguilla">Anguilla</option>
                                        <option value="Antarctica">Antarctica</option>
                                        <option value="Antigua and Barbuda">Antigua and Barbuda</option>
                                        <option value="Argentina">Argentina</option>
                                        <option value="Armenia">Armenia</option>
                                        <option value="Aruba">Aruba</option>
                                        <option value="Australia">Australia</option>
                                        <option value="Austria">Austria</option>
                                        <option value="Azerbaijan">Azerbaijan</option>
                                        <option value="Bahamas">Bahamas</option>
                                        <option value="Bahrain">Bahrain</option>
                                        <option value="Bangladesh">Bangladesh</option>
                                        <option value="Barbados">Barbados</option>
                                        <option value="Belarus">Belarus</option>
                                        <option value="Belgium">Belgium</option>
                                        <option value="Belize">Belize</option>
                                        <option value="Benin">Benin</option>
                                        <option value="Bermuda">Bermuda</option>
                                        <option value="Bhutan">Bhutan</option>
                                        <option value="Bolivia">Bolivia</option>
                                        <option value="Bosnia and Herzegovina">Bosnia and Herzegovina</option>
                                        <option value="Botswana">Botswana</option>
                                        <option value="Bouvet Island">Bouvet Island</option>
                                        <option value="Brazil">Brazil</option>
                                        <option value="British Indian Ocean Territory">British Indian Ocean Territory
                                        </option>
                                        <option value="Brunei Darussalam">Brunei Darussalam</option>
                                        <option value="Bulgaria">Bulgaria</option>
                                        <option value="Burkina Faso">Burkina Faso</option>
                                        <option value="Burundi">Burundi</option>
                                        <option value="Cambodia">Cambodia</option>
                                        <option value="Cameroon">Cameroon</option>
                                        <option value="Canada">Canada</option>
                                        <option value="Cape Verde">Cape Verde</option>
                                        <option value="Cayman Islands">Cayman Islands</option>
                                        <option value="Central African Republic">Central African Republic</option>
                                        <option value="Chad">Chad</option>
                                        <option value="Chile">Chile</option>
                                        <option value="China">China</option>
                                        <option value="Christmas Island">Christmas Island</option>
                                        <option value="Cocos (Keeling) Islands">Cocos (Keeling) Islands</option>
                                        <option value="Colombia">Colombia</option>
                                        <option value="Comoros">Comoros</option>
                                        <option value="Congo">Congo</option>
                                        <option value="Congo, The Democratic Republic of The">Congo, The Democratic
                                            Republic of The</option>
                                        <option value="Cook Islands">Cook Islands</option>
                                        <option value="Costa Rica">Costa Rica</option>
                                        <option value="Cote D'ivoire">Cote D'ivoire</option>
                                        <option value="Croatia">Croatia</option>
                                        <option value="Cuba">Cuba</option>
                                        <option value="Cyprus">Cyprus</option>
                                        <option value="Czech Republic">Czech Republic</option>
                                        <option value="Denmark">Denmark</option>
                                        <option value="Djibouti">Djibouti</option>
                                        <option value="Dominica">Dominica</option>
                                        <option value="Dominican Republic">Dominican Republic</option>
                                        <option value="Ecuador">Ecuador</option>
                                        <option value="Egypt">Egypt</option>
                                        <option value="El Salvador">El Salvador</option>
                                        <option value="Equatorial Guinea">Equatorial Guinea</option>
                                        <option value="Eritrea">Eritrea</option>
                                        <option value="Estonia">Estonia</option>
                                        <option value="Ethiopia">Ethiopia</option>
                                        <option value="Falkland Islands (Malvinas)">Falkland Islands (Malvinas)
                                        </option>
                                        <option value="Faroe Islands">Faroe Islands</option>
                                        <option value="Fiji">Fiji</option>
                                        <option value="Finland">Finland</option>
                                        <option value="France">France</option>
                                        <option value="French Guiana">French Guiana</option>
                                        <option value="French Polynesia">French Polynesia</option>
                                        <option value="French Southern Territories">French Southern Territories
                                        </option>
                                        <option value="Gabon">Gabon</option>
                                        <option value="Gambia">Gambia</option>
                                        <option value="Georgia">Georgia</option>
                                        <option value="Germany">Germany</option>
                                        <option value="Ghana">Ghana</option>
                                        <option value="Gibraltar">Gibraltar</option>
                                        <option value="Greece">Greece</option>
                                        <option value="Greenland">Greenland</option>
                                        <option value="Grenada">Grenada</option>
                                        <option value="Guadeloupe">Guadeloupe</option>
                                        <option value="Guam">Guam</option>
                                        <option value="Guatemala">Guatemala</option>
                                        <option value="Guernsey">Guernsey</option>
                                        <option value="Guinea">Guinea</option>
                                        <option value="Guinea-bissau">Guinea-bissau</option>
                                        <option value="Guyana">Guyana</option>
                                        <option value="Haiti">Haiti</option>
                                        <option value="Heard Island and Mcdonald Islands">Heard Island and Mcdonald
                                            Islands</option>
                                        <option value="Holy See (Vatican City State)">Holy See (Vatican City State)
                                        </option>
                                        <option value="Honduras">Honduras</option>
                                        <option value="Hong Kong">Hong Kong</option>
                                        <option value="Hungary">Hungary</option>
                                        <option value="Iceland">Iceland</option>
                                        <option value="India">India</option>
                                        <option value="Indonesia">Indonesia</option>
                                        <option value="Iran, Islamic Republic of">Iran, Islamic Republic of</option>
                                        <option value="Iraq">Iraq</option>
                                        <option value="Ireland">Ireland</option>
                                        <option value="Isle of Man">Isle of Man</option>
                                        <option value="Israel">Israel</option>
                                        <option value="Italy">Italy</option>
                                        <option value="Jamaica">Jamaica</option>
                                        <option value="Japan">Japan</option>
                                        <option value="Jersey">Jersey</option>
                                        <option value="Jordan">Jordan</option>
                                        <option value="Kazakhstan">Kazakhstan</option>
                                        <option value="Kenya">Kenya</option>
                                        <option value="Kiribati">Kiribati</option>
                                        <option value="Korea, Democratic People's Republic of">Korea, Democratic
                                            People's Republic of</option>
                                        <option value="Korea, Republic of">Korea, Republic of</option>
                                        <option value="Kuwait">Kuwait</option>
                                        <option value="Kyrgyzstan">Kyrgyzstan</option>
                                        <option value="Lao People's Democratic Republic">Lao People's Democratic
                                            Republic</option>
                                        <option value="Latvia">Latvia</option>
                                        <option value="Lebanon">Lebanon</option>
                                        <option value="Lesotho">Lesotho</option>
                                        <option value="Liberia">Liberia</option>
                                        <option value="Libyan Arab Jamahiriya">Libyan Arab Jamahiriya</option>
                                        <option value="Liechtenstein">Liechtenstein</option>
                                        <option value="Lithuania">Lithuania</option>
                                        <option value="Luxembourg">Luxembourg</option>
                                        <option value="Macao">Macao</option>
                                        <option value="Macedonia, The Former Yugoslav Republic of">Macedonia, The
                                            Former Yugoslav Republic of</option>
                                        <option value="Madagascar">Madagascar</option>
                                        <option value="Malawi">Malawi</option>
                                        <option value="Malaysia">Malaysia</option>
                                        <option value="Maldives">Maldives</option>
                                        <option value="Mali">Mali</option>
                                        <option value="Malta">Malta</option>
                                        <option value="Marshall Islands">Marshall Islands</option>
                                        <option value="Martinique">Martinique</option>
                                        <option value="Mauritania">Mauritania</option>
                                        <option value="Mauritius">Mauritius</option>
                                        <option value="Mayotte">Mayotte</option>
                                        <option value="Mexico">Mexico</option>
                                        <option value="Micronesia, Federated States of">Micronesia, Federated States of
                                        </option>
                                        <option value="Moldova, Republic of">Moldova, Republic of</option>
                                        <option value="Monaco">Monaco</option>
                                        <option value="Mongolia">Mongolia</option>
                                        <option value="Montenegro">Montenegro</option>
                                        <option value="Montserrat">Montserrat</option>
                                        <option value="Morocco">Morocco</option>
                                        <option value="Mozambique">Mozambique</option>
                                        <option value="Myanmar">Myanmar</option>
                                        <option value="Namibia">Namibia</option>
                                        <option value="Nauru">Nauru</option>
                                        <option value="Nepal">Nepal</option>
                                        <option value="Netherlands">Netherlands</option>
                                        <option value="Netherlands Antilles">Netherlands Antilles</option>
                                        <option value="New Caledonia">New Caledonia</option>
                                        <option value="New Zealand">New Zealand</option>
                                        <option value="Nicaragua">Nicaragua</option>
                                        <option value="Niger">Niger</option>
                                        <option value="Nigeria">Nigeria</option>
                                        <option value="Niue">Niue</option>
                                        <option value="Norfolk Island">Norfolk Island</option>
                                        <option value="Northern Mariana Islands">Northern Mariana Islands</option>
                                        <option value="Norway">Norway</option>
                                        <option value="Oman">Oman</option>
                                        <option value="Pakistan">Pakistan</option>
                                        <option value="Palau">Palau</option>
                                        <option value="Palestinian Territory, Occupied">Palestinian Territory, Occupied
                                        </option>
                                        <option value="Panama">Panama</option>
                                        <option value="Papua New Guinea">Papua New Guinea</option>
                                        <option value="Paraguay">Paraguay</option>
                                        <option value="Peru">Peru</option>
                                        <option value="Philippines">Philippines</option>
                                        <option value="Pitcairn">Pitcairn</option>
                                        <option value="Poland">Poland</option>
                                        <option value="Portugal">Portugal</option>
                                        <option value="Puerto Rico">Puerto Rico</option>
                                        <option value="Qatar">Qatar</option>
                                        <option value="Reunion">Reunion</option>
                                        <option value="Romania">Romania</option>
                                        <option value="Russian Federation">Russian Federation</option>
                                        <option value="Rwanda">Rwanda</option>
                                        <option value="Saint Helena">Saint Helena</option>
                                        <option value="Saint Kitts and Nevis">Saint Kitts and Nevis</option>
                                        <option value="Saint Lucia">Saint Lucia</option>
                                        <option value="Saint Pierre and Miquelon">Saint Pierre and Miquelon</option>
                                        <option value="Saint Vincent and The Grenadines">Saint Vincent and The
                                            Grenadines</option>
                                        <option value="Samoa">Samoa</option>
                                        <option value="San Marino">San Marino</option>
                                        <option value="Sao Tome and Principe">Sao Tome and Principe</option>
                                        <option value="Saudi Arabia">Saudi Arabia</option>
                                        <option value="Senegal">Senegal</option>
                                        <option value="Serbia">Serbia</option>
                                        <option value="Seychelles">Seychelles</option>
                                        <option value="Sierra Leone">Sierra Leone</option>
                                        <option value="Singapore">Singapore</option>
                                        <option value="Slovakia">Slovakia</option>
                                        <option value="Slovenia">Slovenia</option>
                                        <option value="Solomon Islands">Solomon Islands</option>
                                        <option value="Somalia">Somalia</option>
                                        <option value="South Africa">South Africa</option>
                                        <option value="South Georgia and The South Sandwich Islands">South Georgia and
                                            The South Sandwich Islands</option>
                                        <option value="Spain">Spain</option>
                                        <option value="Sri Lanka">Sri Lanka</option>
                                        <option value="Sudan">Sudan</option>
                                        <option value="Suriname">Suriname</option>
                                        <option value="Svalbard and Jan Mayen">Svalbard and Jan Mayen</option>
                                        <option value="Swaziland">Swaziland</option>
                                        <option value="Sweden">Sweden</option>
                                        <option value="Switzerland">Switzerland</option>
                                        <option value="Syrian Arab Republic">Syrian Arab Republic</option>
                                        <option value="Taiwan, Province of China">Taiwan, Province of China</option>
                                        <option value="Tajikistan">Tajikistan</option>
                                        <option value="Tanzania, United Republic of">Tanzania, United Republic of
                                        </option>
                                        <option value="Thailand">Thailand</option>
                                        <option value="Timor-leste">Timor-leste</option>
                                        <option value="Togo">Togo</option>
                                        <option value="Tokelau">Tokelau</option>
                                        <option value="Tonga">Tonga</option>
                                        <option value="Trinidad and Tobago">Trinidad and Tobago</option>
                                        <option value="Tunisia">Tunisia</option>
                                        <option value="Turkey">Turkey</option>
                                        <option value="Turkmenistan">Turkmenistan</option>
                                        <option value="Turks and Caicos Islands">Turks and Caicos Islands</option>
                                        <option value="Tuvalu">Tuvalu</option>
                                        <option value="Uganda">Uganda</option>
                                        <option value="Ukraine">Ukraine</option>
                                        <option value="United Arab Emirates">United Arab Emirates</option>
                                        <option value="United Kingdom">United Kingdom</option>
                                        <option value="United States">United States</option>
                                        <option value="United States Minor Outlying Islands">United States Minor
                                            Outlying Islands</option>
                                        <option value="Uruguay">Uruguay</option>
                                        <option value="Uzbekistan">Uzbekistan</option>
                                        <option value="Vanuatu">Vanuatu</option>
                                        <option value="Venezuela">Venezuela</option>
                                        <option value="Viet Nam">Viet Nam</option>
                                        <option value="Virgin Islands, British">Virgin Islands, British</option>
                                        <option value="Virgin Islands, U.S.">Virgin Islands, U.S.</option>
                                        <option value="Wallis and Futuna">Wallis and Futuna</option>
                                        <option value="Western Sahara">Western Sahara</option>
                                        <option value="Yemen">Yemen</option>
                                        <option value="Zambia">Zambia</option>
                                        <option value="Zimbabwe">Zimbabwe</option>
                                    </select>

                                </div>
                                {{-- ----------------------------------- --}}
                                <div class="form-group">
                                    <label for="name"
                                        class="col-md-4 col-form-label text-md-end">{{ __('Name') }}</label>
                                    <input id="name" type="text"
                                        class="form-control @error('name') is-invalid @enderror" name="name"
                                        value="{{ old('name') }}" required autocomplete="name" autofocus>

                                    @error('name')
                                        <span class="invalid-feedback" role="alert">
                                            <strong>{{ $message }}</strong>
                                        </span>
                                    @enderror
                                </div>
                                <div class="form-group">
                                    {{-- ----------------------------------- --}}
                                    <label for="email"
                                        class="col-md-4 col-form-label text-md-end">{{ __('Email Address') }}</label>
                                    <input id="email" type="email"
                                        class="form-control @error('email') is-invalid @enderror" name="email"
                                        value="{{ old('email') }}" required autocomplete="email">

                                    @error('email')
                                        <span class="invalid-feedback" role="alert">
                                            <strong>{{ $message }}</strong>
                                        </span>
                                    @enderror
                                    {{-- ----------------------------------- --}}
                                    <label for="password"
                                        class="col-md-4 col-form-label text-md-end">{{ __('Password') }}</label>
                                    <input id="password" type="password"
                                        class="form-control @error('password') is-invalid @enderror" name="password"
                                        required autocomplete="new-password">
                                    @error('password')
                                        <span class="invalid-feedback" role="alert">
                                            <strong>{{ $message }}</strong>
                                        </span>
                                    @enderror
                                    {{-- ----------------------------------- --}}
                                    <label for="password-confirm"
                                        class="col-md-4 col-form-label text-md-end">{{ __('Confirm Password') }}</label>
                                    <input id="password-confirm" type="password" class="form-control"
                                        name="password_confirmation" required autocomplete="new-password">
                                    {{-- ----------------------------------- --}}
                                </div>
                                <div class="form-group row mb-4">
                                    <div class="col-12">
                                        <label for="mm">Date of Birth</label>
                                    </div>
                                    <div class="col-md-4">
                                        <input type="text" class="form-control" id="mm" placeholder="MM">
                                    </div>
                                    <div class="col-md-4">
                                        <input type="text" class="form-control" id="dd" placeholder="DD">
                                    </div>
                                    <div class="col-md-4">
                                        <input type="text" class="form-control" id="yyyy"
                                            placeholder="YYYY">
                                    </div>
                                </div>
                                <div class="form-group">
                                    <input type="submit" value="Sign up" class="btn btn-primary btn-block">
                                </div>
                                <div class="form-group ">
                                    <p class="custom-note"><small>By signing up you will agree to our <a
                                                href="{{ route('register') }}">Privacy Policy</a></small></p>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script type="text/javascript">
        function form_submit() {
            document.getElementById("register_form").submit();
        }

        function form_submit() {
            document.getElementById("login_form").submit();
        }
    </script>
    {{-- 
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
    <script defer src="https://static.cloudflareinsights.com/beacon.min.js/v84a3a4012de94ce1a686ba8c167c359c1696973893317"
        integrity="sha512-euoFGowhlaLqXsPWQ48qSkBSCFs3DPRyiwVu3FjR96cMPx+Fr+gpWRhIafcHwqwCqWS42RZhIudOvEI+Ckf6MA=="
        data-cf-beacon='{"rayId":"865d60bf5e71bbda","version":"2024.2.4","token":"cd0b4b3a733644fc843ef0b185f98241"}'
        crossorigin="anonymous">
    </script> 
--}}
</div>
<!--Header ------------------------------------------------------------------------------------------------ -->
<!--Header ------------------------------------------------------------------------------------------------ -->
