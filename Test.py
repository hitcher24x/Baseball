import unittest
from Baseball import Baseball, Cnp

class TestBaseball(unittest.TestCase):
    
    def test_Baseball(self):
        """ evaluates if the program runs correctly and returns the appropriate results"""


        """
We created manually a simulated file, Simulated_data.csv, containing football data:

- Ronaldo has played for      : RealMadrid, InterMilan, ACMilan, Paris
- Figo has played for         : RealMadrid, InterMilan, Barcelona, Paris
- Ibrahimovich has played for : Barcelona, InterMilan, ACMilan, Paris

with a Threshold of 2 players, we should obtain the following Triplets:
        """
        simulated=['InterMilan,Paris,RealMadrid','Barcelona,InterMilan,Paris',
                   'ACMilan,InterMilan,Paris']
        print("Tests The Program : ")
        baseball=Baseball(2000,2000,2)
        baseball.url="Simulated_data_%d_%d.csv"
        baseball.reader()
        baseball.playerTeams()
        baseball.cleaner()
        baseball.calculator()
        compiled=[]
        for name in baseball.triples:
            if baseball.triples[name]>= baseball.Threshold:
                compiled+=[name]
        self.assertEqual(set(compiled),set(simulated))
        

        
if __name__ == '__main__':
    unittest.main()
