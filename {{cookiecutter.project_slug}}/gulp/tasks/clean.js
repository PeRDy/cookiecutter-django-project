var gulp = require('gulp'),
    del = require('del'),
    cfg = require('../config');

/**
 * Cleaning dist directories
 */
gulp.task('clean:img', function () {
    del.sync([cfg.paths.dist.img + '/**'], cfg.gulpArgs);
})

gulp.task('clean:styles', function () {
    del.sync([cfg.paths.dist.css + '/**'], cfg.gulpArgs);
})

gulp.task('clean:js', function () {
    del.sync([cfg.paths.dist.js + '/**'], cfg.gulpArgs);
})

gulp.task('clean:fonts', function () {
    del.sync([cfg.paths.dist.fonts + '/**'], cfg.gulpArgs);
})

gulp.task('clean:vendor', function () {
    del.sync([cfg.paths.src.vendor + '/**'], cfg.gulpArgs);
})

gulp.task('clean', ['clean:img', 'clean:styles', 'clean:js', 'clean:fonts', 'clean:vendor']);
