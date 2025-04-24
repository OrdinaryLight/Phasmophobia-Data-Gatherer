import csv

# Input and output file names
input_file = "output.txt"
output_file = "games.csv"

# Read the input file and process lines
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)

    # header
    writer.writerow(["Game Number", "Ghost Name", "Multiplier", "Evidence Count", "Map", "Blood Moon"])

    for line in infile:
        parts = line.strip().split(" : ")

        # check for blood moon
        blood_moon = parts[-1] == "bm"
        if blood_moon:
            parts.pop()

        game_num = parts[0].split(" ")[1]
        ghost_name = parts[1]
        multiplier = parts[2].split(" ")[1][:-1]  # Remove trailing 'x'
        num_evidence = parts[3].split(" ")[0]
        game_map = parts[4]

        # Write to CSV
        writer.writerow([game_num, ghost_name, multiplier, num_evidence, game_map, blood_moon])

print(f"Data successfully written to {output_file}")

"""
Code this in python
($inputFile) = output.txt
reason: read ($inputFile), add to new csv file
Format from ($inputFile):
Game ($gameNum) : ($ghostName) : Multiplier ($decimalMultiplier)x : ($numEvidence) Evidence : ($map)
will have a ( : bm) at end if is blood moon. check via length of array when split by " : "
"""