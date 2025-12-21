#!/bin/bash
Prime_Check() {
	flag=0
	for (( i=2; i<=$1; i++ ))
	do
		if (( $1 % i == 0 )); then
			flag=$((flag+1))
		fi
	done
	if (( flag==1 )); then
		echo "$1 is Prime Number"
	else
		echo "$1 is not Prime Number"
	fi
}

read -p "Enter the number for Prime Check : " num
Prime_Check "$num"
