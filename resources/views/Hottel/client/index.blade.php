@extends('Hottel.layouts.app')

@section('content')
<div class="card text-center">
      <div class="medium-12 large-12 columns">
       <div class="div card-header text-center">
        <h4 class="text-danger">Clients List</h4>
      </div> 
      <div class="div bg-primary">

    
        <div class="medium-2  columns m-0 p-3"><a class="button warning" href="{{ route('hotel_new_client') }}">ADD NEW CLIENT</a></div>

        
        <table class="table table-primary p-2 mb-5 text-center" >
          <thead>
            <tr >
              <th width="100" class="text-center">Name</th>
              <th width="100" class="text-center">Email</th>
              <th width="100" class="text-center">Action</th>
            </tr>
          </thead>
          <tbody>

          @foreach( $clients as $client )
              <tr>
                <td>{{ $client->title }}. {{ $client->name }} {{ $client->last_name }}</td><td>{{ $client->email }}</td>
                <td>
                <a class="btn    " style="color: #ff0033; background-color:rgba(198, 201, 201, 0.229);"  href="{{ route('hotel_clients_delete', ['client_id' => $client->id ]) }}">DELETE</a> 
                <a class="btn    " style="color: #ffbf00; background-color:rgb(198, 201, 201, 0.229);"   href="{{ route('hotel_show_client', ['client_id' => $client->id ]) }}">EDIT/DELETE</a>
                <a class="btn    " style="color: #04ff00; background-color:rgb(198, 201, 201, 0.229);"   href="{{ route('hotel_check_room', ['client_id' => $client->id ]) }}">BOOK A ROOM</a>
                </td>
              </tr>
          @endforeach
          </tbody>
        </table>

        
      </div>
    </div>
    </div>
@endsection
{{-- ----------------------------------------------------------------- --}}
{{-- <form method="post" action="target.html">
  <input type="hidden" name="name" value="value" /> 
  <a onclick="this.parentNode.submit();">click here</a>
</form> --}}