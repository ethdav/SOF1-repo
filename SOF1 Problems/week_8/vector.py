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
     
    def dim(self):
        if isinstance(self._vector, list):
            return len(self._vector)
        else:
            return 0
    
def main():
    vector = Vector([1.0,3.5,5.0])
    print(vector.dim())

if __name__ == "__main__":
    main()