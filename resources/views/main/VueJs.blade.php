@extends('layouts.master')
@section('content')

<script>
console.log("-------------------Scraping links on current page  (VueJs.blade) --------------------------" ,   "<IncrementCounter><IncrementCounter/>");
</script>

    <div id="appViteVue3A" class="text-center">
        <p style="font-size: 18px; margin:20px; font-family : sanserif; font-weight: 900; text-wrap: pretty;  direction: ltr; text-align-last: center;"> 
        The Starting Vue3 <br/>
         Main errors sensitive for tag names like Header,IncrementCounter,...<br/> but run from app.js imported other apps..  </p>
         <!-- <app_eader><app_eader/> make just one element mean last but other s is more instanced-->
         
         <app_dear2></app_dear2>
         <app_INC></app_INC>
         <app_INC></app_INC>
         <app_dear></app_dear>
    </div>

    <div id="appViteVue4" class="text-center">
     <VueSchool><VueSchool/>
     <TestComponent><TestComponent/>
    </div>
@endsection