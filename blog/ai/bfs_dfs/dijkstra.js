/*
+  1  2  3  4  5  6
1  0  1 12  /  /  /
2  /  0  9  3  /  /
3  /  /  0  /  5  /
4  /  /  4  0 13 15
5  /  /  /  /  0  4
6  /  /  /  /  /  0
*/

var _map = [
	[],
	[null, 0, 1, 12, 99999, 99999, 99999],
	[null, 99999, 0, 9, 3, 99999, 99999],
	[null, 99999, 99999, 0, 99999, 5, 99999],
	[null, 99999, 99999, 4, 0, 13, 15],
	[null, 99999, 99999, 99999, 99999, 0, 4],
	[null, 99999, 99999, 99999, 99999, 99999, 0],
];

var _distance = [];
var _book = [];

// console.log(_map);

// Floyd-Warshall
/*
for (var n = 1; n <= 6; n++) {
	for (var i = 1; i <= 6; i++) {
		for (var j = 1; j <= 6; j++) {
			if (_map[i][n] + _map[n][j] < _map[i][j]) {
				_map[i][j] = _map[i][n] + _map[n][j];
			}
		}
	}
}
console.log(_map);
*/

for (var i = 1; i <= _map[1].length - 1; i++) {
	_distance[i] = _map[1][i];
	_book[i] = 0;
};
_book[1] = 1;

var _min = 99999;
var _min_point = 0;
for (var i = 1; i <= 6; i++) {
	for (var j = 1; j <= 6; j++) {
		if (_distance[j] < _min && _book[j] == 0) {
			_min = _distance[j];
			_min_point = j;
		}
	}
	_book[_min_point] = 1;
	var _min = 99999;

	for (var k = 1; k <= 6; k++) {
		if (_map[_min_point][k] < 99999) {
			if (_distance[_min_point] + _map[_min_point][k] < _distance[k]) {
				_distance[k] = _distance[_min_point] + _map[_min_point][k];
			}
		}
	};
	console.log(_distance);
}

console.log();
console.log(_distance);