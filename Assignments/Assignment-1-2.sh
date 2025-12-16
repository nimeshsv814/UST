Factorial() {
	n=$1
	F=1
	while [ $n  -gt 1 ]
	do
		F=$((F * n))
		n=$((n - 1))	
	done
	echo "Factorial of $1 : $F"
}

read -p "Enter the number : " num
Factorial "$num"
