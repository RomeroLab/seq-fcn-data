notes = """

Data from: Dissecting enzyme function with microfluidic-based deep mutational scanning

The unlabeled data contains the initial (unsorted) library.  It contains: ~3.6 M sequences
The positive data contains active (sorted) sequences.  Three experimental replicates were merged.  It contains: ~10.7 M sequences
The the high temp data contains sequences that were active after a heat challenge.  Three experimental replicates were merged.  It contains: ~7.1 M sequences
"""


# this script inputs the mutation files (~MB file size) and outputs files containing full sequences (several GB)
WT_Bgl3 = 'MVPAAQQTAMAPDAALTFPEGFLWGSATASYQIEGAAAEDGRTPSIWDTYARTPGRVRNGDTGDVATDHYHRWREDVALMAELGLGAYRFSLAWPRIQPTGRGPALQKGLDFYRRLADELLAKGIQPVATLYHWDLPQELENAGGWPERATAERFAEYAAIAADALGDRVKTWTTLNEPWCSAFLGYGSGVHAPGRTDPVAALRAAHHLNLGHGLAVQALRDRLPADAQCSVTLNIHHVRPLTDSDADADAVRRIDALANRVFTGPMLQGAYPEDLVKDTAGLTDWSFVRDGDLRLAHQKLDFLGVNYYSPTLVSEADGSGTHNSDGHGRSAHSPWPGADRVAFHQPPGETTAMGWAVDPSGLYELLRRLSSDFPALPLVITENGAAFHDYADPEGNVNDPERIAYVRDHLAAVHRAIKDGSDVRGYFLWSLLDNFEWAHGYSKRFGAVYVDYPTGTRIPKASARWYAEVARTGVLPTAGDPNSSSVDKLAAALEHHHHHH*'

files = ['unlabeled_Bgl3_mutations.txt','positive_Bgl3_mutations.txt','positive_Bgl3_mutations_hitemp.txt']

include_WT = False # don't include WT sequences in the output 


if include_WT: # include WT sequences 
    for f in files:
        outfile = open(f.replace('mutations','sequences'),'w')
        variants = [m.split(',') for m in open(f).read().strip().split('\n')]

        for mut in variants:
            if mut[0]=='WT':
                outfile.write(WT_Bgl3+'\n')        
            else:
                mutant_seq = WT_Bgl3
                for m in mut:
                    pos = int(m[1:-1])
                    AA = m[-1]
                    mutant_seq = mutant_seq[:pos]+AA+mutant_seq[pos+1:]
                outfile.write(mutant_seq+'\n')        

else: # don't include WT sequences
    for f in files:
        outfile = open(f.replace('mutations','sequences'),'w')
        variants = [m.split(',') for m in open(f).read().strip().split('\n')]

        for mut in variants:
            if mut[0]!='WT':
                mutant_seq = WT_Bgl3
                for m in mut:
                    pos = int(m[1:-1])
                    AA = m[-1]
                    mutant_seq = mutant_seq[:pos]+AA+mutant_seq[pos+1:]
                outfile.write(mutant_seq+'\n')        
