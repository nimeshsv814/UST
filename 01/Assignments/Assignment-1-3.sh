#!/bin/bash
Sum_Of_N_Numbers() {
	sum=0
	for (( i=1; i<=$1; i++))
	do
		sum=$((sum+i))
	done
	echo "Sum of N numbers is $sum"
}

read -p "Enter the N = " num
Sum_Of_N_Numbers "$num"
