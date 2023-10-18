

const { src, dest, watch, series } = require("gulp")
const sass = require("gulp-sass")(require("sass"))
const purgecss = require("gulp-purgecss")

function buildStyles() {
  return src("sass/**/*.scss")
    .pipe(sass())
    .pipe(purgecss({content: ["recipe_search/templates/recipe_search/*.html"]}))
    .pipe(dest("css"))
}

function watchTask() {
  watch(["sass/**/*.scss", "recipe_search/templates/recipe_search/*.html"], buildStyles)
}

exports.default = series(buildStyles, watchTask)