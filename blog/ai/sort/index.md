---
title: 排序算法js
date: 2018-03-19 18:27:55
tags: [ 算法 ]
---

# doc

- [x] JS家的排序算法 [http://www.jianshu.com/p/1b4068ccd505](http://www.jianshu.com/p/1b4068ccd505)

## pic

![sort.png](sort.png)

## 名词解释

```
n: 数据规模
k:“桶”的个数
In-place: 占用常数内存，不占用额外内存
Out-place: 占用额外内存
稳定性：排序后2个相等键值的顺序和排序之前它们的顺序相同
```

# 10

```
var a = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
```

## 冒泡排序（Bubble Sort）

```
function bubbleSort(arr) {
	var len = arr.length;
	for (var i = 0; i < len; i++) {
		for (var j = 0; j < len - 1 - i; j++) {
			if (arr[j] > arr[j + 1]) { //相邻元素两两对比
				var temp = arr[j + 1]; //元素交换
				arr[j + 1] = arr[j];
				arr[j] = temp;
			}
		}
	}
	return arr;
}
```

## 选择排序（Selection Sort）

```
function selectionSort(arr) {
	var len = arr.length;
	var minIndex, temp;
	for (var i = 0; i < len - 1; i++) {
		minIndex = i;
		for (var j = i + 1; j < len; j++) {
			if (arr[j] < arr[minIndex]) { //寻找最小的数
				minIndex = j; //将最小数的索引保存
			}
		}
		temp = arr[i];
		arr[i] = arr[minIndex];
		arr[minIndex] = temp;
	}
	return arr;
}
```

## 插入排序（Insertion Sort）

```
function insertionSort(arr) {
	var len = arr.length;
	var preIndex, current;
	for (var i = 1; i < len; i++) {
		preIndex = i - 1;
		current = arr[i];
		while (preIndex >= 0 && arr[preIndex] > current) {
			arr[preIndex + 1] = arr[preIndex];
			preIndex--;
		}
		arr[preIndex + 1] = current;
	}
	return arr;
}
```

## 希尔排序（Shell Sort）

```
function shellSort(arr) {
	var len = arr.length,
		temp,
		gap = 1;
	while (gap < len / 3) { //动态定义间隔序列
		gap = gap * 3 + 1;
	}
	for (gap; gap > 0; gap = Math.floor(gap / 3)) {
		for (var i = gap; i < len; i++) {
			temp = arr[i];
			for (var j = i - gap; j >= 0 && arr[j] > temp; j -= gap) {
				arr[j + gap] = arr[j];
			}
			arr[j + gap] = temp;
		}
	}
	return arr;
}
```

## 归并排序（Merge Sort）

```
function mergeSort(arr) { //采用自上而下的递归方法
	var len = arr.length;
	if (len < 2) {
		return arr;
	}
	var middle = Math.floor(len / 2),
		left = arr.slice(0, middle),
		right = arr.slice(middle);
	return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
	var result = [];

	while (left.length && right.length) {
		if (left[0] <= right[0]) {
			result.push(left.shift());
		} else {
			result.push(right.shift());
		}
	}

	while (left.length)
		result.push(left.shift());

	while (right.length)
		result.push(right.shift());

	return result;
}
```

## 快速排序（Quick Sort）

```
function quickSort(arr, left, right) {
	var len = arr.length,
		partitionIndex,
		left = typeof left != 'number' ? 0 : left,
		right = typeof right != 'number' ? len - 1 : right;

	if (left < right) {
		partitionIndex = partition(arr, left, right);
		quickSort(arr, left, partitionIndex - 1);
		quickSort(arr, partitionIndex + 1, right);
	}
	return arr;
}

function partition(arr, left, right) { //分区操作
	var pivot = left, //设定基准值（pivot）
		index = pivot + 1;
	for (var i = index; i <= right; i++) {
		if (arr[i] < arr[pivot]) {
			swap(arr, i, index);
			index++;
		}
	}
	swap(arr, pivot, index - 1);
	return index - 1;
}

function swap(arr, i, j) {
	var temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}
```

## 堆排序（Heap Sort）

```
var len; //因为声明的多个函数都需要数据长度，所以把len设置成为全局变量

function buildMaxHeap(arr) { //建立大顶堆
	len = arr.length;
	for (var i = Math.floor(len / 2); i >= 0; i--) {
		heapify(arr, i);
	}
}

function heapify(arr, i) { //堆调整
	var left = 2 * i + 1,
		right = 2 * i + 2,
		largest = i;

	if (left < len && arr[left] > arr[largest]) {
		largest = left;
	}

	if (right < len && arr[right] > arr[largest]) {
		largest = right;
	}

	if (largest != i) {
		swap(arr, i, largest);
		heapify(arr, largest);
	}
}

function swap(arr, i, j) {
	var temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

function heapSort(arr) {
	buildMaxHeap(arr);

	for (var i = arr.length - 1; i > 0; i--) {
		swap(arr, 0, i);
		len--;
		heapify(arr, 0);
	}
	return arr;
}
```

## 计数排序（Counting Sort）

```
function countingSort(arr, maxValue) {
	var bucket = new Array(maxValue + 1),
		sortedIndex = 0;
	arrLen = arr.length,
		bucketLen = maxValue + 1;

	for (var i = 0; i < arrLen; i++) {
		if (!bucket[arr[i]]) {
			bucket[arr[i]] = 0;
		}
		bucket[arr[i]]++;
	}

	for (var j = 0; j < bucketLen; j++) {
		while (bucket[j] > 0) {
			arr[sortedIndex++] = j;
			bucket[j]--;
		}
	}

	return arr;
}
```

## 桶排序（Bucket Sort）

```
function bucketSort(arr, bucketSize) {
	if (arr.length === 0) {
		return arr;
	}

	var i;
	var minValue = arr[0];
	var maxValue = arr[0];
	for (i = 1; i < arr.length; i++) {
		if (arr[i] < minValue) {
			minValue = arr[i]; //输入数据的最小值
		} else if (arr[i] > maxValue) {
			maxValue = arr[i]; //输入数据的最大值
		}
	}

	//桶的初始化
	var DEFAULT_BUCKET_SIZE = 5; //设置桶的默认数量为5
	bucketSize = bucketSize || DEFAULT_BUCKET_SIZE;
	var bucketCount = Math.floor((maxValue - minValue) / bucketSize) + 1;
	var buckets = new Array(bucketCount);
	for (i = 0; i < buckets.length; i++) {
		buckets[i] = [];
	}

	//利用映射函数将数据分配到各个桶中
	for (i = 0; i < arr.length; i++) {
		buckets[Math.floor((arr[i] - minValue) / bucketSize)].push(arr[i]);
	}

	arr.length = 0;
	for (i = 0; i < buckets.length; i++) {
		insertionSort(buckets[i]); //对每个桶进行排序，这里使用了插入排序
		for (var j = 0; j < buckets[i].length; j++) {
			arr.push(buckets[i][j]);
		}
	}

	return arr;
}
```

## 基数排序（Radix Sort）

```
var counter = [];

function radixSort(arr, maxDigit) {
	var mod = 10;
	var dev = 1;
	for (var i = 0; i < maxDigit; i++, dev *= 10, mod *= 10) {
		for (var j = 0; j < arr.length; j++) {
			var bucket = parseInt((arr[j] % mod) / dev);
			if (counter[bucket] == null) {
				counter[bucket] = [];
			}
			counter[bucket].push(arr[j]);
		}
		var pos = 0;
		for (var j = 0; j < counter.length; j++) {
			var value = null;
			if (counter[j] != null) {
				while ((value = counter[j].shift()) != null) {
					arr[pos++] = value;
				}
			}
		}
	}
	return arr;
}
```
