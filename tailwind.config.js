/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
    colors: {
      primary: '#7b5eea',
      secondary: '#73dcfa',
      type_primary: '#fefffd',
      type_secondary: '#8b9abb',
      bg_primary: '#0c192c',
      bg_secondary: '#1a2d44',
      bg_accent: '#2d3752',
      bg_tertiary: '202c4e',
      accent: '#0070f3',
      accent_light: '#0070f3',
      accent_dark: '#0070f3',
    },
    fontFamily: {
      'body': [
        'Inter',
        'ui-sans-serif',
        'system-ui',
        '-apple-system',
        'system-ui',
        'Segoe UI',
        'Roboto',
        'Helvetica Neue',
        'Arial',
        'Noto Sans',
        'sans-serif',
        'Apple Color Emoji',
        'Segoe UI Emoji',
        'Segoe UI Symbol',
        'Noto Color Emoji'
      ],
      'sans': [
        'Inter',
        'ui-sans-serif',
        'system-ui',
        '-apple-system',
        'system-ui',
        'Segoe UI',
        'Roboto',
        'Helvetica Neue',
        'Arial',
        'Noto Sans',
        'sans-serif',
        'Apple Color Emoji',
        'Segoe UI Emoji',
        'Segoe UI Symbol',
        'Noto Color Emoji'
      ],
      'serif': ['Merriweather', 'serif'],
    },
  },
  plugins: [
    require('flowbite/plugin')({
      datatables: true,
    }),
  ],
}

