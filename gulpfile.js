var gulp = require('gulp'),  
	// pug = require('gulp-pug'),	
	// browserSync = require('browser-sync'),
	concat = require('gulp-concat');
	// reload = browserSync.reload;

// run this task by typing in gulp pug in CLI
gulp.task('build', function() {  
  gulp.src('static/src/css/**/*.css') 
  	.pipe(gulp.dest('static/build/css'));
  gulp.src('static/src/js/**/*.js') 
    .pipe(gulp.dest('static/build/js'));
  gulp.src(['static/src/scripts/**/*'])
    .pipe(gulp.dest('static/build/scripts')); 
  gulp.src(['static/src/fonts/**/*'])
    .pipe(gulp.dest('static/build/fonts'));  
  gulp.src(['static/src/img/**/*'])
    .pipe(gulp.dest('static/build/img'));    
});


gulp.task('default', ['build'], function () {
    gulp.watch('static/src/**/*.*', ['build']);
});