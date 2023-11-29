#five sets of child, father, mother, found on 1000 Genomes online portal.
children_identifiers = ["NA12877", "NA12766", "NA12817", "NA12865", "NA07019"]
fathers_identifiers = ["NA12889", "NA12775", "NA12827", "NA12874", "NA07022"]
mothers_identifiers = ["NA12890", "NA12776", "NA12828", "NA12875", "NA07056"]

#will hold the column indexes for each trio
children = [0,0,0,0,0]
fathers = [0,0,0,0,0]
mothers = [0,0,0,0,0]

# search the header for the column index associated with each person and sort them into the appropriate array.
with open("ALL.chip.omni_broad_sanger_combined.20140818.snps.genotypes.vcf") as data:
    for line_data in data:
        if line_data.startswith("#C"):
            split_data = line_data.split("\t")
            counter = 0
            for i in range(len(children_identifiers)):
                for item in split_data:
                    if item == children_identifiers[i]:
                        children[i] = counter

                    if item == fathers_identifiers[i]:
                        fathers[i] = counter

                    if item == mothers_identifiers[i]:
                        mothers[i] = counter

                    counter = counter+1
                counter = 0
            break

# search the other columns for variants found in each child not present in either of their parents.    
with open("ALL.chip.omni_broad_sanger_combined.20140818.snps.genotypes.vcf") as data:

    # a running count of each type of mutation, along with the total number
    count_A_to_T = 0
    count_A_to_G = 0
    count_A_to_C = 0
    count_T_to_A = 0
    count_T_to_G = 0
    count_T_to_C = 0
    count_G_to_A = 0
    count_G_to_T = 0
    count_G_to_C = 0
    count_C_to_A = 0
    count_C_to_T = 0
    count_C_to_G = 0
    count_other = 0
    count_total_mutations = 0
    count_mutations_by_trio = [0,0,0,0,0]

    # data to be used to create a log file of all mutations found, listing information that might be useful
    output_string = ""

    
    for line_data in data:
        if not line_data.startswith("#"):
            split_data = line_data.split("\t")
            
            for i in range(len(children)):
                kid = children[i]
                dad = fathers[i]
                mom = mothers[i]

                if split_data[kid] in ["1/1", "1/0", "0/1"] and split_data[dad] == "0/0" and split_data[mom] == "0/0" and split_data[6] == "PASS":

                    reference = split_data[3]
                    alternate = split_data[4]

                    if reference == "A" and alternate == "T":
                        count_A_to_T += 1
                    elif reference == "A" and alternate == "G":
                        count_A_to_G += 1
                    elif reference == "A" and alternate == "C":
                        count_A_to_C += 1
                    elif reference == "T" and alternate == "A":
                        count_T_to_A += 1
                    elif reference == "T" and alternate == "G":
                        count_T_to_G += 1
                    elif reference == "T" and alternate == "C":
                        count_T_to_C += 1
                    elif reference == "G" and alternate == "A":
                        count_G_to_A += 1
                    elif reference == "G" and alternate == "T":
                        count_G_to_T += 1
                    elif reference == "G" and alternate == "C":
                        count_G_to_C += 1
                    elif reference == "C" and alternate == "A":
                        count_C_to_A += 1
                    elif reference == "C" and alternate == "T":
                        count_C_to_T += 1
                    elif reference == "C" and alternate == "G":
                        count_C_to_G += 1
                    else:
                        count_other += 1

                    count_total_mutations +=1
                    count_mutations_by_trio[i] += 1

                    output_string = output_string + "\r\n" + "Loc: " + split_data[1] + " Mut_code: " + split_data[2] + " Reference: " + split_data[3] + " Alternate: " + split_data[4] + " Child: " + split_data[kid] + " Mother: " + split_data[mom] + " Father: " + split_data[dad] + " Qual: " + split_data[5] + " info: " + split_data[6] + " " + split_data[7] + " " + split_data[8]
                    #print(output_string)

output_string = output_string + "\r\n" + "A --> T: " + str(count_A_to_T)
output_string = output_string + "\r\n" + "A --> G: " + str(count_A_to_G)
output_string = output_string + "\r\n" + "A --> C: " + str(count_A_to_C)
output_string = output_string + "\r\n" + "T --> A: " + str(count_T_to_A)
output_string = output_string + "\r\n" + "T --> G: " + str(count_T_to_G)
output_string = output_string + "\r\n" + "T --> C: " + str(count_T_to_C)
output_string = output_string + "\r\n" + "G --> A: " + str(count_G_to_A)
output_string = output_string + "\r\n" + "G --> T: " + str(count_G_to_T)
output_string = output_string + "\r\n" + "G --> C: " + str(count_G_to_C)
output_string = output_string + "\r\n" + "C --> A: " + str(count_C_to_A)
output_string = output_string + "\r\n" + "C --> T: " + str(count_C_to_T)
output_string = output_string + "\r\n" + "C --> G: " + str(count_C_to_G)
output_string = output_string + "\r\n" + "Other: " + str(count_other)
output_string = output_string + "\r\n" + "Total: " + str(count_total_mutations)

for i in range(len(children)):
    output_string = output_string + "\r\n" + "Trio " + str(i+1) + ": " + str(count_mutations_by_trio[i])


with open("output.txt", 'w') as new_file:
    new_file.write(output_string)

