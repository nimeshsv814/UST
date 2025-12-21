Reverse_Number() {
	n=$1
	result=0
	while [ "$n" -ne 0 ]
	do
		result=$((result*10))
		t=$((n%10))
		n=$((n/10))
		result=$((result+t))
	done
	echo "Reversed number is $result"
}

read -p "Enter the number to be reversed : " num
Reverse_Number "$num"

