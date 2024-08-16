/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/templates/**/*.{html,js,dj}",
    "./src/static/**/*.{html,js,dj}",
  ],
  theme: {
    extend: {
      fontFamily: {
        roboto: ["Roboto", "sans-serif"],
        lobster: ["Lobster", "sans-serif"],
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

