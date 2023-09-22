// 邻接表
var _uvw = [
    [4, 5,],
    [1, 4, 9],
    [4, 3, 8],
    [1, 2, 5],
    [2, 4, 6],
    [1, 3, 7],
];

var _frist = [-1, -1, -1, -1, -1];
var _next = [];

for (var i = 1; i <= 5; i++) {
    _next[i] = _frist[_uvw[i][0]];
    _frist[_uvw[i][0]] = i;
}

// console.log(_frist);
// console.log(_next);

for (var i = 1; i <= 4; i++) {
    k = _frist[i];
    console.log(i, k);
    while (k != -1) {
        console.log(_uvw[k]);
        k = _next[k];
    }
}
;