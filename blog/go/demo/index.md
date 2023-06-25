---
title: go demo
date: 2018-03-20 16:34:12
tags:
  - go
---

## web

[./simple_web.go](./simple_web.go)

## cpu_test.go

```go
package temp

import "testing"

func Fib(n int) int {
	switch n {
	case 0:
		return 0
	case 1:
		return 1
	default:
		return Fib(n-1) + Fib(n-2)
	}
}

func BenchmarkFib(b *testing.B) {
	for n := 0; n < b.N; n++ {
		Fib(20)
	}
}
```

## 原型

### prototype 1

```go
package main

import "fmt"

type ISpeaker interface {
	Speak()
	Change(string)
}

type SimpleSpeaker struct {
	Message string
}

func (this *SimpleSpeaker) Speak() {
	fmt.Println("I am", this.Message)
}

func (this *SimpleSpeaker) Change(a string) {
	this.Message = this.Message + " " + a
}

func main() {
	var speaker ISpeaker
	speaker = &SimpleSpeaker{"abc"}
	speaker.Speak()
	speaker.Change("change")
	speaker.Speak()
	fmt.Printf("%T", speaker)
}
```

### prototype 2 继承

```go
package main

import "fmt"

type IReadWriter interface {
	Read(buf *byte, cb int) int
	Write(buf *byte, cb int) int
}

type A struct {
	a int
}

func NewA(params int) *A {
	fmt.Println("NewA:", params)
	return &A{params}
}

func (this *A) Read(buf *byte, cb int) int {
	fmt.Println("A_Read:", this.a)
	return cb
}

func (this *A) Write(buf *byte, cb int) int {
	fmt.Println("A_Write:", this.a)
	return cb
}

type B struct {
	A
}

func NewB(params int) *B {
	fmt.Println("NewB:", params)
	return &B{A{params}}
}

func (this *B) Write(buf *byte, cb int) int {
	fmt.Println("B_Write", this.a)
	return cb
}
func (this *B) Foo() {
	fmt.Println("B_Foo:", this.a)
}

func main() {
	var p IReadWriter = NewB(8)
	p.Read(nil, 10)
	p.Write(nil, 10)
}
```

### cli call linux

```go
package main

import (
	"fmt"
	"os/exec"
)

func main() {
	cmd := exec.Command("ls", "-l")
	stdout, _ := cmd.CombinedOutput()

	o := string(stdout)
	fmt.Printf("%T => %v \n", o, o)
}
```

### https

```go
//openssl genrsa -des3 -out server.key 2048
//openssl rsa -in server.key -out server.key
//openssl req -new -x509 -key server.key -out server.crt -days 3650

//openssl genrsa -des3 -out server.key 2048
//openssl req -new -key server.key -out server.csr
//openssl req -new -x509 -key server.key -out ca.crt -days 3650
//openssl x509 -req -days 3650 -in server.csr   -CA ca.crt -CAkey server.key   -CAcreateserial -out server.crt
package main

import (
    "net/http"
)

func main() {
    h := http.FileServer(http.Dir("."))
    http.ListenAndServeTLS(":443", "server.crt", "server.key", h)
}
```

### 快速排序

```go
// go run sorter.go -i 1.dat -o 2.dat -a bubblesort
package main

import (
	"algorithms/bubblesort"
	"algorithms/qsort"
	"bufio"
	"flag"
	"fmt"
	"io"
	"os"
	"strconv"
	"time"
)

var infile *string = flag.String("i", "infile", "File contains values for sorting")
var outfile *string = flag.String("o", "outfile", "File to receive sorted values")
var algorithm *string = flag.String("a", "qsort", "Sort algorithm")

func main() {
	flag.Parse()
	if infile != nil {
		fmt.Println("infile =", *infile, "outfile =", *outfile, "algorithm =", *algorithm)
	}

	values, err := readValues(*infile)
	if err == nil {
		fmt.Println("Read values:", values)

		t1 := time.Now()

		switch *algorithm {
		case "qsort":
			qsort.QuickSort(values)
		case "bubblesort":
			bubblesort.BubbleSort(values)
		}

		t2 := time.Now()

		fmt.Println("spend", t2.Sub(t1), "to comlpete")
		fmt.Println("End values:", values)
		writeValues(values, "2.dat")
	} else {
		fmt.Println(err)
	}
}

func readValues(infile string) (values []int, err error) {
	file, err := os.Open(infile)
	if err != nil {
		return
	}
	defer file.Close()

	br := bufio.NewReader(file)

	values = make([]int, 0)

	for {
		line, isPerfix, err1 := br.ReadLine()
		if err1 != nil {
			if err1 != io.EOF {
				err = err1
			}
			break
		}
		if isPerfix {
			return
		}
		str := string(line)
		value, err1 := strconv.Atoi(str)
		if err1 != nil {
			err = err1
			return
		}
		values = append(values, value)
	}

	return
}

func writeValues(values []int, outfile string) error {
	file, err := os.Create(outfile)
	if err != nil {
		return err
	}

	defer file.Close()

	for _, value := range values {
		str := strconv.Itoa(value)
		file.WriteString(str + "\n")
	}

	return nil
}
```

### web-staging.go

```
package main

import (
	"fmt"
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
	"os/exec"
	"path"
)

const (
	TEMPLATTE_DIR = "./views"
	// TEMPLATTE_DIR = ""
)

var templates map[string]*template.Template

func init() {
	fileInfoArr, err := ioutil.ReadDir(TEMPLATTE_DIR)
	check(err)

	templates = make(map[string]*template.Template)
	var templateName, templatePath string
	for _, fileInfo := range fileInfoArr {
		templateName = fileInfo.Name()
		if ext := path.Ext(templateName); ext != ".html" {
			continue
		}
		templatePath = TEMPLATTE_DIR + "/" + templateName
		log.Println("Loading template: ", templatePath)
		t := template.Must(template.ParseFiles(templatePath))
		templates[templatePath] = t
	}
	for _, a := range templates {
		log.Printf("%v", a)
	}
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func readerHtml(w http.ResponseWriter, tmpl string, locals map[string]interface{}) {
	tmpl = TEMPLATTE_DIR + "/" + tmpl + ".html"
	err := templates[tmpl].Execute(w, locals)
	check(err)
}

func aHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		readerHtml(w, "index", nil)
	}
	if r.Method == "POST" {
		branch_name := r.FormValue("branch_name")
		staging_id := r.FormValue("staging_id")

		if branch_name == "" {
			fmt.Fprintf(w, "error")
			return
		}

		_dostr := ""
		// _dostr += "cd /Users/a111111/Desktop/www/kreport && "
		_dostr += "cd /data/deployment/echo-web-staging/echo-web && "
		_dostr += "git fetch --prune origin && "
		_dostr += "git checkout " + branch_name + " && "
		_dostr += "git pull && "
		_dostr += "echo 'git status' && "
		_dostr += "git status && "
		_dostr += "../staging_deploy_echo_web.sh " + staging_id + ";"
		cmd, _ := exec.Command("/bin/sh", "-c", _dostr).Output()

		locals := make(map[string]interface{})
		locals["log"] = string(cmd)
		readerHtml(w, "done", locals)
	}
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", aHandler)
	err := http.ListenAndServe(":10080", mux)
	if err != nil {
		log.Fatal("ListenAndServe: ", err.Error())
	}
}
```
