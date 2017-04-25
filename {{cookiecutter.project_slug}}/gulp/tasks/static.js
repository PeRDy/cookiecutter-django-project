var gulp = require('gulp'),
    path = require('path'),
    cfg = require('../config.js');


/**
 * Images
 */
gulp.task('static:img', function () {
    return gulp.src([cfg.files.glob.img]
        .map(function (obj) {
            return path.join(cfg.paths.src.img, obj)
        }), cfg.gulpArgs)
        .pipe(gulp.dest(cfg.paths.dist.img, cfg.gulpArgs))
});

/**
 * Other files
 */
gulp.task('static:files', function () {
    return gulp.src([cfg.files.glob.files]
        .map(function (obj) {
            return path.join(cfg.paths.src.files, obj)
        }), cfg.gulpArgs)
        .pipe(gulp.dest(cfg.paths.dist.base, cfg.gulpArgs))
});
