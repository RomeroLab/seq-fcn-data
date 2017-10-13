
def read_data(datafile):
    '''reads the standard data file format I have been using'''
    data = open(datafile,'r').read().strip().replace('\t','').split('\n')

    # remove all comments in data file 
    nocomments = [line.split('#')[0].strip() for line in data if len(line.strip())>0 and line.strip()[0]!='#']


    ## get the header
    header_ind = [i for i,row in enumerate(nocomments) if '>header' in row][0] + 1
    header = [h.strip() for h in nocomments[header_ind].split(',')]

    # get the data
    data_ind = [i for i,row in enumerate(nocomments) if '>data' in row][0] + 1
    data = []
    for line in nocomments[data_ind:]:
        d = [e.strip() for e in line.split(',')]
        data.append(d)
    return header,data


notes = """

Data from Martin.  

Publication: Directed Evolution of Gloeobacter violaceus Rhodopsin Spectral Properties"""

# Gloeobacter violaceus Rhodopsin sequence
WT = 'MLMTVFSSAPELALLGSTFAQVDPSNLSVSDSLTYGQFNLVYNAFSFAIAAMFASALFFFSAQALVGQRYRLALLVSAIVVSIAGYHYFRIFNSWDAAYVLENGVYSLTSEKFNDAYRYVDWLLTVPLLLVETVAVLTLPAKEARPLLIKLTVASVLMIATGYPGEISDDITTRIIWGTVSTIPFAYILYVLWVELSRSLVRQPAAVQTLVRNMRWLLLLSWGVYPIAYLLPMLGVSGTSAAVGVQVGYTIADVLAKPVFGLLVFAIALVKTKADQESSEPHAAIGAAANKSGGSLIS'

header,data = read_data('rhodopsin_peaks.data')

names = [d[0] for d in data]
mutations = [d[1].split('/') for d in data]
peaks = [d[2] for d in data]


# turn the mutations into sequences
sequences = [WT]
for mut in mutations[1:]:
    mutant =  WT
    for m in mut:
        pos = int(m[1:-1])-1
        if m[0]!=WT[pos]:
            print('WT seq positions dont match--numbering problem somewhere!')
            1/0
        else:
            mutant = mutant[:pos]+m[-1]+mutant[pos+1:]
    sequences.append(mutant)
