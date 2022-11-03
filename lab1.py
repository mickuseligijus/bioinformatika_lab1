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

# reverse_sequence = reverse(sequence)

# sequence_frame1 = get_reading_frame(sequence)
# sequence_frame2 = get_reading_frame(sequence[1:])
# sequence_frame3 = get_reading_frame(sequence[2:])

# reverse_sequence_frame1 = get_reading_frame(reverse_sequence)
# reverse_sequence_frame2 = get_reading_frame(reverse_sequence[1:])
# reverse_sequence_frame3 = get_reading_frame(reverse_sequence[2:])


####################################### 1 dalis POROS #################################
# pairs_f1 = get_pairs(sequence_frame1)
# pairs_f2 = get_pairs(sequence_frame2)
# pairs_f3 = get_pairs(sequence_frame3)

# pairs_f4 = get_pairs(reverse_sequence_frame1)
# pairs_f5 = get_pairs(reverse_sequence_frame2)
# pairs_f6 = get_pairs(reverse_sequence_frame3)
#######################################################################################

####################################### 2 dalis tolimiausias STOP START ###############
# pairs_stop_f1 = get_furthest_start(sequence_frame1)
# pairs_stop_f2 = get_furthest_start(sequence_frame2)
# pairs_stop_f3 = get_furthest_start(sequence_frame3)

# pairs_stop_f4 = get_furthest_start(reverse_sequence_frame1)
# pairs_stop_f5 = get_furthest_start(reverse_sequence_frame2)
# pairs_stop_f6 = get_furthest_start(reverse_sequence_frame3)
#######################################################################################

####################################### 3 dalis fragmentai > 100 ######################
# filtered_f1 = get_filtered_pairs(pairs_f1)
# filtered_f2 = get_filtered_pairs(pairs_f2)
# filtered_f3 = get_filtered_pairs(pairs_f3)

# filtered_f4 = get_filtered_pairs(pairs_f4)
# filtered_f5 = get_filtered_pairs(pairs_f5)
# filtered_f6 = get_filtered_pairs(pairs_f6)
#######################################################################################

codons = get_codons()
dicodons = get_dicodons(codons)

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

    
def get_codons_sequence(filtered_pairs,sequence_frame):
    acc = []
    for p in filtered_pairs:
        (a,b) = p
        l = sequence_frame[a:b+1]
        acc = concat_list(acc,l)

    return acc

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

def concat_list(list1, list2):
    for i in list2 :
        list1.append(i)
    return list1

# filtered_frame_list = [
#     (filtered_f1,sequence_frame1),
#     (filtered_f2,sequence_frame2),
#     (filtered_f3,sequence_frame3),
#     (filtered_f4,reverse_sequence_frame1),
#     (filtered_f5,reverse_sequence_frame2),
#     (filtered_f6,reverse_sequence_frame3)]

####################################### 4 dalis kodonu ir dikodonu dazniai #############
# codons_frequency1 = get_frequency(codons,filtered_frame_list,get_codons_sequence)
# dicodons_frequency1 = get_frequency(dicodons,filtered_frame_list,get_dicodons_sequences)
########################################################################################



def combine_methods(seq):

    reverse_seq = reverse(seq)
    filtered_reading_frames = concat_list(get_shifting(seq), get_shifting(reverse_seq))

    return filtered_reading_frames


def get_shifting(seq):
    reading_frames = []
    for i in range(3):
        frame = get_reading_frame(seq[i:])
        pairs = get_pairs(frame)
        filtered_pairs = get_filtered_pairs(pairs)
        reading_frames.append((filtered_pairs,frame))
    
    return reading_frames

def calculate_distance(seq_frequency):

    matrixCodons = []
    matrixDicodons = []
    sum = 0
    for s1 in seq_frequency:
        (info,codon1,dicodon1) = s1
        row = []
        rowDicodons = []
        for s2 in seq_frequency:
            (info2,codon2,dicodon2) = s2
            sum = 0
            sumDicodons = 0
            for i in range(len(codon1)):
                (name1,fr1) = codon1[i]
                (name2,fr2) = codon2[i]

                distance = (abs(fr1-fr2))
                sum = sum + distance

            for ii in range(len(dicodon1)):
                (name3,fr3) = dicodon1[ii]
                (name4,fr4) = dicodon2[ii]

                distanceDicodons = (abs(fr3-fr4))
                sumDicodons = sumDicodons + distanceDicodons

            row.append(sum**1/2)
            rowDicodons.append(sumDicodons**1/2)

        matrixCodons.append((info,row))
        matrixDicodons.append((info,rowDicodons))
    
    return (matrixCodons,matrixDicodons)



def print_matrix(matrix):
    print(len(matrix))
    for row in matrix:
        (info, values) = row
        print(info, end = ' ')
        for v in values:
            print(v, end = ' ')
        print()

def print_distribution(seq_fr):
    print("\n")
    most_common(seq_fr)
    print("\n")
    for s in seq_fr:
        (info, codons, dicodons) = s
        co = sorted(codons, key=lambda tup: tup[1], reverse=True)
        dico =sorted(dicodons, key=lambda tup: tup[1], reverse=True)
        print(info, co[0], co[1], co[2])
        print(info, dico[0], dico[1], dico[2])
    

def most_common(list):
    codon_list = []
    dicodon_list = []

    for codon in codons:
        accCodon = 0
        for l in list:
            (_, co, _) = l
            for c in co:
                (name, amountCodon) = c
                if name == codon:
                    accCodon += amountCodon
        codon_list.append((codon,accCodon))

    for dicodon in dicodons:
        accDicodon = 0
        for l in list:
            (_, _, dico) = l
            for d in dico:
                (name, amountDicoodon) = d
                if name == dicodon:
                    accDicodon += amountDicoodon
        dicodon_list.append((dicodon,accDicodon))

    co = sorted(codon_list, key=lambda tup: tup[1], reverse=True)
    dico =sorted(dicodon_list, key=lambda tup: tup[1], reverse=True)

    print("codons")
    print(co[0], co[1], co[2])
    print("dicodons")
    print(dico[0], dico[1], dico[2])



        
# def max_number(x):
#     temp = 0
#     code = ""
#     previous =""
#     temp_previous = 0
#     for i in x:
#         (a,b) = i
#         if b>=temp:
#             temp_previous = temp
#             previous = code
#             if temp == 0:
#                 previous = a
#                 temp_previous = b
#             temp = b  
#             code = a

    
#     return ((code, temp), (previous,temp_previous))

data_sources = ["data/bacterial1.fasta","data/bacterial2.fasta","data/bacterial3.fasta","data/bacterial4.fasta","data/mamalian1.fasta","data/mamalian2.fasta","data/mamalian3.fasta","data/mamalian4.fasta"]

seq_frequency = []
for location in data_sources:
    info = location.replace("data/", "")
    info = info.replace(".fasta", "")
    (meta_info, seq) = read_from_file(location)
    filtered_reading_frames = combine_methods(seq)
    codons_frequency = get_frequency(codons,filtered_reading_frames,get_codons_sequence)
    dicodons_frequency = get_frequency(dicodons,filtered_reading_frames,get_dicodons_sequences)
    seq_frequency.append((info,codons_frequency,dicodons_frequency))        

(matrix_codons, matrix_dicodons) = calculate_distance(seq_frequency)
print_matrix(matrix_codons)
print_matrix(matrix_dicodons)
print_distribution(seq_frequency)





