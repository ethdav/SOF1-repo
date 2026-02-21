package sof2week03softwarelab;

public class Vector {
    private double[] vector;

    public Vector(double[] v) {
        vector = new double[v.length];
        vector = v.clone();
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

    public static void main() {
        double[] test = {1.0, 3.7, 2.3, 5.1};
        Vector vec1 = new Vector(test);
        Vector vec2 = vec1.scalarProduct(2.0);
        System.out.println(vec1.toString());
        System.out.println(vec2.toString());
    }
}
