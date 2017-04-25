var path = require('path');
var pathSrcBase = path.normalize("./client/src");
var pathDistBase = path.normalize("./client/dist");
var pathSrcVendorBase = path.join(pathSrcBase, "vendor");
var pathDistVendorBase = path.join(pathDistBase, "vendor");

cfg = {
    files: {
        glob: {
            js: "/**/*.js",
            scss: "/**/*.scss",
            apps: "*.js",
            styles: "*.scss",
            img: "/**/*",
            files: "/**/*"
        },
        dist: {
            style: "style.css"
        }
    },
    paths: {
        src: {
            base: pathSrcBase,
            fonts: path.join(pathSrcBase, "fonts"),
            scss: path.join(pathSrcBase, "scss"),
            js: path.join(pathSrcBase, "js"),
            img: path.join(pathSrcBase, "img"),
            files: path.join(pathSrcBase, "static"),
            vendor: {
                base: pathSrcVendorBase,
                fonts: [
                    // List of Fonts files to be included
                    "font-awesome-sass/assets/fonts/**/*"
                ],
                css: [
                    // List of CSS files to be included
                ],
                js: [
                    // List of JS files to be included
                ]
            }
        },
        dist: {
            base: pathDistBase,
            fonts: path.join(pathDistBase, "fonts"),
            css: path.join(pathDistBase, "css"),
            js: path.join(pathDistBase, "js"),
            img: path.join(pathDistBase, "img"),
            vendor: {
                base: pathDistVendorBase,
                fonts: path.join(pathDistBase, "fonts"),
                css: path.join(pathDistVendorBase, "css"),
                js: path.join(pathDistVendorBase, "js")
            }
        }
    },
    gulpArgs: {
        cwd: process.cwd()
    },
    browserifyOptions: {
        paths: [
            path.join(pathSrcBase, 'js/')
        ]
    },
    babelifyOptions: {
        presets: [
            'es2015'
        ]
    },
    sassOptions: {
        errLogToConsole: true,
        outputStyle: 'expanded',
        includePaths: [pathSrcVendorBase]
    },
    eslintOptions: {
        baseConfig: {
            parserOptions: {
                "ecmaVersion": 6,
                "sourceType": "module",
                "ecmaFeatures": {
                    "jsx": true
                }
            }
        }
    },
    bowerPath: pathSrcVendorBase
}

module.exports = cfg