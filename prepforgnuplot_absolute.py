# ----------------------------------------------------------------------------------$
# Python script that preps file with speedup times ready for gnuplot
# Lewis Sharpe
# Date: 18/05/20
# Run with command: python prepforgnuplot_absolute.py
# ----------------------------------------------------------------------------------$
infile = "absolute.csv"
outfile = "absolute_cleaned.csv"
delete_list = ["core-number-"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()


