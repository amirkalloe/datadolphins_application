import { createApp } from 'vue'
import { createVuetify, ThemeDefinition } from 'vuetify'

const default_theme = {
  primary: "#1976D2",
  secondary: "#1976D2",
  accent: "#82B1FF",
  error: "#FF5252",
  info: "#2196F3",
  success: "#4CAF50",
  warning: "#FFC107",
  headerTextColour: "#FFFFFF",
  headerHoverColour: "#328de6",
}

export default createVuetify({
  theme: {
    defaultTheme: 'default_theme',
    themes: {
      default_theme,
    },
  },
})
