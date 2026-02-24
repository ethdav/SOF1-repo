package sof2week03softwarelab;

public class Vector {
    public double[] vector;

    public Vector(double[] v) {
        vector = new double[v.length];
        vector = v.clone();
    }

    public boolean equals(Object other) {
        if (other == null) {
            return false;
        }
        if (!(other instanceof Vector)) {
            return false;
        }
        Vector otherVector = (Vector) other;
        if (this.size() != otherVector.size()) {
            return false;
        }
        for (int i = 0; i < this.size(); i++) {
            if (this.vector[i] != otherVector.vector[i]) {
                return false;
            }
        }
        return true;
    }
    
    public String toString() {
        String newString = "[";
        for (int i = 0; i < vector.length; i++) {
            newString += vector[i];
            if (i < vector.length - 1) {
                newString += ", ";
            }
        }
        newString += "]";
        return newString;
    }

    public int size() {
        return vector.length;
    }

    public Double get(int index) {
        return (Double) vector[index];
    }

    public Double set(int index, double value) {
        double old = vector[index];
        vector[index] = value;
        return (Double) old;
    }

    public Vector scalarProduct(double scalar) {
        double[] tempVector = new double[vector.length];
        for (int i = 0; i < tempVector.length; i++) {
            tempVector[i] = vector[i] * scalar;
        }
        Vector scalarProd = new Vector(tempVector);
        return scalarProd;
    }

    public Vector add(Vector other) {
        if (this.size() != other.size()) {
            return null;
        }
        double[] tempArray = new double[this.size()];
        for (int i = 0; i < tempArray.length; i++) {
            tempArray[i] = this.get(i) + other.get(i);
        }
        Vector sumVector = new Vector(tempArray);
        return sumVector;
    }

    public static void main() {
        double[] test = {1.0, 3.7, 2.3, 5.1};
        Vector vec1 = new Vector(test);
        Vector vec2 = vec1.scalarProduct(1.0);
        System.out.println(vec1.toString());
        System.out.println(vec2.toString());
        System.out.println(vec1.equals(vec2));
    }
}
