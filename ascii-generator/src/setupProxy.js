const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
    app.use(
        '/generate-ascii',
        createProxyMiddleware({
            target: 'http://localhost:5000',  // Change to match your Flask server URL
            changeOrigin: true,
        })
    );
};
