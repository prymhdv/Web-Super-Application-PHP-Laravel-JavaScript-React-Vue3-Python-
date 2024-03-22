const mix = require('laravel-mix');

/*npm install laravel-mix --save-dev   -------    npx mix
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */

mix
    /* CSS */
    .sass('resources/DashboardOneUI/sass/main.scss', 'public/DashboardOneUI/css/oneui.css')
    .sass('resources/DashboardOneUI/sass/oneui/themes/amethyst.scss', 'public/DashboardOneUI/css/themes/')
    .sass('resources/DashboardOneUI/sass/oneui/themes/city.scss', 'public/DashboardOneUI/css/themes/')
    .sass('resources/DashboardOneUI/sass/oneui/themes/flat.scss', 'public/DashboardOneUI/css/themes/')
    .sass('resources/DashboardOneUI/sass/oneui/themes/modern.scss', 'public/DashboardOneUI/css/themes/')
    .sass('resources/DashboardOneUI/sass/oneui/themes/smooth.scss', 'public/DashboardOneUI/css/themes/')

    /* JS */
    .js('resources/DashboardOneUI/js/app.js', 'public/DashboardOneUI/js/laravel.app.js')
    .js('resources/DashboardOneUI/js/oneui/app.js', 'public/DashboardOneUI/js/oneui.app.js')

    /* Page JS */
    .js('resources/DashboardOneUI/js/pages/tables_datatables.js', 'public/DashboardOneUI/js/pages/tables_datatables.js')

    /* Tools */
    .browserSync('localhost:8000')
    .disableNotifications()

    /* Options */
    .options({
        processCssUrls: false
    });
