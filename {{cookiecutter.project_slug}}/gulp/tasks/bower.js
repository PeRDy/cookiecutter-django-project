'use strict';

var gulp = require('gulp'),
    bower = require('gulp-bower'),
    cfg = require('../config.js');

/**
 * Exec a 'bower install' inside a child_process
 */
gulp.task('bower', function (cb) {
    return bower(cfg.bowerPath)
});
