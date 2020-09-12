#unit test
import unittest
import prime number
class primenumber(unittest.testcase):
    def testprime(self):
        number=32
        result=prime.isprime(number)
        self.assertequals(result,false)
    def testprimenum(self):
        num=199
        res=prime.isprime(number)
        self.assertequals(result,true)
if __name=="__main__":
    unttest.main()
        
