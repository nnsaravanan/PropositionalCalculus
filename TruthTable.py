from itertools import product
import pandas as pd

class TruthTable:
    '''class to create a truth table and validate a premise and conclusion'''

    def __init__(self,vars=[],premises = [],conclusion=[]):
        '''initalizes function by creating a head outline for the table'''

        self.vars = vars
        self.premises = premises
        self.conclusion = conclusion
        self.table = list()
        self.critical_rows = list()
        self.head = self.vars+self.premises+self.conclusion
        
    def run_table(self):
        '''creates a raw truth table'''
        
        table_vars = [list(x) for x in list(product([True, False], repeat=len(self.vars)))]
        self.table+=table_vars
        
        for row in self.table:
            prem_row = list()
            conc_row = list()

            for ind in range(len(row)):
                self.vars[ind].value = row[ind]
            for premise in self.premises:
                prem_row.append(premise.eval())
            for conclusion in self.conclusion:
                conc_row.append(conclusion.eval())
            row += prem_row+conc_row
            if all(prem_row):
                self.critical_rows+=conc_row
    
    def validate(self):
        '''creates a raw truth table and returns whether the premise and conclusion are valid'''

        self.run_table()
        if all(self.critical_rows):
            return "This argument is Valid"
        return "This argument is Invalid"
                
    def print_table(self):
        '''prints table as a pandas dataframe to be read easier'''

        map_dict = {True:'T',False:'F'}
        printable_list = list()
        for row in self.table:
            printable_list.append(list(map(lambda x: map_dict[x],row)))

        truth_table = pd.DataFrame(printable_list,columns= self.head)
        return truth_table
        
        