/*
	Implement a job scheduler which takes in a function f and an integer n, and
	calls f after n milliseconds.
*/

package main

import (
	"time"
	"fmt"
	"strconv"
)

// Sleep for n milliseconds, then run function f
func job_schedule(f func(), n int64 ) {
	fmt.Println("Running job in ", n, " milliseconds")
	time.Sleep(time.Duration(n) * time.Millisecond)
	f()
}

// Example job to run
func hello() {
	fmt.Println("Hey there hi there!")
}

// Example job to run
func square() {
	var length_string string
	fmt.Println("Enter the square's side length: ")
	fmt.Scanln(&length_string)
	length_int, _ := strconv.ParseInt(length_string, 10, 64)
	fmt.Println("Square area: ", length_int * length_int)
}

func main() {
	var user_input = ""
	var selected_func func()
	var valid_input = false

	for  user_input != "exit" {
		fmt.Println("1: Hello\n2: Square\nexit: quit the program")
		fmt.Println("Please enter your selected operation:")
		fmt.Scanln(&user_input)

		switch user_input {
		case "1":
			selected_func = hello
			valid_input = true
		case "2":
			selected_func = square
			valid_input = true
		case "exit":
			valid_input = true
			break
		default:
			fmt.Println("Input not recognized. Please choose an operation:")
		}

		if user_input == "exit" {
			break
		}

		if valid_input {
			fmt.Println("Enter the number of milliseconds to wait before running the job: ")
			fmt.Scanln(&user_input)
			user_time, _ := strconv.ParseInt(user_input, 10, 64)
			job_schedule(selected_func, user_time)
		}
	}
}