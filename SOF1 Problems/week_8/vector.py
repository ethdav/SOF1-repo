import copy

class Vector:
    def __init__(self, vector_list=None):
        self._vector = copy.copy(vector_list)

    def __str__(self):
        if self._vector is None:
            return "<>"
        elif isinstance(self._vector ,list):
            out = "<"
            for item in self._vector:
                out += str(item) + ", "
            out = out[:-2]
            return out + ">"
        
    def __eq__(self, other):
        if isinstance(other, Vector) is False:
            raise TypeError("Given item is not a vector")
        elif self.size() != other.size():
            raise ValueError("Vectors not of same length")
        else:
            for index in range(len(self._vector)):
                if self._vector[index] != other._vector[index]:
                    return False
            return True
     
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
        if not isinstance(index, int) or not isinstance(value, float):
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
    
    def add(self, other):
        if isinstance(other, Vector) is False:
            raise TypeError("Given item is not a vector")
        elif self.size() != other.size():
            raise ValueError("Vectors not of same length")
        else:
            added_list = []
            for item in range(len(self._vector)):
                added_list.append(self._vector[item] + other._vector[item])
            return Vector(added_list)

def main():
    vector1 = Vector([1.0,3.5,5.0])
    vector2 = Vector([1.0,3.5,5.0])
    print(vector1 is vector2)

if __name__ == "__main__":
    main()