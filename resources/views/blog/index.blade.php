@extends('layouts.master')

@section('content')
<div class="row">
    <div class="col-md-12 text-center">
        <br />
        <p class="quote text-center">The beautiful Posts</p> <br />
        @if(!Auth::check())
        <a href="{{route('login')}}" class="btn btn-success btn-lg btn-block">Login to New post</a>
        <button type="button" class="btn btn-primary" style="color: #333;">Primary</button>
        <button type="button" class="btn btn-secondary" style="color: #333;">Secondary</button>
        <button type="button" class="btn btn-success" style="color: #333;">Success</button>
        <button type="button" class="btn btn-danger" style="color: #333;">Danger</button>
        <button type="button" class="btn btn-warning" style="color: #333;">Warning</button>
        <button type="button" class="btn btn-info" style="color: #333;">Info</button>
        <button type="button" class="btn btn-light" style="color: #333;">Light</button>
        <button type="button" class="btn btn-dark" style="color: #333;">Dark</button>
        <button type="button" class="btn btn-link btn-lg" style="color: #333;">Link</button>
        <br>
        <div class="btn-group btn-group-toggle" data-toggle="buttons">
            <label class="btn btn-secondary active">
                <input type="radio" name="options" id="option1" autocomplete="off" checked> Active
            </label>
            <label class="btn btn-secondary">
                <input type="radio" name="options" id="option2" autocomplete="off"> Radio
            </label>
            <label class="btn btn-secondary">
                <input type="radio" name="options" id="option3" autocomplete="off"> Radio
            </label>
        </div>
        @endif
    </div>
</div>

@foreach($posts as $post)
<div class="row">
    <div class="col-md-12 text-center">
        <br />
        <h1 class="post-title">{{ $post->title }}</h1>
        <p style="font-weight: bold" class="text-center">
            @foreach($post->tags as $tag)
            {{ $tag->name }}
            @endforeach
        </p>
        <p class="text-center">{{ $post->content }}!</p>
        <p class="text-center"><a href="{{ route('blog.post', ['id' => $post->id]) }}">Read more...</a></p>
    </div>
</div>
<hr>
@endforeach
<div class="row">
    <div class="col-md-12 text-center">
        {{ $posts->links() }}
    </div>
</div>
@endsection