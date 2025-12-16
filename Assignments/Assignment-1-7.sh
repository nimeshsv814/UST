#!/bin/bash
add() {
	echo "Result : $(( $1 + $2 ))"
}
sub() {
	echo "Result : $(( $1 - $2 ))"
}
mul() {
	echo "Result : $(( $1 * $2 ))"
}
div() {
	if [ "$2" -eq 0 ]; then
		echo "Error:Can't divide by Zero"
	else
		echo "Result : $(( $1 / $2 ))"
	fi
}
while true
do
	echo "----------Calculator----------"
	echo "1) Add"
	echo "2) Subtract"
	echo "3) Multiply"
	echo "4) Divide"
	echo "5) Exit"
	read -p "Enter the option : " option

	case "$option" in
		1|2|3|4)
			read -p "Enter first number : " a
			read -p "Enter second number : " b
			case "$option" in
				1) add "$a" "$b" ;;
				2) sub "$a" "$b" ;;
				3) mul "$a" "$b" ;;
				4) div "$a" "$b" ;;
			esac
			;;
		5)
			echo "Exited"
			break
			;;
		*)
			echo "Invalid option....."
	esac
	echo
done
