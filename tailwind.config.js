/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        arapawa: {
          800: "#2A4E62",
          700: "#557181",
        },
      },

      FontFamily: {
        h1: ["Workbench"],
      },
    },
  },
  plugins: [],
};
