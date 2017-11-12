import pandas as pd

def Cnp(n,p, l=None, res=None):
    """ calculates p-uplets among n elements and returns a list of the p-uplets """
    
    if l is None: l=[]
    if res is None: res=[]
    if p==0:
        res.append(l)
        return res 
    if n==0:
        return res
    else:
        l1=list(l)
        l1.append(n)
        Cnp(n-1, p-1, l1, res)
        Cnp(n-1, p, l, res)
        return res


class Baseball:
    def __init__(self,begin,end,threshold):
        
        self.begin=begin # first year considered for the program
        self.end=end # last year considered for the program
        self.Threshold=threshold # ex : 50
        self.url="https://s3.amazonaws.com/dd-interview-data/data_scientist/baseball/appearances/%d/%d-0,000"
        self.liste= pd.DataFrame({'Player_ID': [],'Team': []}) # initialise dataframe
        self.dico={} # dictionary of players (keys) and teams associated to each (items)
        self.triples={} # dictionary of 3 teams paired (keys) and the number of players associated (items)

    def reader(self):
        """ downloads data from the url """
        
        for i in range (self.begin,self.end+1):
            urlbis = self.url % (i,i)
            data=pd.read_csv(urlbis,names=["Year","Team","League","Player_ID","Player_Name","Total_games_played","Games started",
                                       "Games in which player batted","Games in which player appeared on defense",
                                       "Games as pitcher","Games as catcher","Games as firstbaseman","Games as secondbaseman",
                                       "Games as thirdbaseman","Games as shortstop","Games as leftfielder","Games as centerfielder",
                                       "Games as right fielder","Games as outfielder","Games as designated hitter",
                                       "Games as pinch hitter","Games as pinch runner"],usecols=['Player_ID','Team'])

            self.liste=pd.concat([self.liste,data[['Player_ID','Team']]])

    def playerTeams(self):
        """ crosses the dataframe: provides the teams of each player; we use numpy array for faster computations """
        
        for row in self.liste.values:
            if row[0] in self.dico:
                self.dico[row[0]]=self.dico[row[0]]+" "+row[1]
            else:
                self.dico[row[0]]=row[1]

    def cleaner(self):
        """ puts the teams of a player into a list with no repetition """
        """ it also removes players who have played for less than 3 teams """
        
        for player in list(self.dico.keys()): # makes a copy of the keys so that we can modify dico
            self.dico[player]=list(set(self.dico[player].split()))
            if len(self.dico[player])< 3:
                self.dico.pop(player)

    

    def calculator(self):
        """ calculates the number of players that have played for any triple of teams"""

        for player in self.dico.keys():
            cnp=Cnp(len(self.dico[player]),3) # takes every possible choice of "3 teams among n teams"
            for l in cnp:

                # we sort the triplet to preserve its uniqueness in the counting
                triplet=sorted([self.dico[player][l[0]-1],self.dico[player][l[1]-1],self.dico[player][l[2]-1]])
                
                name="%s,%s,%s"%(triplet[0],triplet[1],triplet[2])
                if name in self.triples:
                    self.triples[name]+=1
                else:
                    self.triples[name]=1
                    
    
    def start_program(self):
        """ runs the program """
        print("Parameters : ")
        print("Begin : %d" % self.begin)
        print("End : %d" % self.end)
        print("Threshold : %d" % self.Threshold)
        print(" ")
        print("Starting Step 1/3 :")
        print("Downloading data...")
        self.reader()
        print("Step 1/3 finished correctly.")
        print("Starting Step 2/3 :")
        print("Parsing and Cleaning data for each Player...")
        self.playerTeams()
        self.cleaner()
        print("Step 2/3 finished correctly.")
        print("Starting Step 3/3 :")
        print("Creating Triplets of Teams and Counting Players...")
        self.calculator()
        print("Step 3/3 finished correctly.")
        print("The Triplets are : ")
        Final=[]
        for name in self.triples:
            if self.triples[name]>=self.Threshold:
                print(name)
                Final+=[name]

                    
        
        




    
