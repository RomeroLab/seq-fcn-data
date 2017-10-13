
notes = """

Data from: Dissecting enzyme function with microfluidic-based deep mutational scanning

The unlabeled data contains the initial (unsorted) library.  It contains: ~1.5 M sequences
The positive data contains active (sorted) sequences.  Three experimental replicates were merged.  It contains: ~2.6 M sequences

"""

# this script inputs the mutation files (~MB file size) and outputs files containing full sequences (several GB)

WT_Bgl3 = 'MVPAAQQTAMAPDAALTFPEGFLWGSATASYQIEGAAAEDGRTPSIWDTYARTPGRVRNGDTGDVATDHYHRWREDVALMAELGLGAYRFSLAWPRIQPTGRGPALQKGLDFYRRLADELLAKGIQPVATLYHWDLPQELENAGGWPERATAERFAEYAAIAADALGDRVKTWTTLNEPWCSAFLGYGSGVHAPGRTDPVAALRAAHHLNLGHGLAVQALRDRLPADAQCSVTLNIHHVRPLTDSDADADAVRRIDALANRVFTGPMLQGAYPEDLVKDTAGLTDWSFVRDGDLRLAHQKLDFLGVNYYSPTLVSEADGSGTHNSDGHGRSAHSPWPGADRVAFHQPPGETTAMGWAVDPSGLYELLRRLSSDFPALPLVITENGAAFHDYADPEGNVNDPERIAYVRDHLAAVHRAIKDGSDVRGYFLWSLLDNFEWAHGYSKRFGAVYVDYPTGTRIPKASARWYAEVARTGVLPTAGDPNSSSVDKLAAALEHHHHHH*'

files = ['unlabeled_Bgl3_mutations.txt','positive_Bgl3_mutations.txt']

for f in files:
    outfile = open(f.replace('mutations','sequences'),'w')
    variants = [m.split(',') for m in open(f).read().strip().split('\n')]

    for mut in variants:
        mutant_seq = WT_Bgl3
        for m in mut:
            pos = int(m[1:-1])
            AA = m[-1]
            mutant_seq = mutant_seq[:pos]+AA+mutant_seq[pos+1:]
        outfile.write(mutant_seq+'\n')        
