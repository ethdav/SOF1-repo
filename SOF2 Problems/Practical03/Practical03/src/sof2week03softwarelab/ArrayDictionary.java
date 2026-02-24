package sof2week03softwarelab;

public class ArrayDictionary {
    Integer[] keys;
    String[] values;

    public ArrayDictionary() {
        keys = new Integer[100];
        values = new String[100];
    }

    public ArrayDictionary(int size) {
        keys = new Integer[size];
        values = new String[size];
    }

    public String toString() {
        String newString = "{";
        for (int i = 0; i < this.keys.length; i++) {
            newString += this.keys[i] + ":" + this.values[i];
            if (i < this.keys.length - 1) {
                newString += ", ";
            }
        }
        return newString + "}";
    }

    public int size() {
        return this.keys.length;
    }

    private void grow() {
        Integer[] tempInts = new Integer[this.keys.length * 2];
        String[] tempStrs = new String[this.values.length * 2];
    }

    public String put(Integer key, String value) {
        boolean keyFound = false;
        for (int i = 0; i < this.size(); i++) {
            if (key == this.keys[i]) {
                keyFound = true;
                break;
            }
        }
        if (keyFound) {

        }
    }

    public static void main(String[] args) {
        ArrayDictionary arrayDict = new ArrayDictionary(10);
        System.out.println(arrayDict.toString());
    }
}
