marks = []
for subject in range(5):
	try:
		mark = float(input(f"Enter marks for subject {subject + 1}: "))
		if not 0 <= mark <= 100:
			raise ValueError
		marks.append(mark)
	except ValueError:
		print("Invalid marks. Enter a number from 0 to 100.")
		break
else:
	total = sum(marks)
	average = total / 5
	grade = "A" if average >= 90 else "B" if average >= 80 else "C" if average >= 70 else "D" if average >= 60 else "F"
	print("Total:", total)
	print("Average:", average)
	print("Grade:", grade)
