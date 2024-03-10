@extends('layouts.master')
@section('content')


<div id="VueJs">

    <h4 class="text-center">-------------------Hello VueJs------------------</h4>
    <h1>{{ message }}</h1>
    <script src="{{ asset('js/vue.js') }}"></script>
    <script>
        new Vue({
            el: '#VueJs',
            data: {
                message: 'Hello' + ' Vue.js'
            }
        })
    </script>
    <h4 class="text-center">-------------------Hello VueJs------------------</h4>

</div>




@endsection