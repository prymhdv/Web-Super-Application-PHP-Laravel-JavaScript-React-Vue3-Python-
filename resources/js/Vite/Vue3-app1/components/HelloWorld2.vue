<!--
This example demonstrates handling user input with the v-on directive.
-->

<script setup>
import { ref } from 'vue'

const message = ref('Hello World!')

function reverseMessage() {
  // Access/mutate the value of a ref via
  // its .value property.
  message.value = message.value.split('').reverse().join('')
}

function notify() {
  alert('navigation was prevented.')
}
</script>

<template>
  <div class="Helloworld32">

    <div class="col-md-4 text-center "></div>
    <div class="col-md-4 text-center">

      <h1>{{ message }}</h1>


      <button @click="reverseMessage">Reverse Message</button>

      <button @click="message += '!'">Append "!"</button>

      <a href="https://vuejs.org" @click.prevent="notify">
        A link with e.preventDefault()
      </a>
    </div>
    <div class="col-md-4">
    </div>
  </div>
</template>

<style>

.Helloworld32 h1{
  display: inline-block;
  color: rgb(26, 25, 25);
  background-color: #b8b7b7b6;
  border-radius: 12px ;
  margin: 10px;
  padding: 15px;
  font-weight: 500;
  font-size: 16px;
}

.Helloworld32 button {
  display: inline-block;
  margin-bottom: 1em;
  align-content: center;
  color: rgb(26, 25, 25);
  background-color: #b8b7b7b6;
  border-radius: 12px ;
  margin: 10px;
  padding: 9px;
  font-weight: 500;
  font-size: 16px;
}
.Helloworld32 a {
  display: inline-block;
  margin-bottom: 1em;
  align-content: center;
  color: rgb(26, 25, 25);
  background-color: #b8b7b7b6;
  border-radius: 12px ;
  margin: 10px;
  padding: 9px;
  font-weight: 500;
  font-size: 16px;
}
</style>