var gulp = require('gulp'),
    path = require('path'),
    cssmin = require('gulp-clean-css'),
    sourcemaps = require('gulp-sourcemaps'),
    uglify = require('gulp-uglify'),
    gutil = require('gulp-util'),
    source = require('vinyl-source-stream'),
    buffer = require('vinyl-buffer'),
    cfg = require('../config.js');


/**
 * Vendor Fonts
 */
gulp.task('vendor:fonts', function () {
    return gulp.src(cfg.paths.src.vendor.fonts
            .map(function (obj) {
                return path.join(cfg.paths.src.vendor.base, obj)
            }),
        cfg.gulpArgs)
        .pipe(gulp.dest(cfg.paths.dist.vendor.fonts, cfg.gulpArgs))
});

/**
 * Vendor JS
 */
gulp.task('vendor:css', function () {
    return gulp.src(cfg.paths.src.vendor.css
            .map(function (obj) {
                return path.join(cfg.paths.src.vendor.base, obj)
            }),
        cfg.gulpArgs)
        .pipe(cssmin())
        .pipe(gulp.dest(cfg.paths.dist.vendor.css, cfg.gulpArgs))
});

/**
 * Vendor CSS
 */
gulp.task('vendor:js', function () {
    return gulp.src(cfg.paths.src.vendor.js
            .map(function (obj) {
                return path.join(cfg.paths.src.vendor.base, obj)
            }),
        cfg.gulpArgs)
        .pipe(buffer())
        .pipe(sourcemaps.init({loadMaps: true}))
        .pipe(uglify())
        .on('error', gutil.log)
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(cfg.paths.dist.vendor.js, cfg.gulpArgs))
});
