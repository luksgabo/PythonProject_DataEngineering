def area_of_rectangle(length, breadth):
    '''Function that takes rectangle dimensions (length and breadth) and return area'''
    area = length*breadth
    if area>0:
        return area
    else:
        return ValueError('values should be positive!')

def area_of_circle(radius):
    '''Function that takes circle radius and return area'''
    PI = 3.1415926
    return PI*(radius**2)
