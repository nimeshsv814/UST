Check_File() {
	file="$1"
	if [ ! -e "$file" ]; then
		echo "File $file does not exist."
		return
	fi
	echo "File $file does exist"

	if [ -r "$file" ]; then
		echo "Read Permission : Yes"
	else
		echo "Read Permission : No"
	fi

	if [ -w "$file" ]; then
		echo "Write Permission : Yes"
	else
		echo "Write Permission : No"
	fi

	if [ -x "$file" ]; then
		echo "Execute Permission : Yes"
	else
		echo "Execute  Permission : No"
	fi
}

read -p "Enter file path : " path
Check_File "$path"
