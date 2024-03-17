@extends('Hottel.layouts.app')

@section('content')
<div class=" d-flex justify-content-center card- text-center bg-light text-danger m-0" style="width: auto; padding: 0 250px;">
  <div class="card ">

  <div class="card-header bg-secoundry">
            <h4  >{{ $modify == 1 ? 'Modify Client' : 'New Client' }}</h4>  
  </div>
  <div class="card-body ">
  <div class="medium-12 large-12 columns d-flex flex-row">
        
        <form action="{{ $modify == 1 ?   route('hotel_update_client.Route', [ 'client_id' => $client_id]) : route('hotel_create_client.Route') }}" method="post">
          @csrf    {{ csrf_field() }} 
          <div class="medium-4  columns">
            <label>Title</label>
            <select name="title">
            @foreach( $titles as $title )
                          <option value="{{ $title }}" >{{ $title }}.</option>
            @endforeach
                        </select>
          </div>
          <div class="medium-4  columns">
            <label>Name</label>
            <input name="name" type="text" value="{{ old('name') ? old('name') : $name }}">
            <small class="error">{{$errors->first('name')}}</small>
          </div>
          <div class="medium-4  columns">
            <label>Last Name</label>
            <input name="last_name" type="text" value="{{ old('last_name') ? old('last_name') : $last_name }}">
            <small class="error">{{$errors->first('last_name')}}</small>
          </div>
          <div class="medium-8  columns">
            <label>Address</label>
            <input name="address" type="text" value="{{ old('address') ? old('address') : $address }}">
            <small class="error">{{$errors->first('address')}}</small>
          </div>
          <div class="medium-4  columns">
            <label>zip_code</label>
            <input name="zip_code" type="text" value="{{ old('zip_code') ? old('zip_code') : $zip_code }}">
            <small class="error">{{$errors->first('zip_code')}}</small>
          </div>
          <div class="medium-4  columns">
            <label>City</label>
            <input name="city" type="text" value="{{ old('city') ? old('city') : $city }}">
            <small class="error">{{$errors->first('city')}}</small>
          </div>
          <div class="medium-4  columns">
            <label>State</label>
            <input name="state" type="text" value="{{ old('state') ? old('state'): $state }}">
            <small class="error">{{$errors->first('state')}}</small>
          </div>
          <div class="medium-12  columns">
            <label>Email</label>
            <input name="email" type="text" value="{{ old('email') ? old('email') : $email }}">
            <small class="error">{{$errors->first('email')}}</small>
          </div>
          <div class="medium-12  columns">
            <input name="save" type="submit" value="SAVE" class="button success hollow" type="submit">
            @if($modify == 1 )
            <input name="delete" type="submit" value="DELETE" class="button success hollow" type="submit">
            @endif
          </div>
        </form>
      </div>
     
    </div>

      <div class="medium-12 large-12 columns">
        {{-- <button type="submit" class="button success " onclick="event.preventDefault(); document.getElementById('delete-client').submit();">  {{ __('DELETE') }}  </button> --}}
        {{-- @if (Auth::check()) <form id="delete-client" action="{{ route('hotel_update_client', [ 'client_id' => $client_id])  }}" method="POST" class="d-none">  @csrf  </form>  @endif --}}
     
      </div>
    </div>  
  </div>
@endsection