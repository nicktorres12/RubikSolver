from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.model.cube import Cube
 

class SolveTest(TestCase):
        
    
    #test if cube is missing    
    def test110_solve_validateCube_missingCube(self):
        encodedCube = None 
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
    
    #test that less than 54 characters in cube    
    def test120_solve_validateCube_lessThan54(self):
        encodedCube = 'bbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
        
    #test if invalid characters in cube          
    def test130_solve_validateCube_invalidValue(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyy;;;;;;;;;'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
        
    #test if more or less than 6 unique Values in cube            
    def test140_solve_validateCube_UniqueValue(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrroooooooo1ggggggggyyyyyyyyy1111111112'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
        
    #test to make sure cube has unique center values
    def test150_solve_validateCube_UniqueCenters(self):
        encodedCube = 'bbbbbbbborrrrrrrrroooobooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
    
    #tests to see if bottom layer is solved. This is scramble test #1
    def test160_solve_bottomlayer(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        parms = {}
        parms['cube'] = encodedCube
        dirs = solve(parms)
        parms['dir'] = dirs['solution']
        result = rotate(parms)
        self.assertEqual('w', result.get('cube')[45])
        self.assertEqual('w', result.get('cube')[46])
        self.assertEqual('w', result.get('cube')[47])
        self.assertEqual('w', result.get('cube')[48])
        self.assertEqual('w', result.get('cube')[50])
        self.assertEqual('w', result.get('cube')[51])
        self.assertEqual('w', result.get('cube')[52])
        self.assertEqual('w', result.get('cube')[53])
        self.assertEqual(result.get('cube')[4], result.get('cube')[6])
        self.assertEqual(result.get('cube')[4], result.get('cube')[7])
        self.assertEqual(result.get('cube')[4], result.get('cube')[8])
        self.assertEqual(result.get('cube')[13], result.get('cube')[15])
        self.assertEqual(result.get('cube')[13], result.get('cube')[16])
        self.assertEqual(result.get('cube')[13], result.get('cube')[17])
        self.assertEqual(result.get('cube')[22], result.get('cube')[24])
        self.assertEqual(result.get('cube')[22], result.get('cube')[25])
        self.assertEqual(result.get('cube')[22], result.get('cube')[26])
        self.assertEqual(result.get('cube')[31], result.get('cube')[33])
        self.assertEqual(result.get('cube')[31], result.get('cube')[34])
        self.assertEqual(result.get('cube')[31], result.get('cube')[35])
    #tests to see if bottom layer is solved. This is scramble test #2
    def test170_solve_bottomlayer(self):
        encodedCube = 'ggowbgrorybyyrowgobbwggywoybywoobbrgoyrryrrwgywbwwrobg'
        parms = {}
        parms['cube'] = encodedCube
        dirs = solve(parms)
        parms['dir'] = dirs['solution']
        result = rotate(parms)
        self.assertEqual('w', result.get('cube')[45])
        self.assertEqual('w', result.get('cube')[46])
        self.assertEqual('w', result.get('cube')[47])
        self.assertEqual('w', result.get('cube')[48])
        self.assertEqual('w', result.get('cube')[50])
        self.assertEqual('w', result.get('cube')[51])
        self.assertEqual('w', result.get('cube')[52])
        self.assertEqual('w', result.get('cube')[53])
        self.assertEqual(result.get('cube')[4], result.get('cube')[6])
        self.assertEqual(result.get('cube')[4], result.get('cube')[7])
        self.assertEqual(result.get('cube')[4], result.get('cube')[8])
        self.assertEqual(result.get('cube')[13], result.get('cube')[15])
        self.assertEqual(result.get('cube')[13], result.get('cube')[16])
        self.assertEqual(result.get('cube')[13], result.get('cube')[17])
        self.assertEqual(result.get('cube')[22], result.get('cube')[24])
        self.assertEqual(result.get('cube')[22], result.get('cube')[25])
        self.assertEqual(result.get('cube')[22], result.get('cube')[26])
        self.assertEqual(result.get('cube')[31], result.get('cube')[33])
        self.assertEqual(result.get('cube')[31], result.get('cube')[34])
        self.assertEqual(result.get('cube')[31], result.get('cube')[35])
        

    def test190_solve_middlelayer(self):
        encodedCube = 'yobgbyborwyygrbywogwrogybrowybrorwwrgrooybowrygggwbgbw'
        parms = {}
        parms['cube'] = encodedCube
        dirs = solve(parms)
        parms['dir'] = dirs['solution']
        result = rotate(parms)
        self.assertEqual('w', result.get('cube')[45])
        self.assertEqual('w', result.get('cube')[46])
        self.assertEqual('w', result.get('cube')[47])
        self.assertEqual('w', result.get('cube')[48])
        self.assertEqual('w', result.get('cube')[50])
        self.assertEqual('w', result.get('cube')[51])
        self.assertEqual('w', result.get('cube')[52])
        self.assertEqual('w', result.get('cube')[53])
        self.assertEqual(result.get('cube')[4], result.get('cube')[3])
        self.assertEqual(result.get('cube')[4], result.get('cube')[5])
        self.assertEqual(result.get('cube')[4], result.get('cube')[6])
        self.assertEqual(result.get('cube')[4], result.get('cube')[7])
        self.assertEqual(result.get('cube')[4], result.get('cube')[8])
        self.assertEqual(result.get('cube')[13], result.get('cube')[12])
        self.assertEqual(result.get('cube')[13], result.get('cube')[14])
        self.assertEqual(result.get('cube')[13], result.get('cube')[15])
        self.assertEqual(result.get('cube')[13], result.get('cube')[16])
        self.assertEqual(result.get('cube')[13], result.get('cube')[17])
        self.assertEqual(result.get('cube')[22], result.get('cube')[21])
        self.assertEqual(result.get('cube')[22], result.get('cube')[23])
        self.assertEqual(result.get('cube')[22], result.get('cube')[24])
        self.assertEqual(result.get('cube')[22], result.get('cube')[25])
        self.assertEqual(result.get('cube')[22], result.get('cube')[26])
        self.assertEqual(result.get('cube')[31], result.get('cube')[30])
        self.assertEqual(result.get('cube')[31], result.get('cube')[32])
        self.assertEqual(result.get('cube')[31], result.get('cube')[33])
        self.assertEqual(result.get('cube')[31], result.get('cube')[34])
        self.assertEqual(result.get('cube')[31], result.get('cube')[35])
        
    def test200_solve_middlelayer(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        parms = {}
        parms['cube'] = encodedCube
        dirs = solve(parms)
        parms['dir'] = dirs['solution']
        result = rotate(parms)
        self.assertEqual('w', result.get('cube')[45])
        self.assertEqual('w', result.get('cube')[46])
        self.assertEqual('w', result.get('cube')[47])
        self.assertEqual('w', result.get('cube')[48])
        self.assertEqual('w', result.get('cube')[50])
        self.assertEqual('w', result.get('cube')[51])
        self.assertEqual('w', result.get('cube')[52])
        self.assertEqual('w', result.get('cube')[53])
        self.assertEqual(result.get('cube')[4], result.get('cube')[3])
        self.assertEqual(result.get('cube')[4], result.get('cube')[5])
        self.assertEqual(result.get('cube')[4], result.get('cube')[6])
        self.assertEqual(result.get('cube')[4], result.get('cube')[7])
        self.assertEqual(result.get('cube')[4], result.get('cube')[8])
        self.assertEqual(result.get('cube')[13], result.get('cube')[12])
        self.assertEqual(result.get('cube')[13], result.get('cube')[14])
        self.assertEqual(result.get('cube')[13], result.get('cube')[15])
        self.assertEqual(result.get('cube')[13], result.get('cube')[16])
        self.assertEqual(result.get('cube')[13], result.get('cube')[17])
        self.assertEqual(result.get('cube')[22], result.get('cube')[21])
        self.assertEqual(result.get('cube')[22], result.get('cube')[23])
        self.assertEqual(result.get('cube')[22], result.get('cube')[24])
        self.assertEqual(result.get('cube')[22], result.get('cube')[25])
        self.assertEqual(result.get('cube')[22], result.get('cube')[26])
        self.assertEqual(result.get('cube')[31], result.get('cube')[30])
        self.assertEqual(result.get('cube')[31], result.get('cube')[32])
        self.assertEqual(result.get('cube')[31], result.get('cube')[33])
        self.assertEqual(result.get('cube')[31], result.get('cube')[34])
        self.assertEqual(result.get('cube')[31], result.get('cube')[35])
        
def test220_solve_middlelayer(self):
        encodedCube = 'rooybwryggbbgrwygorgorgobwwbbyyorbwwyoyryygbwggoowrrbw'
        parms = {}
        parms['cube'] = encodedCube
        dirs = solve(parms)
        parms['dir'] = dirs['solution']
        result = rotate(parms)
        print(result.get('cube'))
        self.assertEqual('w', result.get('cube')[45])
        self.assertEqual('w', result.get('cube')[46])
        self.assertEqual('w', result.get('cube')[47])
        self.assertEqual('w', result.get('cube')[48])
        self.assertEqual('w', result.get('cube')[50])
        self.assertEqual('w', result.get('cube')[51])
        self.assertEqual('w', result.get('cube')[52])
        self.assertEqual('w', result.get('cube')[53])
        self.assertEqual(result.get('cube')[4], result.get('cube')[3])
        self.assertEqual(result.get('cube')[4], result.get('cube')[5])
        self.assertEqual(result.get('cube')[4], result.get('cube')[6])
        self.assertEqual(result.get('cube')[4], result.get('cube')[7])
        self.assertEqual(result.get('cube')[4], result.get('cube')[8])
        self.assertEqual(result.get('cube')[13], result.get('cube')[12])
        self.assertEqual(result.get('cube')[13], result.get('cube')[14])
        self.assertEqual(result.get('cube')[13], result.get('cube')[15])
        self.assertEqual(result.get('cube')[13], result.get('cube')[16])
        self.assertEqual(result.get('cube')[13], result.get('cube')[17])
        self.assertEqual(result.get('cube')[22], result.get('cube')[21])
        self.assertEqual(result.get('cube')[22], result.get('cube')[23])
        self.assertEqual(result.get('cube')[22], result.get('cube')[24])
        self.assertEqual(result.get('cube')[22], result.get('cube')[25])
        self.assertEqual(result.get('cube')[22], result.get('cube')[26])
        self.assertEqual(result.get('cube')[31], result.get('cube')[30])
        self.assertEqual(result.get('cube')[31], result.get('cube')[32])
        self.assertEqual(result.get('cube')[31], result.get('cube')[33])
        self.assertEqual(result.get('cube')[31], result.get('cube')[34])
        self.assertEqual(result.get('cube')[31], result.get('cube')[35])        
        
 