var gulp = require('gulp'),
    path = require('path'),
    sass = require('gulp-sass'),
    rename = require('gulp-rename'),
    concat = require('gulp-concat'),
    cleanCss= require('gulp-clean-css'),
    source = require('vinyl-source-stream'),
    buffer = require('vinyl-buffer'),
    cfg = require('../config.js');

/**
 * Scss compilation
 */
gulp.task('styles', function () {
    return gulp.src([cfg.files.glob.scss]
            .map(function (obj) {
                return path.join(cfg.paths.src.scss, obj)
            }),
        cfg.gulpArgs)
        .pipe(sass(cfg.sassOptions).on('error', sass.logError))
        .pipe(rename({extname: '.css'}))
        .pipe(gulp.dest(cfg.paths.dist.css, cfg.gulpArgs));
});

gulp.task('styles:min', function () {
    return gulp.src([cfg.files.glob.scss]
            .map(function (obj) {
                return path.join(cfg.paths.src.scss, obj)
            }),
        cfg.gulpArgs)
        .pipe(sass(cfg.sassOptions).on('error', sass.logError))
        .pipe(rename({extname: '.css'}))
        .pipe(cleanCss())
        .pipe(gulp.dest(cfg.paths.dist.css, cfg.gulpArgs));
});