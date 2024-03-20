<template>
     <div class="col-md-4">  </div>
     <div class="col-md-4">
        <img alt="Vue logo" src="img\Logo\logo.png" />  
        <h1 class="text-center">I'm here to test !</h1>
        <button @click.prevent="tiggerEndpoint" class="hollow">Trigger Endpoint</button>
    </div> 
    <div class="col-md-4"> </div>
 
</template>

<script>
export default {
    name: 'HelloVue'
}
</script>