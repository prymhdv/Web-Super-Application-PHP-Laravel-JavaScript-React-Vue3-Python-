@extends('layouts.master')
@section('content')
    <div class="HomePage" style="direction: rtl;">
        <hr>

        {{-- <div class="slider-box text-center"> --}}
        {{-- <div class="container"> --}}
        {{-- <div class="row"> --}}
        {{-- <div class="col-md-12"> --}}
        {{-- <h1>پر فروش ترین محصولات</h1> --}}
        {{-- <p> ارسال رایگان، مشاوره خرید، تضمین کیفیت</p> --}}
        {{-- <a href="#" class="site-btn">بیشتر بخوانید <i class="fa fa-long-arrow-left"> </i></a> --}}
        {{-- </div> --}}
        {{-- </div> --}}
        {{-- </div> --}}
        {{-- </div> --}}

        {{-- img/Slider/164-600x403.jpg --}}
        <div class="container gallery_bx">
            <h4>تصاویر محصولات</h4>
            <div class="gallery"><?php
            // (B) GET IMAGES IN GALLERY FOLDER
            $dirImage = __DIR__ . DIRECTORY_SEPARATOR . 'img' . DIRECTORY_SEPARATOR . 'Slider';
            // (C) OUTPUT IMAGES
            $valid_ext = ['jpg', 'gif', 'jpeg', 'svg', 'bmp']; // valid extensions
            foreach (new DirectoryIterator($dirImage) as $fileInfo) {
                // interator
                if (in_array($fileInfo->getExtension(), $valid_ext)) {
                    // in $valid_ext
                    //                                echo $fileInfo->getFilename() . "<br>\n"; // do something here
                    //                                printf("<img src='img/Slider/%s'>", $fileInfo->getFilename());
                    $img = $fileInfo->getFilename();
                    $caption = substr($img, 0, strrpos($img, '.'));
                    printf("<figure><img src='img/Slider/%s'><figcaption>%s</figcaption></figure>", rawurlencode($img), $caption);
                }
            }
            ?>
            </div>
            <div class="photo-next">
                <nav aria-label="Page navigation example">
                    <ul class="pagination">
                        <li class="page-item">
                            <a class="page-link" href="#" aria-lable="Previous">
                                <span aria-hidden="true">&laquo;</span>
                                <span class="sr-only">Previous</span>
                            </a>
                        </li>
                        <li class="page-item"><a class="page-link" href="#">1</a></li>
                        <li class="page-item"><a class="page-link" href="#">2</a></li>
                        <li class="page-item"><a class="page-link" href="#">3</a></li>
                        <li class="page-item">
                            <a class="page-link" href="#" aria-lable="Next">
                                <span aria-hidden="true">&raquo;</span>
                                <span class="sr-only">Next</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>

        <div class="services">
            <div class="container ">
                <div class="row">

                    <div class="col-md-4">
                        <div class="desc">
                            <h4>محصولات</h4>
                            <span> شیرآلات</span>
                            <p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.
                                چاپگرها و
                                متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد
                                نیاز و کاربردهای
                                متنوع با هدف بهبود ابزارهای کاربردی می باشد. کتابهای زیادی در شصت و سه درصد گذشته، حال و
                                آینده شناخت
                                فراوان جامعه و متخصصان را می طلبد تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای
                                علی الخصوص
                                طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد کرد. در این صورت می توان امید داشت که تمام و
                                دشواری موجود
                                در ارائه راهکارها و شرایط سخت تایپ به پایان رسد وزمان مورد نیاز شامل حروفچینی دستاوردهای
                                اصلی و جوابگوی
                                سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد.</p>
                            <div class="text-left">
                                <a href="#" class="site-btn">بیشتر</a>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-8">
                        <div class="col-md-6">
                            <div class="item">
                                <i class="fas  fa-users"></i>
                                <span>پشتیبانی آنلاین</span>
                                <P>زمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود
                                    طراحی اساسا مورد
                                    استفاده قرار گیرد.</P>
                            </div>
                        </div>

                        <div class="col-md-6">
                            <div class="item">
                                <i class="fas  fa-map-marker"></i>
                                <span>نقشه و لوکیشن</span>
                                <P>زمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود
                                    طراحی اساسا مورد
                                    استفاده قرار گیرد.</P>
                            </div>
                        </div>
                        <div class="col-md-6">

                            <div class="item">
                                <i class="fas  fa-cogs"></i>
                                <span>تنظیمات پیشرفته</span>
                                <P>زمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود
                                    طراحی اساسا مورد
                                    استفاده قرار گیرد.</P>
                            </div>
                        </div>

                        <div class="col-md-6">
                            <div class="item">
                                <i class="fas  fa-ticket"></i>
                                <span>تیک آنلاین</span>
                                <P>زمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود
                                    طراحی اساسا
                                    مورد استفاده قرار گیرد.</P>
                            </div>
                        </div>


                    </div>
                </div>
            </div>
        </div>
        <div class="index-blog">
            <div class="container">
                <div class="row row1">
                    <div class="col-md-6">
                        <div class="desc">
                            <h4>عنوان مطالب در این قسمت باشد.</h4>
                            <div class="meta">
                                <span>
                                    <i class="fas fa-calender-o">99.9.16</i>
                                    <i class="fab fa-comment-o">10 نظر</i>
                                </span>
                            </div>
                            <p> با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو
                                در زبان فارسی
                                ایجاد کرد. در این صورت می توان امید داشت</p>
                            <div class="text-left">
                                <a href="#" class="site-btn">بیشتر</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="pic">
                            <img src="img/Slider/51N3x6y16DS._AC_UL320_.jpg" alt="" class="image-rounded">

                        </div>
                    </div>
                </div>
                <div class="row  row2">

                    <div class="col-md-6">
                        <div class="pic">
                            <img src="img/Slider/51oYZFK3OdL._AC_UL320_.jpg" alt="" class="image-rounded">

                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="desc">
                            <h4>عنوان مطالب در این قسمت باشد.</h4>
                            <div class="meta">
                                <span>
                                    <i class="fas fa-calender-o">99.9.16</i>
                                    <i class="fas fa-comment-o">10 نظر</i>
                                </span>
                            </div>
                            <p> با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو
                                در زبان فارسی
                                ایجاد کرد. در این صورت می توان امید داشت</p>
                            <div class="text-left">
                                <a href="#" class="site-btn">بیشتر</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row row3">
                    <div class="col-md-6">
                        <div class="desc">
                            <h4>عنوان مطالب در این قسمت باشد.</h4>
                            <div class="meta">
                                <span>
                                    <i class="fas fa-calender-o">99.9.16</i>
                                    <i class="fas fa-comment-o">10 نظر</i>
                                </span>
                            </div>
                            <p> با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو
                                در زبان فارسی
                                ایجاد کرد. در این صورت می توان امید داشت</p>
                            <div class="text-left">
                                <a href="#" class="site-btn">بیشتر</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="pic">
                            <img src="img/Slider/51wPNrXJaNL._AC_UL320_.jpg" alt="" class="image-rounded">

                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="site_boxes_content">
            <div class="container">
                <div class="row">
                    <div class="col-md-6">
                        <div class="box">
                            <span class="title">محصولات پر بازدید</span>
                            <div class="post-item-bx">
                                <div class="col-md-5">
                                    <div class="pic">
                                        <img src="img/Products/ww.jpg" alt="">
                                    </div>
                                </div>
                                <div class="col-md-7">
                                    <div class="desc">
                                        <h5>شیرآلات</h5>
                                        <p>برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد
                                            کرد. </p>
                                        <span><i class="fas fa-calender-o">99.9.10</i></span>
                                    </div>
                                </div>
                                <div class="col-md-5">
                                    <div class="pic">
                                        <img src="img/Products/rr.jpg" alt="">
                                    </div>
                                </div>
                                <div class="col-md-7">
                                    <div class="desc">
                                        <h5>شیرآلات</h5>
                                        <p>برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد
                                            کرد. </p>
                                        <span><i class="fas fa-calender-o">99.9.10</i></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="box">
                            <span class="title">محصولات جدید</span>
                            <div class="post-item-bx">
                                <div class="col-md-5">
                                    <div class="pic">
                                        <img src="img/Products/ff.jpg" alt="">
                                    </div>
                                </div>
                                <div class="col-md-7">
                                    <div class="desc">
                                        <h5>شیرآلات</h5>
                                        <p>برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد
                                            کرد. </p>
                                        <span><i class="fas fa-calender-o">99.9.10</i></span>
                                    </div>
                                </div>
                                <div class="col-md-5">
                                    <div class="pic">
                                        <img src="img/Products/dd.jpg" alt="">
                                    </div>
                                </div>
                                <div class="col-md-7">
                                    <div class="desc">
                                        <h5>شیرآلات</h5>
                                        <p>برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد
                                            کرد. </p>
                                        <span><i class="fas fa-calender-o">99.9.10</i></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
@endsection
