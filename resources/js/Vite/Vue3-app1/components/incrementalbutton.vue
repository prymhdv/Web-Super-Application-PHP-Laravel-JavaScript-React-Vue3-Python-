<script setup>
import { ref } from 'vue';

const counter = ref(0);
</script>

<template>
    <div class="text-center"><h1>I'm here to test!</h1>
    <button type="button" @click="counter++" class="p-2 text-white bg-gray-500 rounded">
        Counter is: {{ counter }}
    </button>
    <div class="container " >
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header text-center">
                        <H1>Supplier Code Selection Component</H1></div>

                    <div class="card-body text-center">
                        <h>I'm an example component.</h>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
  
</template>