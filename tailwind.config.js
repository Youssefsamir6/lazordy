1.
   /** @type {import('tailwindcss').Config} */
   const plugin = require('tailwindcss/plugin');
   const rtl = require('tailwindcss-rtl');
   module.exports = {
     content: [
       './templates/**/*.html',
       './inventory/templates/**/*.html',
       './reports/templates/**/*.html',
       './src/**/*.{js,html,css}',
       './node_modules/flowbite/**/*.js',
     ],
     darkMode: 'class', // Enable dark mode via class
     theme: {
       extend: {
         colors: {
           background: 'rgb(var(--background-rgb))',
           foreground: 'rgb(var(--foreground-rgb))',
           card: 'rgb(var(--card-rgb))',
           primary: {
             DEFAULT: 'rgb(var(--primary-rgb))',
             foreground: 'rgb(var(--primary-foreground-rgb))',
           },
           accent: {
             DEFAULT: 'rgb(var(--accent-rgb))',
           },
           sidebar: {
             background: 'rgb(var(--sidebar-background-rgb))',
             foreground: 'rgb(var(--sidebar-foreground-rgb))',
           },
           muted: 'rgb(var(--muted-rgb))',
           border: 'rgb(var(--border-rgb))',
         },
       },
     },
     plugins: [
       require('flowbite/plugin'),
       plugin(function({ addUtilities }) {
         const newUtilities = {
           '.direction-rtl': {
             direction: 'rtl',
           },
           '.direction-ltr': {
             direction: 'ltr',
           },
           '.text-start': {
             'text-align': 'start',
           },
           '.text-end': {
             'text-align': 'end',
           },
         };
         addUtilities(newUtilities);
       }),
     ],
   };
