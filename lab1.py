def read_from_file(file_location):
    f = open(file_location,'r')
    content = f.read()
    f.close()
    a = content.find("\n")
    sequence = content[a:]
    sequence = sequence.replace("\n","")
    return (content[:a],sequence)

def get_reading_frame(s):
    list = []
    while(s != ""):
        list.append(s[0:3])
        s = s[3:]
    return list

def reverse(s):
    rev = ""
    while(s != ""):
        if s[0] == "A":
            rev += "T"
        elif s[0] == "T":
            rev += "A"    
        elif s[0] == "C":
            rev += "G"
        elif s[0] == "G":
            rev += "C"
        s = s[1:]
    return rev

def get_start_position_list(list):
    start_position_list = []
    index = 0
    for l in list:
        if l == start:
            start_position_list.append(index)
        index=index+1
    return start_position_list

def get_ending_position_list(list):
    ending_position_list = []
    index = 0
    for l in list:
        if l == ending1 or l == ending2 or l == ending3:
            ending_position_list.append(index)
        index=index+1
    return ending_position_list

def get_pairs(list):
    start_position_list = get_start_position_list(list)
    ending_position_list = get_ending_position_list(list)

    pairs = []
    for s in start_position_list:
        for e in ending_position_list:
            if s < e:
                pairs.append((s,e))
                break
    return pairs

def get_furthest_start(list):
    start = get_start_position_list(list)
    ending = get_ending_position_list(list)

    pairs = []
    length = len(ending)
    for i in range(len(ending)):
        temp = -1
        if i !=length and i!=length-1:
            for s in start:
                if ending[i] < s and ending[i+1] > s:
                    temp = s
                elif ending[i] <s and ending[i+1] < s:
                    break
        if temp != -1:
            pairs.append((ending[i],temp))

    return pairs

def get_filtered_pairs(pairs):
    list = []
    for p in pairs:
        (a,b) = p
        length = (b-a+1)*3
        # print(length)
        if length>=100:
            list.append(p)
    return list

def get_codons():
    x = {"T","C","A","G"}
    codons = []
    for i in x:
        for ii in x:
            for iii in x:
                codon = i+ii+iii
                codons.append(codon)
    return codons

def get_dicodons(codons):
    dicodons = []
    for i in codons:
        for ii in codons:
            dicodon = i+ii
            dicodons.append(dicodon)
    return dicodons


(info, sequence) = read_from_file('data/bacterial1.fasta')

start = "ATG"
ending1 = "TAA"
ending2 = "TGA"
ending3 = "TAG"

reverse_sequence = reverse(sequence)

sequence_frame1 = get_reading_frame(sequence)
sequence_frame2 = get_reading_frame(sequence[1:])
sequence_frame3 = get_reading_frame(sequence[2:])

reverse_sequence_frame1 = get_reading_frame(reverse_sequence)
reverse_sequence_frame2 = get_reading_frame(reverse_sequence[1:])
reverse_sequence_frame3 = get_reading_frame(reverse_sequence[2:])


####################################### 1 dalis POROS #################################
pairs_f1 = get_pairs(sequence_frame1)
pairs_f2 = get_pairs(sequence_frame2)
pairs_f3 = get_pairs(sequence_frame3)

pairs_f4 = get_pairs(reverse_sequence_frame1)
pairs_f5 = get_pairs(reverse_sequence_frame2)
pairs_f6 = get_pairs(reverse_sequence_frame3)
#######################################################################################

####################################### 2 dalis tolimiausias STOP START ###############
pairs_stop_f1 = get_furthest_start(sequence_frame1)
pairs_stop_f2 = get_furthest_start(sequence_frame2)
pairs_stop_f3 = get_furthest_start(sequence_frame3)

pairs_stop_f4 = get_furthest_start(reverse_sequence_frame1)
pairs_stop_f5 = get_furthest_start(reverse_sequence_frame2)
pairs_stop_f6 = get_furthest_start(reverse_sequence_frame3)
#######################################################################################

####################################### 3 dalis fragmentai > 100 ######################
filtered_f1 = get_filtered_pairs(pairs_f1)
filtered_f2 = get_filtered_pairs(pairs_f2)
filtered_f3 = get_filtered_pairs(pairs_f3)

filtered_f4 = get_filtered_pairs(pairs_f4)
filtered_f5 = get_filtered_pairs(pairs_f5)
filtered_f6 = get_filtered_pairs(pairs_f6)
#######################################################################################

codons = get_codons()
dicodons = get_dicodons(codons)

#finds frequency of codons in a specific reading frame
# def get_codons_frequency(pairs, sequence_frame, codons):
#     list = []
#     for p in pairs:
#         (a,b) = p
#         l = sequence_frame[a:b+1]
#         list.append(l)
    
#     f_list = []
#     for l in list:
#         acc = []
#         for codon in codons:
#             index = 0
#             for element in l:
#                 if element == codon:
#                     index=index+1
#             acc.append((codon,index))
#         f_list.append(acc)

#     accumulator = []
#     for codon in codons:
#         accumulator.append((codon,0))

#     for l in f_list:
#         for pair in l:
#             (codone,frequency) = pair
#             for i in range(len(accumulator)):
#                 (codone_acc, frequency_acc) = accumulator[i]
#                 if codone_acc == codone:
#                     frequency_acc+=frequency
#                     accumulator[i] = (codone,frequency_acc)

#     return accumulator

    # print(len(pairs))
                
#######################################################################################

# frequency1 = get_codons_frequency(filtered_f1,sequence_frame1,codons)
# frequency2 = get_codons_frequency(filtered_f2,sequence_frame2,codons)
# frequency3 = get_codons_frequency(filtered_f3,sequence_frame3,codons)

# frequency4 = get_codons_frequency(filtered_f4,reverse_sequence_frame1,codons)
# frequency5 = get_codons_frequency(filtered_f5,reverse_sequence_frame2,codons)
# frequency6 = get_codons_frequency(filtered_f6,reverse_sequence_frame3,codons)

# frenquencies = [frequency1,frequency2,frequency3,frequency4,frequency5,frequency6]
# print(frenquencies)



def get_dicodons_sequences(filtered_pairs, sequence_frame):
    list = []
    for p in filtered_pairs:
        (a,b) = p
        l = sequence_frame[a:b+1]
        list.append(l)

    dicodons_list_frame = []
    m = 0
    counter = 0
    temp =""
    for l in list:
        for i in l:
            temp += i
            counter = counter + 1
            if counter == 2:
                counter = 0
                dicodons_list_frame.append(temp)
                temp = ""
    
    return dicodons_list_frame

# print(get_dicodons_sequences(filtered_f1, sequence_frame1))

def get_frequency(pattern, filtered_frame_list, get_sequence):
    acc = []
    for filtered_frame in filtered_frame_list:
        (filtered, frame) = filtered_frame
        sequence = get_sequence(filtered,frame)
        acc = concat_list(acc, sequence)

    frenquencies = []

    for p in pattern:
        counter = 0
        for pp in acc:
            if p == pp:
                counter = counter +1
        frenquencies.append((p,counter))
    
    return frenquencies

# def get_dicodons_frequency(filtered_frame_list):

#     acc_dicodons = []
#     for filtered_frame in filtered_frame_list:
#         (filtered, frame) = filtered_frame
#         dicodons_sequence = get_dicodons_sequences(filtered,frame)
#         acc_dicodons = concat_list(acc_dicodons, dicodons_sequence)

#     frenquencies = []
#     for dicodon in dicodons:
#         counter = 0
#         for dicodon_sequence in acc_dicodons:
#             if dicodon == dicodon_sequence:
#                 counter = counter +1
#         frenquencies.append(dicodon,counter)
    
#     return frenquencies

# def get_codons_frequency(filtered_frame_list,a):

#     acc_codons = []
#     for filtered_frame in filtered_frame_list:
#         (filtered, frame) = filtered_frame
#         codons_sequence = get_codons_sequence(filtered,frame)
#         acc_dicodons = concat_list(acc_dicodons, codons_sequence)

#     frenquencies = []
#     for codon in codons:
#         counter = 0
#         for codon_sequence in acc_codons:
#             if codon == codon_sequence:
#                 counter = counter +1
#         frenquencies.append(codon,counter)
    
#     return frenquencies
    
def get_codons_sequence(filtered_pairs,sequence_frame):
    acc = []
    for p in filtered_pairs:
        (a,b) = p
        l = sequence_frame[a:b+1]
        acc = concat_list(acc,l)

    return acc

def concat_list(list1, list2):
    for i in list2 :
        list1.append(i)
    return list1

filtered_frame_list = [
    (filtered_f1,sequence_frame1),
    (filtered_f2,sequence_frame2),
    (filtered_f3,sequence_frame3),
    (filtered_f4,reverse_sequence_frame1),
    (filtered_f5,reverse_sequence_frame2),
    (filtered_f6,reverse_sequence_frame3)]

# get_dicodons_frequency(filtered_frame_list)
print(get_frequency(codons,filtered_frame_list,get_codons_sequence))


#sums up frequency of different reading frames
# def sum_up_frequency(f_list):
#     accumulator = []
#     for codon in codons:
#         accumulator.append((codon,0))

#     for l in f_list:
#         for pair in l:
#             (codone,frequency) = pair
#             for i in range(len(accumulator)):
#                 (codone_acc, frequency_acc) = accumulator[i]
#                 if codone_acc == codone:
#                     frequency_acc+=frequency
#                     accumulator[i] = (codone,frequency_acc)

#     return accumulator

# print(sum_up_frequency(frenquencies))

codons_frequency = get_frequency(codons,filtered_frame_list,get_codons_sequence)
dicodons_frequency = get_frequency(dicodons,filtered_frame_list,get_dicodons_sequences)

print(dicodons_frequency)
# v2 = sum_up_frequency(frenquencies)

# print(v1==v2)










# codons = {
#     "TTT","TTC","TTA","TTG",
#     "TCT","TCC","TCA","TCG",
#     "TAT","TAC","TAA","TAG",
#     "TGT","TGC","TGA","TGG",

#     "CTT","CTC","CTA","CTG",
#     "CCT","CCC","CCA","CCG",
#     "CAT","CAC","CAA","CAG",
#     "CGT","CGC","CGA","CGG",

#     "ATT","ATC","ATA","ATG",
#     "ACT","ACC","ACA","ACG",
#     "AAT","AAC","AAA","AAG",
#     "AGT","AGC","AGA","AGG",

#     "GTT","GTC","GTA","GTG",
#     "GCT","GCC","GCA","GCG",
#     "GAT","GAC","GAA","GAG",
#     "GGT","GGC","GGA","GGA"
#     }

# x = "AAAATGTACTATTAG"

# p = get_reading_frame(x)
# m = get_pairs(p)
# print(m)

# t = get_filtered_pairs(m)



# print("pirmas: \n") 
# print(listFrame1)
# print("antras: \n") 
# print(listFrame2)
# print("trecias: \n") 
# print(listFrame3)

# print(reverse("ACGTTTGA"))