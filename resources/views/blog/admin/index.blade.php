@extends('layouts.master')

@section('content')
    @if (Session::has('info'))
        <div class="row">
            <div class="col-md-12">

                <p class="alert alert-info" role="alert">{{ Session::get('info') }}</p>
            </div>
        </div>
    @elseif (Session::has('danger'))
        <div class="row">
            <div class="col-md-12">
                <div class="alert alert-success" role="alert">
                    <h4 class="alert-heading">Well done!</h4>
                    <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit
                        longer so that you can see how spacing within an alert works with this kind of content.</p>
                    <hr>
                    <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
                </div>
                <div class="alert alert-warning alert-dismissible fade show" role="alert">
                    <strong>Holy guacamole!</strong> You should check in on some of those fields below.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
                <p class="alert alert-danger" role="alert">{{ Session::get('danger') }}</p>
            </div>
        </div>
    @endif
    <div class="row">
        <div class="col-md-12">
            <a href="{{ route('Blog.User.new.Route') }}" class="btn btn-success btn-lg">New Post</a>

        </div>
    </div>
    <hr>

    @foreach ($posts as $post)
        <div class="col-md-auto flex-md-row bg-light card m-1 p-2">
            {{-- @dd($post->user_name); --}}

            <div class="flex-md-fill ">
                <p class=" text-dark font-weight-light col-md-auto text-truncate">
                    <strong> <a href="#" class="text-decoration-none">{{ $post->user_name }} :</a>
                    </strong> {{ $post->title }}
                </p>
            </div>
            <div class="flex-md ">
                <a class=" btn btn-info" href="{{ route('Blog.User.edit.Route', ['id' => $post->id]) }}">Edit</a>
                <a class=" btn btn-warning"href="{{ route('Blog.User.delete.Route', ['id' => $post->id]) }}">Delete</a>
            </div>
        </div>
    @endforeach
@endsection
