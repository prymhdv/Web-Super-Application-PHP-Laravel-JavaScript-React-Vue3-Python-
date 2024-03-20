@extends('layouts.master')

@section('content')
   @if (Session::has('info'))
        <div class="row">
            <div class="col-md-12">

                <p class="alert alert-info" role="alert">{{ Session::get('info') }}</p>
            </div>
        </div>
    @endif
<div style="direction: ltr">

        <div class="col-md-12 text-center d-flex-row">

            @if (!Auth::check())
                <a href="{{ route('login') }}" class="btn btn-success btn-lg btn-block">Login to New post</a>
            @else
                <div class="btn btn-primary text-info m-1 p-2">
                    <p class="  d-inline p-5"><i class=" fas  fa-user"></i> UserPanel:</p>
                    <a href="{{ route('Blog.User.index.Route') }}" class="btn btn-success btn-lg btn-block">Mannage</a>
                    <a type="button" class="btn btn-secondary text-black ">Secondary</a>
                    <a type="button" class="btn btn-success text-black">Success</a>
                    <a type="button" class="btn btn-danger text-black">Danger</a>
                    <a type="button" class="btn btn-warning text-black">Warning</a>
                    <a type="button" class="btn btn-info text-black">Info</a>
                    <a type="button" class="btn btn-light text-black">Light</a>
                </div>
            @endif

        </div>

        <div class="container bg-light position-relative m-1 ">
            @foreach ($posts as $post)
                <div class=" card m-3 ">
                    <div class="card-header text-center   p-2 bg-primary text-white">
                        <h1 class="post-title text-dark  text-sm">
                            <a href="#" class="text-decoration-none text-light">{{ $post->user_name }} :</a>
                            {{ $post->title }}
                        </h1>
                    </div>
                    {{-- -------------------------------------------------------- --}}
                    <div class="card-body text-center d-flex p-2 m-2 " >
                        <img class="card p-2" src="{{ asset('img/Logo/s.png') }}" alt="Generic placeholder image"width="50px" height="50px">
                        <p style="font-weight: bold  " class="text-center ">
                            @foreach ($post->tags as $tag)
                                {{ $tag->name }}
                            @endforeach
                        </p>
                        <p class="text-center flex-fill">{{ $post->content }}!</p>
                        <p class="text-center"><a href="{{ route('blog.post.id.Route', ['id' => $post->id]) }}"
                                class="text-primary">Read more...</a></p>
                    </div>
                    {{-- -------------------------------------------------------- --}}
                    <div class="card-footer text-center txt-primary flex-md-row-reverse d-md-flex  justify-content-center ">
                        <div class=" form-floating p-1 ml-auto">
                            <p class="  ">{{ count($post->likes) }}
                                <a class="text-decoration-none"
                                    href="{{ route('blog.post.like.Route', ['id' => $post->id]) }}"><i
                                        class="fas fa-heart"></i>
                                </a>
                            </p>
                        </div>
                        <div class=" form-floating flex-fill ">
                            <textarea class="form-control " placeholder="Leave a comment here" id="floatingTextarea"></textarea>
                            <label for="floatingTextarea">Comments</label>
                            <a href="#" class="btn btn-success btn-sm align-items-center ">Submit</a>
                        </div>
                    </div>
                    {{-- -------------------------------------------------------- --}}
                </div>
            @endforeach
        </div>
        {{-- post link  ---------------------------------------------------- --- --}}
        {{-- post link  ---------------------------------------------------- --- --}}
        <div class=" rounded ">
            {{ $posts->links('vendor.pagination.bootstrap-5') }}
        </div>
        {{-- post link  ---------------------------------------------------- --- --}}
        {{-- post link  ---------------------------------------------------- --- --}}
    </div>
@endsection
