// resoureces/js/app.js
 
//require('./bootstrap') ;
//import 'resources/css/Reactjs/appMainReactjs.css';

import { createRoot } from 'react-dom/client';
import { createInertiaApp } from '@inertiajs/react';
import { resolvePageComponent } from 'laravel-vite-plugin/inertia-helpers';

const appName = window.document.getElementsByTagName('title')[0]?.innerText || 'Laravel';

createInertiaApp({
    title: (title) => `${title} - ${appName}`,
    resolve: (name) => resolvePageComponent(`./Pages/${name}.jsx`, import.meta.glob('./Pages/**/*.jsx')),
    setup({ el, App, props }) {
        const root = createRoot(el);

        root.render(<App {...props} />);
    },
    progress: {
        color: '#4B5563',
    },
});




  

// import React from 'react';
// import { render } from 'react-dom';

// //import { Router, Route, browserHistory } from 'react-router';

 

// import Example from './components/HelloReact';
// // React Components
// require('./components/HelloReact');
// require('./components/Counter');
 

// render(<HelloReact />, document.getElementById('HelloReact'));