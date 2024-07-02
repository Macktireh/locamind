/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/templates/**/*.{html,js,dj}",
    "./src/static/**/*.{html,js,dj}",
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

