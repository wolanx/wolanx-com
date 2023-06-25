---
title: js 小片段
date: 2018-03-22 16:38:57
tags:
  - js
---

### download data

```javascript
download('aaa', '1.txt', 'text/plain');

function download(text, name, type) {
    var file = new Blob([text], {
        type: type
    })
    var a = $('<a id="download-it">Download it</a>').appendTo('body')
    a[0].href = URL.createObjectURL(file)
    a[0].download = name
    a[0].click()
}
```

### 是否当前窗口

```javascript
var vis = (function () {
    var stateKey, eventKey, keys = {
        hidden: "visibilitychange",
        webkitHidden: "webkitvisibilitychange",
        mozHidden: "mozvisibilitychange",
        msHidden: "msvisibilitychange"
    };
    for (stateKey in keys) {
        if (stateKey in document) {
            eventKey = keys[stateKey];
            break;
        }
    }
    return function (c) {
        if (c) document.addEventListener(eventKey, c);
        return !document[stateKey];
    }
})();
```