/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
        animation: {
          pulseColor: 'pulseColor 5s infinite', // Slower for a smoother transition
        },
        keyframes: {
          pulseColor: {
            '0%, 100%': { backgroundColor: 'rgba(244, 114, 182, 0.5)' }, // Pink, 50% opacity
            '25%': { backgroundColor: 'rgba(167, 139, 250, 0.5)' }, // Purple
            '50%': { backgroundColor: 'rgba(251, 191, 36, 0.5)' }, // Yellow
            '75%': { backgroundColor: 'rgba(96, 165, 250, 0.5)' }, // Blue
          },
          
        },
        backgroundImage: {
          'custom-gradient': 'linear-gradient(180deg, rgba(19,19,20,1) 0%, rgba(40,42,44,1) 100%)',
        },

        colors: {
          leafGreen: {
            DEFAULT: '#309900',
            dark: '#005600',
            mid: '#5e9900',
            light: '#990',
          },
        },
        keyframes: {
          falling: {
            '0%': { transform: 'translate3d(300px, 0, 0) rotate(0deg)' },
            '100%': { transform: 'translate3d(-350px, 700px, 0) rotate(90deg)', opacity: '0' },
          },
          falling2: {
            '0%': { transform: 'translate3d(0, 0, 0) rotate(90deg)' },
            '100%': { transform: 'translate3d(-400px, 680px, 0) rotate(0deg)', opacity: '0' },
          },
          falling3: {
            '0%': { transform: 'translate3d(0, 0, 0) rotate(-20deg)' },
            '100%': { transform: 'translate3d(-230px, 640px, 0) rotate(-70deg)', opacity: '0' },
          },
          // Mirrored animations
          fallingLeft: {
            '0%': { transform: 'translate3d(-300px, 0, 0) rotate(0deg)' },
            '100%': { transform: 'translate3d(350px, 700px, 0) rotate(-90deg)', opacity: '0' },
          },
          falling2Left: {
            '0%': { transform: 'translate3d(0, 0, 0) rotate(-90deg)' },
            '100%': { transform: 'translate3d(400px, 680px, 0) rotate(0deg)', opacity: '0' },
          },
          falling3Left: {
            '0%': { transform: 'translate3d(0, 0, 0) rotate(20deg)' },
            '100%': { transform: 'translate3d(230px, 640px, 0) rotate(70deg)', opacity: '0' },
          },
        },
        animation: {
          falling: 'falling 5s infinite ease-in-out',
          falling2: 'falling2 5s infinite ease-in-out',
          falling3: 'falling3 5s infinite ease-in-out',
          fallingLeft: 'fallingLeft 5s infinite ease-in-out',
          falling2Left: 'falling2Left 5s infinite ease-in-out',
          falling3Left: 'falling3Left 5s infinite ease-in-out',
        },
    },
  },
  plugins: [require('daisyui'),],
}

