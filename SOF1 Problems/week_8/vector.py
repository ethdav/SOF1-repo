import copy

class Vector:
    def __init__(self, *vectors):
        self._vector = []
        if len(vectors) < 1:
            pass
        elif isinstance(vectors[0], list):
            self._vector = copy.copy(vectors[0])
        else:
            for item in vectors:
                if isinstance(item, (int, float)):
                    self._vector.append(round(item, 1))
                else:
                    raise TypeError("Invalid data type")

    def __str__(self):
        if self.size() == 0:
            return "<>"
        elif isinstance(self._vector ,list):
            out = "<"
            for item in self._vector:
                out += str(round(float(item), 1)) + ", "
            out = out[:-2]
            return out + ">"
        
    def __eq__(self, other):
        if isinstance(other, Vector) is False:
            return False
        elif self.size() != other.size():
            return False
        else:
            for index in range(len(self._vector)):
                if self._vector[index] != other._vector[index]:
                    return False
            return True
        
    def __ne__(self, other):
        return not self == other
    
    def __add__(self, other):
        if isinstance(other, Vector) is False:
            raise TypeError(f"Cannot add type vector to type:{type(other)}")
        elif self.size() != other.size():
            raise ValueError("Vectors not of same length")
        else:
            added_list = []
            for item in range(len(self._vector)):
                added_list.append(self._vector[item] + other._vector[item])
            return Vector(added_list)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([x*other for x in self._vector])
        else:
            raise TypeError(f"Error: invalid type:{type(other)}")
        
    def __rmul__(self, other):
        return self * other
    
    def __iadd__(self, other):
        return self + other

    def __imul__(self, other):
        return self * other
    
    def __getitem__(self, index):
        return self._vector[index]
    
    def __setitem__(self, index, value):
        if isinstance(value, (int, float)):
            self._vector[index] = round(value, 1)
        else:
            raise TypeError(f"Value is invalid type:{type(value)}")
        
    def __delitem__(self, index):
        self._vector.pop(index)
     
    def dim(self):
        if isinstance(self._vector, list):
            return len(self._vector)
        else:
            return 0

    def get(self, index):
        if isinstance(index, int) and index < len(self._vector):
            return self._vector[index]
        elif index >= len(self._vector):
            raise IndexError("Index out of range")
        else:
            raise TypeError("I was too lazy to write other exceptions")
    
    def set(self, index, value):
        if not isinstance(index, int) or not isinstance(value, (int, float)):
            raise TypeError("Type Error: incorrect index or value type")
        elif index >= len(self._vector):
            raise IndexError("Index out of range")
        else:
            self._vector[index] = round(value, 1)

    def size(self):
        return len(self._vector)

    def scalar_product(self, scalar):
        scalar_list = []
        for item in self._vector:
            scalar_list.append(item * scalar)
        return Vector(scalar_list)

def main():
    vector1 = Vector([1,3,5])
    vector2 = Vector(1,3,5)
    print(vector1 == vector2)

if __name__ == "__main__":
    main()