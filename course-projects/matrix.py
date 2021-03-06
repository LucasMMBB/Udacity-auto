import math
from math import sqrt
import numbers
from copy import copy


# Helper methods
def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for _ in range(height)]
        return Matrix(g)
def zeroeslist(height, width):
        """
        Create a list of zeroes
        """
        return [[0.0 for _ in range(width)] for _ in range(height)]
def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])
        self.EMPTY = 0
    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            return self.g[0][0]
        elif self.h == 2:
            return self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sm = 0
        for i in range(self.h):
            sm += self.g[i][i]

        return sm

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        # TODO - your code here
        
        if self.h == 1:
        	k = float(self.g[0][0])
        	if k == 0:
        		raise(ValueError, "This Matrix is not inversed")
        	return Matrix([[1 / k]])
        k = float(self.g[0][0]*self.g[1][1] - self.g[1][0]*self.g[0][1])
        
        if k == 0:
        	raise(ValueError, "This Matrix is singular")

        k = 1 / k
        tmp = zeroeslist(2, 2)
        tmp[0][0] = k*self.g[1][1]
        tmp[1][1] = k*self.g[0][0]
        tmp[1][0] = -k*self.g[1][0]
        tmp[0][1] = -k*self.g[0][1]

        return Matrix(tmp)


    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        m = self.g
        return Matrix([[m[a][b] for a in range(self.h)] for b in range(self.w)])
        

    def is_square(self):
        return self.h == self.w


    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        tmp = zeroeslist(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                tmp[i][j] = self.g[i][j] + other.g[i][j]
        return Matrix(tmp)


    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        if self.h == self.EMPTY and self.w == self.EMPTY:
            return Matrix(self.g)
        
        tmp = zeroeslist(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                tmp[i][j] = -float(self.g[i][j])

        return Matrix(tmp)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subbed if the dimensions are the same")
        
        tmp = zeroeslist(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                tmp[i][j] = self.g[i][j] - other.g[i][j]

        return Matrix(tmp)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if isinstance(other, int):
            tmp = zeroeslist(self.h, self.w)
            for i in range(self.h):
                for j in range(self.w):
                    tmp = self.g[i][j] * other
            return tmp

        if self.w == other.h:
            tmp = zeroeslist(self.h, other.w)

            for i in range(self.h):
                for j in range(other.w):
                    p = self.w
                    tmpSum = 0
                    for k in range(p):
                        tmpSum += self.g[i][k]*other.g[k][j]
                    tmp[i][j] = tmpSum
            return Matrix(tmp)
        else:
            raise(ValueError, "Matrixes are not compatible")

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #   
            # TODO - your code here
            #
            tmp = zeroeslist(self.h, self.w)
            for i in range(self.h):
                for j in range(self.w):
                    tmp[i][j] = float(other) * self.g[i][j]
            return Matrix(tmp)