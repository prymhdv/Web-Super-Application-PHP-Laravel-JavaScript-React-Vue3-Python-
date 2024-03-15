@extends('layouts.master')

@section('content')
<div class="row">
    <div class="col-md-12 text-center">
        <br />
        <p class="quote text-center">The beautiful Posts</p> <br />
        @if(!Auth::check())
        <a href="{{route('login')}}" class="btn btn-success btn-lg btn-block">Login to New post</a>
        <button type="button" class="btn btn-primary text-info" >Primary</button>
        <button type="button" class="btn btn-secondary text-black " >Secondary</button>
        <button type="button" class="btn btn-success text-black"  >Success</button>
        <button type="button" class="btn btn-danger text-black"  >Danger</button>
        <button type="button" class="btn btn-warning text-black"  >Warning</button>
        <button type="button" class="btn btn-info text-black"   >Info</button>
        <button type="button" class="btn btn-light text-black"  >Light</button>
        <button type="button" class="btn btn-dark text-black"  >Dark</button>
        <button type="button" class="btn btn-link text-black btn-lg" >Link</button>
        <br>
         
        @endif
    </div>
</div>
<div class="container bg-light  position-relative m-1 " >
    @foreach($posts as $post)
            <div class=" card m-3 ">
                <div class="card-header text-center   p-2 bg-primary text-white">
                    <h1 class="post-title">{{ $post->title }}</h1>
                </div>
                <div class="post-body text-center alert-primary">
                    <img class="mr-3 position-absolute p-2 " src="{{asset('img/Logo/s.png')}}" alt="Generic placeholder image" width="50px" height="50px">
                    <p style="font-weight: bold" class="text-center">
                        @foreach($post->tags as $tag)
                        {{ $tag->name }}
                        @endforeach
                    </p>
                    <p class="text-center">{{ $post->content }}!</p>
                    <p class="text-center"><a href="{{ route('blog.post', ['id' => $post->id]) }}" class="text-primary">Read more...</a></p>
                </div>
        </div>
    @endforeach
</div>
<div class="container p-2 col-12 bg-secondary rounded ">
    {{ $posts->links() }}
</div>
@endsection