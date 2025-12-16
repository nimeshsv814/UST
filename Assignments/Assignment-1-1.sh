Number_Positive_Negative_Zero() {
	if [ $1 -gt 0 ]; then
		echo "$1 is Positive Number"
	elif [ $1 -lt 0 ]; then
		echo "$1 is Negative Number"
	else
		echo "$1 is Zero"
	fi
}

read -p "Enter the number to check whether Positive or Negative or Zero : " num

Number_Positive_Negative_Zero "$num"
