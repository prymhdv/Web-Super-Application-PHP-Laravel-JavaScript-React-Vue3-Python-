import { defineConfig } from "vite";
import { fileURLToPath, URL } from "url";
import laravel from "laravel-vite-plugin";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
    plugins: [
        laravel({
            input: "resources/js/Vuejs/appMainVuejs.js",
            ssr:   "resources/js/Vuejs/ssr.js",
            refresh: true,
        }),
        //laravel(['resources/js/app.js']),
        vue({
            template: {
                transformAssetUrls: {
                    base: null,
                    includeAbsolute: false,
                },
            },
        }),
        vue({
            template: {
                transformAssetUrls: {
                    // The Vue plugin will re-write asset URLs, when referenced
                    // in Single File Components, to point to the Laravel web
                    // server. Setting this to `null` allows the Laravel plugin
                    // to instead re-write asset URLs to point to the Vite
                    // server instead.
                    base: null,
 
                    // The Vue plugin will parse absolute URLs and treat them
                    // as absolute paths to files on disk. Setting this to
                    // `false` will leave absolute URLs un-touched so they can
                    // reference assets in the public directory as expected.
                    includeAbsolute: false,
                },
            },
        }),
    ],
    ssr: {
        noExternal: ["vue", "@protonemedia/laravel-splade"]
    },
    resolve: {
        alias: [
            { '@': '/resources/ts',}
        //   { '@/': `${path.resolve(__dirname, 'src')}/` },
        //   { find: '@', replacement: fileURLToPath(new URL('./src', import.meta.url)) },
        //   { find: '@assets', replacement: fileURLToPath(new URL('./src/shared/assets', import.meta.url)) },
        //   { find: '@cmp', replacement: fileURLToPath(new URL('./src/shared/cmp', import.meta.url)) },
        //   { find: '@stores', replacement: fileURLToPath(new URL('./src/shared/stores', import.meta.url)) },
        //   { find: '@use', replacement: fileURLToPath(new URL('./src/shared/use', import.meta.url)) },
        ],
      },
});