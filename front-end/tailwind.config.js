/** @type {import('tailwindcss').Config} */

// const withMT = require("@material-tailwind/react/utils/withMT");

// module.exports = withMT({
//   content: ["./src/**/*.{html,js}", "./public/**/*.html", 
//     "./src/**/*.{vue,js,jsx,ts,tsx}"],
//   theme: {
//     extend: {},
//   },
//   plugins: [require("tailgrids/plugin")],
// });


module.exports = {
  content: ["./src/**/*.{html,js}", "./public/**/*.html", 
    "./src/**/*.{vue,js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [require("tailgrids/plugin"),require('daisyui'),],
}

