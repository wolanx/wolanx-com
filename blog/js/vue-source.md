---
title: vue 源码解读
date: 2017-11-27 16:38:57
tags:
  - js
---

```js title="gulpfile.js"
var gulp = require('gulp')
var watch = require('gulp-watch');
var component = require('gulp-component');

gulp.task('default', function () {
    // 观察 *.js 并配置 component.json scripts
    return watch(['component.json', 'src/**/*.js'], function (v) {
        console.log(v.path);
        gulp.src('component.json')
            .pipe(component.scripts({
                standalone: true,
            }))
            .pipe(gulp.dest('./dist'));
    })
});
```

```json title="component.json"
{
  "name": "Zhaoyujie",
  "version": "0.10.5",
  "main": "src/test.js",
  "author": "Evan You <yyx990803@gmail.com>",
  "description": "Simple, Fast & Composable MVVM for building interative interfaces",
  "keywords": [
    "mvvm",
    "framework",
    "data binding"
  ],
  "license": "MIT",
  "scripts": [
    "src/main.js",
    "src/emitter.js",
    "src/config.js",
    "src/utils.js",
    "src/fragment.js",
    "src/compiler.js",
    "src/viewmodel.js",
    "src/binding.js",
    "src/observer.js",
    "src/directive.js",
    "src/exp-parser.js",
    "src/text-parser.js",
    "src/deps-parser.js",
    "src/filters.js",
    "src/transition.js",
    "src/batcher.js",
    "src/directives/index.js",
    "src/directives/if.js",
    "src/directives/repeat.js",
    "src/directives/on.js",
    "src/directives/model.js",
    "src/directives/with.js",
    "src/directives/html.js",
    "src/directives/style.js",
    "src/directives/partial.js",
    "src/directives/view.js",
    "src/test.js",
    "src/a.js",
    "src/b.js"
  ]
}
```