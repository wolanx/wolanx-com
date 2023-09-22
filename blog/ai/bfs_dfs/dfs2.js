var _map = [
	[],
	[null, 0, 2, -1, -1, 10], // 1
	[null, -1, 0, 3, -1, 7], // 2
	[null, 4, -1, 0, 4, -1], // 3 
	[null, -1, -1, -1, 0, 5], // 4
	[null, -1, -1, 3, -1, 0], // 5
];

var _start = 1;
var _end = 5;

var _path = [];

var _count = 0;

function deepcopy(obj) {
	var out = [],
		i = 0,
		len = obj.length;
	for (; i < len; i++) {
		if (obj[i] instanceof Array) {
			out[i] = deepcopy(obj[i]);
		} else out[i] = obj[i];
	}
	return out;
}

function dfs(_start, _path) {
	// if (_count > 100) {
	// 	return;
	// }
	if (_start == _end) {
		console.log('PATH', _path);
		return;
	}
	var _can = _map[_start];
	for (var i in _can) {
		if (_can[i] > 0) {
			var _next = _can[i];
			if (_path.indexOf(_next) < 0) {
				console.log(i, _next);
				var _npath = deepcopy(_path);
				_npath.push(_next);
				_count++;
				dfs(i, _npath);
			}
		} else {
			continue;
		}
	};
}

dfs(_start, _path);