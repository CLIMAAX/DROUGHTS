"""
Data Envelopment Analysis implementation

Sources:
Sherman & Zhu (2006) Service Productivity Management, Improving Service Performance using Data Envelopment Analysis (DEA) [Chapter 2]
ISBN: 978-0-387-33211-6
http://deazone.com/en/resources/tutorial

"""

import numpy as np
from scipy.optimize import fmin_slsqp


class DEA(object):

    def __init__(self, inputs, outputs, loud):
        """
        Initialize the DEA object with input data
        n = number of entities (observations)
        m = number of inputs (variables, features)
        r = number of outputs
        :param inputs: inputs, n x m numpy array
        :param outputs: outputs, n x r numpy array
        :return: self
        """

        # supplied data
        self.inputs = inputs
        self.outputs = outputs

        # parameters
        self.n = inputs.shape[0]
        self.m = inputs.shape[1]
        self.r = outputs.shape[1]
	

        # iterators
        self.unit_ = range(self.n)
        self.input_ = range(self.m)
        self.output_ = range(self.r)

        # result arrays
        self.output_w = np.zeros((self.r, 1), dtype=np.float64)  # output weights
        self.input_w = np.zeros((self.m, 1), dtype=np.float64)  # input weights
        self.lambdas = np.zeros((self.n, 1), dtype=np.float64)  # unit efficiencies
        self.efficiency = np.zeros_like(self.lambdas)  # thetas

        # names
        self.names = []
        
        # flags
        self.loud = loud
    def __efficiency(self, unit):
        """
        Efficiency function with already computed weights
        :param unit: which unit to compute for
        :return: efficiency
        """

        # compute efficiency
        denominator = np.dot(self.inputs, self.input_w)
        numerator = np.dot(self.outputs, self.output_w)

        return (numerator/denominator)[unit]

    def __target(self, x, unit):
        """
        Theta target function for one unit
        :param x: combined weights
        :param unit: which production unit to compute
        :return: theta
        """
        in_w, out_w, lambdas = x[:self.m], x[self.m:(self.m+self.r)], x[(self.m+self.r):]  # unroll the weights
        denominator = np.dot(self.inputs[unit], in_w)
        numerator = np.dot(self.outputs[unit], out_w)

        return numerator/denominator

    def __constraints(self, x, unit):
        """
        Constraints for optimization for one unit
        :param x: combined weights
        :param unit: which production unit to compute
        :return: array of constraints
        """

        in_w, out_w, lambdas = x[:self.m], x[self.m:(self.m+self.r)], x[(self.m+self.r):]  # unroll the weights
        constr = []  # init the constraint array

        # for each input, lambdas with inputs
        for input in self.input_:
            t = self.__target(x, unit)
            lhs = np.dot(self.inputs[:, input], lambdas)
            cons = t*self.inputs[unit, input] - lhs
            constr.append(cons)

        # for each output, lambdas with outputs
        for output in self.output_:
            lhs = np.dot(self.outputs[:, output], lambdas)
            cons = lhs - self.outputs[unit, output]
            constr.append(cons)

        # for each unit
        for u in self.unit_:
            constr.append(lambdas[u])

        return np.array(constr)

    def __optimize(self):
        """
        Optimization of the DEA model
        Use: http://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.optimize.linprog.html
        A = coefficients in the constraints
        b = rhs of constraints
        c = coefficients of the target function
        :return:
        """
        d0 = self.m + self.r + self.n
        # iterate over units
        #https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin_slsqp.html
        iprint = 0
        if self.loud:
            iprint = 1
        for unit in self.unit_:
            # weights
    
            imode = 1
            counter = 0
            limit = 10
            while imode != 0:
                x0 = np.random.rand(d0) - 0.5
                x0, fx, its, imode, smode = fmin_slsqp(self.__target, x0, f_ieqcons=self.__constraints,\
                    args=(unit,), iprint = iprint, full_output = True)
                counter += 1
                if counter >= limit:
                    raise RuntimeError('DEA optimizer exceeded the maximum number of iterations')
                
            # unroll weights
            self.input_w, self.output_w, self.lambdas = x0[:self.m], x0[self.m:(self.m+self.r)], x0[(self.m+self.r):]
            self.efficiency[unit] = self.__efficiency(unit)

    def name_units(self, names):
        """
        Provide names for units for presentation purposes
        :param names: a list of names, equal in length to the number of units
        :return: nothing
        """

        assert(self.n == len(names))

        self.names = names

    def fit(self):
        """
        Optimize the dataset, generate basic table
        :return: table
        """

        self.__optimize()  # optimize
        
        efficiencies = []
        
        for n, eff in enumerate(self.efficiency):
            efficiencies.append(round(eff[0], 3))
        
        return efficiencies
        '''
        print("Final thetas for each unit:\n")
		print("---------------------------\n")
		for n, eff in enumerate(self.efficiency):
			if len(self.names) > 0:
           	     name = "Unit %s" % self.names[n]
	            else:
       	         name = "Unit %d" % (n+1)
        	    print("%s theta: %.4f" % (name, eff))
	            print("\n")
            print("---------------------------\n")
        '''

'''
if __name__ == "__main__":
    X = np.array([
        [20., 300.],
        [30., 200.],
        [40., 100.],
        [20., 200.],
        [10., 400.]
    ])
    y = np.array([
        [1000.],
        [1000.],
        [1000.],
        [1000.],
        [1000.]
    ])
    names = [
        'Bratislava',
        'Zilina',
        'Kosice',
        'Presov',
        'Poprad'
    ]
    dea = DEA(X,y)
    dea.name_units(names)
    dea.fit()
'''