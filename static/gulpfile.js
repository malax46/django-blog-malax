// Require gulp and plugins
var gulp    = require('gulp'),
    //connect = require('gulp-connect'),
    filelog = require('gulp-filelog'),
    //jade    = require('gulp-jade'),
    plumber = require('gulp-plumber'),
    sass    = require('gulp-sass');

/* Web Server
gulp.task('server', function() {
  connect.server({
    root: './dist/',
    port: 8080,
    livereload: true
  });
});


// Browser livereload
gulp.task('html', function () {
    gulp.src('./dist/')
    .pipe(connect.reload());
});

// Browser livereload
gulp.task('css', function () {
    gulp.src('./dist/css/')
    .pipe(connect.reload());
});
*/

// Task to compile Sass files
gulp.task('sass', function() {  
    gulp.src('scss/*.scss')
   .pipe(plumber())
   .pipe(sass())
   .pipe(gulp.dest('css/'))
   .pipe(filelog()); 
});

/* Task to compile Jade files
gulp.task('jade', function() {  
    gulp.src('./dev/templates/*.jade')
   .pipe(plumber())
   .pipe(jade({
        pretty: true
   }))
   .pipe(gulp.dest('./dev/templates/'))
   .pipe(filelog())
   .pipe(gulp.dest('./dist/'))
   .pipe(filelog());
});
*/

// Gulp watch
gulp.task('watch', function() {
    gulp.watch('scss/**', ['sass']);
    //gulp.watch('templates/**', ['jade']);
    //gulp.watch('dist/*.html', ['html']);
    //gulp.watch('dist/css/*.css', ['css']);
});

// Gulp Default
gulp.task('default', ['watch']);


