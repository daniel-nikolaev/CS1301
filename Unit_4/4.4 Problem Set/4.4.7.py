#Write a function called multiply_file_by_index. This function
#should take two parameters, both strings. The first string is
#the filename of a file to which to write (output_file), and
#the second string is the filename of a file from which to read
#(input_file).
#
#In the input file, there will be an integer on every line.
#To the output file, you should write the integer from the
#original file multiplied by the line number on which it
#appeared. You should assume that the first line of the file
#is line 1 (which is different from a list, where the first item
#is at index 0).
#
#For example, if the input file contained this text:
#1
#4
#3
#7
#6
#
#Then the output file would contain this text:
#1
#8
#9
#28
#30


#Add your code here!
def multiply_file_by_index(output_file, input_file):
    # Open input file for reading
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()
        
    # Open output file for writing
    with open(output_file, 'w') as output_file:
        # Loop through lines, compute and write to output file
        for i, line in enumerate(lines, start=1):
            number = int(line.strip())
            multiplied = number * i
            output_file.write(str(multiplied) + "\n")



#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, output_file.txt should have the text:
#1
#8
#9
#28
#30
multiply_file_by_index("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")

#If you accidentally erase input_file.txt, here's its original
#text to copy back in (remove the pound signs):
#1
#4
#3
#7
#6


