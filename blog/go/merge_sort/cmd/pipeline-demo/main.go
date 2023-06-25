package main

import (
	"bufio"
	"fmt"
	"os"
	"time"

	"../../pipeline"
)

var startTime time.Time

func init() {
	startTime = time.Now()
}

func main() {
	const filename = "small.in"
	const n = 100 * 1000 * 1000

	file, err := os.Create(filename)
	defer file.Close()
	if err != nil {
		panic(err)
	}
	r := pipeline.RandomSource(n)
	writer := bufio.NewWriter(file)
	pipeline.WriteSink(writer, r)
	writer.Flush()

	file, err = os.Open(filename)
	if err != nil {
		panic(err)
	}
	g := pipeline.ReaderSource(bufio.NewReader(file), -1)

	count := 0
	for v := range g {
		fmt.Println(v)
		count++
		if count > 20 {
			break
		}
	}
}

func mergeDemo() {
	p1 := pipeline.ArraySoure(3, 7, 1, 24)
	p2 := pipeline.ArraySoure(9, 42, 5, 6, 0)

	fmt.Println(time.Now().Sub(startTime))

	pp := pipeline.Merge(
		pipeline.InMemSort(p1),
		pipeline.InMemSort(p2),
	)

	fmt.Println(time.Now().Sub(startTime))

	for v := range pp {
		fmt.Print(v, " ")
	}
}
