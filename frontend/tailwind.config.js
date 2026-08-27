/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        rosaCha: '#FFB6C1',
        rosaBebe: '#FFC0CB',
      },
    },
  },
  plugins: [],
}
