import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
    plugins: [
        react(),
        VitePWA({
            registerType: 'autoUpdate',
            includeAssets: ['favicon.svg', 'robots.txt', 'apple-touch-icon.png'],
            manifest: {
                name: 'Raizr - Find Word Roots',
                short_name: 'Raizr',
                description: 'Map the etymological roots of English words.',
                theme_color: '#13072e',
                icons: [
                    {
                        src: 'raizr_192.png',
                        sizes: '192x192',
                        type: 'image/png'
                    },
                    {
                        src: 'raizr_512.png',
                        sizes: '512x512',
                        type: 'image/png'
                    }
                ]
            }
        })
    ]
})
