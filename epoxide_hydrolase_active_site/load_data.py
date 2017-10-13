
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

Data Sources: 

epoxide hydrolase data
from: Constructing and Analyzing the Fitness Landscape of an Experimental Evolutionary Process
Table S2. Experimental results obtained for the mutants as catalysts in the hydrolytic kinetic resolution of rac-1


"""

# load data
names,data = read_data('reetz_epoxide_hydrolase.data')

mutations = dict()
mutations['B'] = ['L215F', 'A217N', 'R219S']
mutations['C'] = ['M329P', 'L330Y']
mutations['D'] = ['C350V']
mutations['E'] = ['T317W', 'T318V']
mutations['F'] = ['L249Y']





