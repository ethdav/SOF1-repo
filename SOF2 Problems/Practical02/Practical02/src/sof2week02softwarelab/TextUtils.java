package sof2week02softwarelab;

import java.util.ArrayList;
import java.util.Arrays;

public class TextUtils {
    
    public static int toBase10(String binary) {
        int base10 = 0;
        for (int i = 0; i < binary.length(); i++) {
            int bit = binary.charAt(i) - '0';
            base10 += bit * Math.pow(2, binary.length() - i - 1);
        }
        return base10;
    }

    public static String[] split(String text) {
        return split(text, " ");
    }

    public static String[] split(String text, String separators) {
        ArrayList<String> wordArray = new ArrayList<String>();
        text = text.strip();
        char[] textArray = text.toCharArray();
        char[] sepArray = separators.toCharArray();
        String word = "";
        for (int i = 0; i < textArray.length; i++) {
            boolean sepFound = false;
            for (char separator : sepArray) {
                if (textArray[i] == separator) {
                    sepFound = true;
                }
            }
            if (sepFound == true) {
                if (word != "") {
                    wordArray.add(word);
                    word = "";
                }
            }
            else {
                word += textArray[i];
            }
            if (i == textArray.length - 1 && word != "") {
                wordArray.add(word);
            }
        }
        String[] splitText = new String[wordArray.size()];
        for (int i = 0; i < wordArray.size(); i++) {
            splitText[i] = wordArray.get(i);
        }
        return splitText;
    }

    public static int[][] rasterise(int[] data, int width) {
        if (width == 0 || (data.length % width) != 0) {
            return null;
        }
        int height = data.length / width;
        int[][] newArray = new int[height][width];
        for (int i = 0; i < data.length; i++) {
            int heightI = Math.floorDiv(i, width);
            newArray[heightI][i % width] = data[i];
        }
        return newArray;
    }

    public static void main(String[] args) {
        // String binString = "10001011";
        // System.out.println(toBase10(binString));
        // String seps = " .,!?/";
        // String text = "Tis but a scratch";
        // String[] splitText = split(text);
        // for (String word : splitText) {
        //     System.out.println(word);
        // }
        int[] oneDArray = {0,1,2,3,4,5,6,7,8,9};
        String arrayOutput = Arrays.deepToString(rasterise(oneDArray, 0));
        System.out.println(arrayOutput);
    }
}
