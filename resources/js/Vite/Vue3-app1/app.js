import '../../bootstrap';
//--------------------------------------------------------------------
//window.vue = require('vue');
import { createApp } from 'vue/dist/vue.esm-bundler.js';
 
import PolyGrapher     from  './components/PolyGrapher.vue';
import IncrementCounter from './components/incrementalbutton.vue';
import HelloWorld2 from      './components/HelloWorld2.vue';
//--------------------------------------------------------------------
const app = createApp({});
// app.component('test-component-tag', TestComponent);
// app.component('test-component-tag2', VueSchool);
//--------------------------------------------------------------------
 
//--------------------------------------------------------------------
 
//import {Vue} from 'vue'
import * as Vue from 'vue';
import TestComponent from './components/TestComponent.vue'
import VueSchool from './components/VueSchool.vue'

// new Vue({
//     el: '#app',
//     render: (element => element(TestComponent)),//this will render only navigation component. How to render pageoptions too in this call?
//     components: {TestComponent,VueSchool}
// })
//--------------------------------------------------------------------
 
//--------------------------------------------------------------------
app.component('app_dear2', HelloWorld2);
app.component('app_INC', IncrementCounter);
app.component('app_dear', PolyGrapher);
app.mount('#appViteVue3A');
//-----------------------------------------------------------------------
//-----------------------------------------------------------------------