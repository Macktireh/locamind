/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./bienlocation/templates/**/*.{html,js,dj}",
    "./bienlocation/static/**/*.{html,js,dj}",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ["light", "dark", "night"],
  },
}

