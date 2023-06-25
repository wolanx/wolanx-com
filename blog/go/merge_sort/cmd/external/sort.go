package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"

	"../../pipeline"
)

func main() {
	//p := createPipeline("small.in", 800*1000*1000, 4)
	p := createNetworkPipeline("small.in", 800*1000*1000, 4)
	writeToFile(p, "small.out")
	printFile("small.out")
}

func createPipeline(filename string, fileSize, chunkCount int) <-chan int {
	chunkSize := fileSize / chunkCount

	pipeline.Init()

	sortResults := []<-chan int{}
	for i := 0; i < chunkCount; i++ {
		file, err := os.Open(filename)
		if err != nil {
			panic(err)
		}
		file.Seek(int64(i*chunkSize), 0)

		source := pipeline.ReaderSource(bufio.NewReader(file), chunkSize)
		sortResults = append(sortResults, pipeline.InMemSort(source))
	}

	return pipeline.MergeN(sortResults...)
}

func writeToFile(p <-chan int, fileName string) {
	file, err := os.Create(fileName)
	defer file.Close()
	if err != nil {
		panic(err)
	}
	writer := bufio.NewWriter(file)
	defer writer.Flush()

	pipeline.WriteSink(writer, p)
}

func printFile(fielName string) {
	file, err := os.Open(fielName)
	defer file.Close()
	if err != nil {
		panic(err)
	}
	p := pipeline.ReaderSource(file, -1)

	count := 0
	for v := range p {
		fmt.Println(v)
		count++
		if count > 100 {
			break
		}
	}
}

func createNetworkPipeline(filename string, fileSize, chunkCount int) <-chan int {
	chunkSize := fileSize / chunkCount

	pipeline.Init()

	sortAddr := []string{}
	for i := 0; i < chunkCount; i++ {
		file, err := os.Open(filename)
		if err != nil {
			panic(err)
		}
		file.Seek(int64(i*chunkSize), 0)

		source := pipeline.ReaderSource(bufio.NewReader(file), chunkSize)

		addr := ":" + strconv.Itoa(7000+i)
		pipeline.NetworkSink(addr, pipeline.InMemSort(source))
		sortAddr = append(sortAddr, addr)
	}

	sortResults := []<-chan int{}
	for _, addr := range sortAddr {
		sortResults = append(sortResults, pipeline.NetworkSource(addr))
	}

	return pipeline.MergeN(sortResults...)
}
