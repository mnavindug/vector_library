class Vector2D:
    '''
    This is a class for the basic vector operations on the 2D plane.
    
    Addition, Subtraction, Cross product, Dot product and Norm operations are available
    '''

    def __init__(self,x,y):
        '''Initializes the vector object with its components.'''
        self.x = x
        self.y = y

    def __add__(self,other):
        '''Returns the addition of 2 vector objects in the 2D plane.'''
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        '''Returns the subtraction of 2 vector objects in the 2D plane.'''
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self,other):   
        '''Returns the cross product of 2 vector objects in the 2D plane.

           Use * operator for this operation.'''
        pass
    
    def __repr__(self):
        '''Returns the vector object in the standard notation.'''
        return f'<{self.x},{self.y}>'
    
    def __len__(self):
        '''Returns the square of the norm.'''
        return self.x**2 + self.y**2
    
    def __matmul__(self, other):       
        '''Returns the dot product of 2 vector objects in the 2D plane.

           Use the @ symbol for this operation.'''
        return self.x* other.x + self.y * other.y
    
    def norm(self):
        '''Returns the norm of the vector object.'''
        mag_squared = len(self)
        return mag_squared**0.5



class Vector3D:
    '''
    This is a class for the basic vector operations on the 3D plane.
    
    Addition, Subtraction, Cross product, Dot product and Norm operations are available
    '''


    def __init__(self,x,y,z):
        '''Initializes the vector object with its components.'''
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        '''Returns the addition of 2 vector objects in the 3D plane.'''
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self,other):
        '''Returns the subrtraction of 2 vector objects in the 3D plane.'''
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self,other):        
        '''Returns the cross product of 2 vector objects in the 3D plane.

           Use * operator for this operation.'''
        return Vector3D(self.y * other.z - self.z * other.y, -1 * (self.x * other.z - self.z * other.x), self.x * other.y - self.y * other.x)
    
    def __repr__(self):
        '''Returns the vector object in the standard notation.'''
        return f'<{self.x},{self.y},{self.z}>'
    
    def __len__(self):
        '''Returns the square of the norm.'''
        return self.x**2 + self.y**2 + self.z**2
    
    def __matmul__(self, other):
        '''Returns the dot product of 2 vector objects in the 3D plane.

           Use the @ symbol for this operation.'''
        return self.x* other.x + self.y * other.y + self.z*other.z
    
    def norm(self):
        '''Returns the norm of the vector object.'''
        mag_squared = len(self)
        return mag_squared**0.5
    

    

 

