import unittest
from Comparisons import *
from TruthTable import *


class TestComparisions(unittest.TestCase):

    def test_init(self):
        true,false= Variable('x',True), Variable('y',False)
        self.assertTrue(true.value)
        self.assertFalse(false.value)
    
    def test_constant(self):
        true,false= Variable('x',True), Variable('y',False)
        proposition1,proposition2 = Constant(true),Constant(false)
        self.assertTrue(proposition1.value)
        self.assertFalse(proposition2.value)
    
    def test_negation(self):
        true,false= Variable('x',True), Variable('y',False)
        proposition1,proposition2 = Negation(true),Negation(false)
        self.assertFalse(proposition1)
        self.assertTrue(proposition2)

    def test_conjunction(self):
        true,false= Variable('x',True), Variable('y',False)
        proposition1,proposition2,proposition3 = Conjunction(true,true),Conjunction(true,false),Conjunction(false,false)
        self.assertTrue(proposition1)
        self.assertFalse(proposition2)
        self.assertFalse(proposition3)

    def test_disjunction(self):
        true,false= Variable('x',True), Variable('y',False)
        proposition1,proposition2,proposition3 = Disjunction(true,true),Disjunction(true,false),Disjunction(false,false)
        self.assertTrue(proposition1)
        self.assertTrue(proposition2)
        self.assertFalse(proposition3)

    def test_conditional(self):
        true,false= Variable('x',True), Variable('y',False)
        proposition1,proposition2,proposition3,proposition4 = Conditional(true,true),Conditional(true,false),Conditional(false,false),Conditional(false,true)
        self.assertTrue(proposition1)
        self.assertFalse(proposition2)
        self.assertTrue(proposition3)
        self.assertTrue(proposition4)

    def test_biconditional(self):
        true,false= Variable('x',True), Variable('y',False)
        proposition1,proposition2,proposition3,proposition4 = Biconditional(true,true),Biconditional(true,false),Biconditional(false,false),Biconditional(false,true)
        self.assertTrue(proposition1)
        self.assertFalse(proposition2)
        self.assertTrue(proposition3)
        self.assertFalse(proposition4)
    
    def test_compound_proposition(self):
        true,false = Variable('x'),Variable('y',False)
        # ((x <-> y) ^ (~y v (x -> z)))

        self.assertTrue(Conjunction(Biconditional(true, true), Disjunction(Negation(false), (Conditional(true , true)))))
        self.assertTrue(Conjunction(Biconditional(false, false), Disjunction(Negation(false), (Conditional(false , false)))))
        self.assertFalse(Conjunction(Biconditional(true, false), Disjunction(Negation(true), (Conditional(true , true)))))
        self.assertTrue(Conjunction(Biconditional(false, false), Disjunction(Negation(true), (Conditional(true , true)))))
        self.assertTrue(Conjunction(Biconditional(true, true), Disjunction(Negation(true), (Conditional(true , true)))))
        self.assertFalse(Conjunction(Biconditional(true, true), Disjunction(Negation(true), (Conditional(true , false)))))
        self.assertTrue(Conjunction(Biconditional(false, false), Disjunction(Negation(true), (Conditional(false , true)))))

    def test_basic_truthtable(self):

        # (p -> q) , (q -> r) : (p -> r) --> VALID
        p,q,r = Variable('p'),Variable('q'),Variable('r')
        variables = [p,q,r]
        premises = [Conditional(p,q),Conditional(q,r)]
        conclusion = [Conditional(p,r)]
        tt = TruthTable(variables,premises,conclusion)
        self.assertEqual(tt.validate(),'This argument is Valid')
        print('\n')
        print(tt.print_table())

        # (p -> q) , q : p --> INVALID
        p,q = Variable('p'),Variable('q')
        variables = [p,q]
        premises = [Conditional(p,q),Constant(q)]
        conclusion = [Constant(p)]
        tt = TruthTable(variables,premises,conclusion)
        self.assertEqual(tt.validate(),'This argument is Invalid')
        print('\n')
        print(tt.print_table())


    def test_complex_truthtable(self):

        # ((p -> q) ^ r) , (~q v r) : (p <-> (q <-> r)) --> INVALID
        p,q,r = Variable('p'),Variable('q'),Variable('r')
        variables = [p,q,r]
        premises = [Conjunction(Conditional(p,q),r),Disjunction(Negation(q),r)]
        conclusion = [Biconditional(p,Biconditional(q,r))]
        tt = TruthTable(variables,premises,conclusion)
        self.assertEqual(tt.validate(),'This argument is Invalid')
        print('\n')
        print(tt.print_table())


unittest.main()