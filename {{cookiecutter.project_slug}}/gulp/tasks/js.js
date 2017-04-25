var gulp = require('gulp'),
    path = require('path'),
    flatmap = require('gulp-flatmap'),
    eslint = require('gulp-eslint'),
    browserify = require('browserify'),
    babelify = require('babelify'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    sourcemaps = require('gulp-sourcemaps'),
    gutil = require('gulp-util'),
    source = require('vinyl-source-stream'),
    buffer = require('vinyl-buffer'),
    transform = require('vinyl-transform'),
    cfg = require('../config.js');

/**
 * JSLint validation
 */
gulp.task('js:lint', function () {
    return gulp.src([cfg.files.glob.js]
            .map(function (obj) {
                return path.join(cfg.paths.src.js, obj)
            }),
        cfg.gulpArgs)
        .pipe(eslint(cfg.eslintOptions))
        .pipe(eslint.format())
        .pipe(eslint.failAfterError());
});

/** JavaScript compilation */
gulp.task('js', function () {
    return gulp.src([cfg.files.glob.js]
            .map(function (obj) {
                return path.join(cfg.paths.src.js, obj)
            }),
        cfg.gulpArgs)
        .pipe(flatmap(function (stream, file) {
            return browserify(file.path, cfg.browserifyOptions)
                .transform(babelify, cfg.babelifyOptions)
                .bundle()
                .pipe(source(file.path))
                .pipe(buffer())
                .pipe(sourcemaps.init({loadMaps: true}))
                .pipe(sourcemaps.write('./'))
                .on('error', gutil.log)
                .pipe(rename({dirname: '.'}))
                .pipe(gulp.dest(cfg.paths.dist.js, cfg.gulpArgs));
        }));
});

gulp.task('js:min', function () {
    process.env.NODE_ENV = 'production';
    return gulp.src([cfg.files.glob.js]
            .map(function (obj) {
                return path.join(cfg.paths.src.js, obj)
            }),
        cfg.gulpArgs)
        .pipe(flatmap(function (stream, file) {
            return browserify(file.path, cfg.browserifyOptions)
                .transform(babelify, cfg.babelifyOptions)
                .bundle()
                .pipe(source(file.path))
                .pipe(buffer())
                .pipe(sourcemaps.init({loadMaps: true}))
                .pipe(uglify())
                .on('error', gutil.log)
                .pipe(sourcemaps.write('./'))
                .pipe(rename({dirname: '.'}))
                .pipe(gulp.dest(cfg.paths.dist.js, cfg.gulpArgs));
        }));
});
