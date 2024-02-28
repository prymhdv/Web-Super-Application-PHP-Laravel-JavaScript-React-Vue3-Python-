@extends('layouts.master')
@section('content')
    <div class="row">
        <div class="col-md-12">
            <p class="quote">خوش آمد گویی</p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12 text-center">
            <h1 class="post-title">مطالعه ویژگی ها</h1>
            <p>بهترین نوع جنس ها چیست؟</p>
            <p><a href="{{ route('main.index', ['id' => 1]) }}">مطالعه بیشتر...</a></p>
        </div>
    </div>
    <hr>
@endsection
