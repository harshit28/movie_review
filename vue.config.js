module.exports = {
    chainWebpack: config => {
        config.module.rules.delete('eslint');
    },
    outputDir: 'dist',
    assetsDir: 'static',

    devServer: {
        proxy: {
          '/api*': {
            // Forward frontend dev server request for /api to flask dev server
            target: 'http://localhost:5000/'
          }
        }
      }
}