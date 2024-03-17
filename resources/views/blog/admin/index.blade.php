@extends('layouts.master')

@section('content')
    @if(Session::has('info'))
        <div class="row">
            <div class="col-md-12">
                <p class="alert alert-info">{{ Session::get('info') }}</p>
            </div>
        </div>
    @endif
    <div class="row">
        <div class="col-md-12">
            <a href="{{ route('Blog.User.create.Route') }}" class="btn btn-success btn-lg">New Post</a>
            
        </div>
    </div>
    <hr>
    @foreach($posts as $post)
    <div class="row">
        <div class="col-md-12">
            <p><strong>{{ $post->title }}</strong>
                <a href="{{ route('Blog.User.edit.Route', ['id' => $post->id]) }}">Edit</a>
                <a href="{{ route('Blog.User.delete.Route', ['id' => $post->id]) }}">Delete</a>
            </p>
        </div>
    </div>
    @endforeach
@endsection