/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", //teplate at the project label
    "./**/templates/**/*.html" //template inside apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

