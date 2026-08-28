/**
 * Blitz Taxi — shared design tokens
 * Mirrors the CSS custom properties in css/style.css (:root) on the website,
 * so the rider and driver apps carry the exact same visual identity.
 */

export const colors = {
  bg: '#080B12',
  bg1: '#0E131D',
  bg2: '#141B27',
  bg3: '#1D2635',
  line: 'rgba(255,255,255,0.06)',
  line2: 'rgba(255,255,255,0.13)',
  amber: '#F2B34B',
  amber2: '#F8CE7C',
  amberDim: '#7C6030',
  volt: '#37D2E6',
  volt2: '#7FE6F1',
  text: '#F4F2EC',
  text2: '#AAB2BF',
  text3: '#69717F',
  // inferred from usage on the site (not a defined CSS token, kept for parity)
  success: '#4CAF50',
} as const;

export const radius = {
  base: 12,
} as const;

export const fonts = {
  // Load with expo-font / react-native-vector-icons or a similar loader;
  // fall back to the platform default until the custom fonts are linked.
  heading: 'Sora',       // maps to --sora
  body: 'Inter',         // maps to --body
  mono: 'Space Mono',    // maps to --mono
} as const;

export const theme = { colors, radius, fonts };
export default theme;
