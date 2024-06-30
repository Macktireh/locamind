/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./scr/templates/**/*.{html,js,dj}",
    "./scr/static/**/*.{html,js,dj}",
  ],
  theme: {
    extend: {
      fontFamily: {
        poppins: ["Roboto", "sans-serif"],
        oswald: ["Lobster", "sans-serif"],
      },
    },
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ["light", "dark", "night"],
  },
}

