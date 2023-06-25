var map = [
	[1, 1, 1],
	[1, 1, 0],
	[0, 1, 0],
];
var _map = [
	[1, 1, 1, 1, 1],
	[1, 1, 0, 0, 1],
	[0, 1, 1, 0, 1],
	[0, 0, 1, 0, 1],
	[0, 1, 1, 1, 1],
];
var map = [
	[1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
	[0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
	[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
	[0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
	[1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
	[1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
];

var _arrow = [
	[1, 0],
	[0, 1],
	[-1, 0],
	[0, -1],
];

var mx = _map.length - 1;
var my = _map.length - 1;

// 终点
var ex = mx;
var ey = my;
// var ex = 2;
// var ey = 7;

// book
var ed = [];
for (var i = 0; i <= mx; i++) {
	ed[i] = [];
	for (var j = 0; j <= my; j++) {
		ed[i][j] = 0;
	};
};
ed[0][0] = 1;

var _l = [
	[0, 0]
];

function dfs(x, y, _ed, _l) {
	// console.log(_ed[2]);
	// console.log(_map);
	if (x == ex && y == ey) {
		// console.log(_l);
		console.log(_ed);
		// console.log(_l.length);
		return;
	}
	for (var i = 0; i < _arrow.length; i++) {
		// console.log(x, y);
		var nx = x + _arrow[i][0];
		var ny = y + _arrow[i][1];
		if (nx < 0 || ny < 0 || nx > mx || ny > my || !_map[x][y]) {
			continue;
		} else {
			// console.log(nx, ny, mx, my);
			if (!_ed[nx][ny]) {
				// console.log(nx, ny);
				_ed[nx][ny] = 1;
				_l.push([nx, ny]);
				dfs(nx, ny, _ed, _l);
				// console.log(nx, ny);
				_ed[nx][ny] = 0;
				_l.pop();
			}
		}
	};
}

dfs(0, 0, ed, _l);

var Node = function() {
	this.x;
	this.y;
	this.prev;
	this.ed = ed;
}

var _qs = [];
var _q = new Node;
_q.x = 0;
_q.y = 0;
_q.ed = ed;
_qs.push(_q);

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

var print_r = function(arr) {
	var str = '';
	for (var i in arr) {
		for (var j in arr[i]) {
			str += arr[i][j];
		};
		str += '\n';
	};
	console.log(str);
}

var count = 0;
while (_qs.length) {
	// console.log(_qs);
	var _q = _qs.shift();
	var x = _q.x;
	var y = _q.y;

	if (x == ex && y == ey) {
		console.log(_q.ed);
		console.log('end', x, y);
		break;
	}

	for (var i = 0; i < _arrow.length; i++) {
		// console.log(x, y);
		var nx = x + _arrow[i][0];
		var ny = y + _arrow[i][1];
		if (nx < 0 || ny < 0 || nx > mx || ny > my || !_map[nx][ny]) {
			continue;
		} else {
			var _nq = new Node;
			_nq.x = nx;
			_nq.y = ny;
			var ned = []
			_nq.ed = deepcopy(_q.ed);
			// _nq.ed = _q.ed.clone();
			if (!_nq.ed[nx][ny]) {
				_nq.ed[nx][ny] = 1;
				count++;
				// print_r(_q.ed);
				// print_r(_nq.ed);
				_qs.push(_nq);
				// for (var qq in _qs) {
				// 	console.log(_qs[qq]);
				// };
				// console.log();
			}
		}
	};
	if (count > 5) {
		// break;
	}
}