# -----------------------------------------------------------------------------------------------------------------------------
# Python script that searches for time taken line for each core number in log file and print them as a list in another text file.
# Lewis Sharpe
# Date: 04/05/20
# -----------------------------------------------------------------------------------------------------------------------------
with open('LOG', 'r') as searchfile:
    for line in searchfile:
        if 'Time taken for core(s) number' in line:
            print line
with open('str_patmatch_output.txt', 'a') as the_file:
    the_file.write(line)
# -----------------------------------------------------------------------------------------------------------------------------
