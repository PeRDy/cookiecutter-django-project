var gulp = require('gulp'),
    path = require('path'),
    cfg = require('../config.js');

/**
 * Compiling resources and serving application
 */
gulp.task('default:watch', function () {
    gulp.watch(
        [cfg.files.glob.js]
            .map(function (obj) {
                return path.join(cfg.paths.src.base, obj)
            }),
        ['clean:js', 'js:lint', 'js'],
        cfg.gulpArgs
    );
    gulp.watch(
        [cfg.files.glob.scss]
            .map(function (obj) {
                return path.join(cfg.paths.src.scss, obj)
            }),
        ['clean:styles', 'styles']
    );
});

/**
 * Compiling resources.
 */
gulp.task('default', ['clean', 'bower', 'static:img', 'static:files', 'vendor:fonts', 'vendor:css', 'vendor:js',
    'js:lint', 'styles', 'js']);

/**
 * Compiling resources in a min form.
 */
gulp.task('default:dist', ['clean', 'bower', 'static:img', 'static:files', 'vendor:fonts', 'vendor:css', 'vendor:js',
    'js:lint', 'styles:min', 'js:min']);
