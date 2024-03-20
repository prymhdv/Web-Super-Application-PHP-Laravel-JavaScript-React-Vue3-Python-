

//import path from 'path';
import { defineConfig } from 'vite';
import { fileURLToPath, URL } from 'url';

import laravel from 'laravel-vite-plugin';
import vue from '@vitejs/plugin-vue';
import react from '@vitejs/plugin-react';


export default defineConfig({
    plugins: [
        laravel({
            input: ['resources/js/app.js','resources/css/app.css'],  
            ssr:   ['resources/js/ssr.js', ], 
            refresh: true,
        }),
        vue({
            template: {
                transformAssetUrls: {
                    base: null,
                    includeAbsolute: false,
                },
               
            },
            
        }),
         
        react(), 
    ],
    // resolve: {
    //     resolve: {
    //         alias: 'hello' :'@hello',
    //      //  { vue : vue/dist/vue.esm-bundler.js,}
    //     //    { vue: 'vue/dist/vue.esm-bundler.js', },
    //     //     vue: '@vue/compat/dist/vue.esm-bundler',
    //     //     vue: 'vue/dist/vue.runtime.esm-bundler',
    //         //{'react' => '/resources/js'},
    //     },
    // },
});

