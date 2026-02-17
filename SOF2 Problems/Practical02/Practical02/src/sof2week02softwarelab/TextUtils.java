package sof2week02softwarelab;

import java.util.ArrayList;

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
        ArrayList<String> wordArray = new ArrayList<String>();
        text = text.strip();
        String word = "";
        for (int i = 0; i <= text.length(); i++) {
            if (i == text.length() || text.charAt(i) == ' ') { 
                if (word != "") {
                   wordArray.add(word); 
                }
                word = "";
            }
            else {
                word += text.charAt(i);
            }
        }
        String[] splitText = new String[wordArray.size()];
        for (int i = 0; i < wordArray.size(); i++) {
            splitText[i] = wordArray.get(i);
        }
        return splitText;
    }

    public static String[] split(String text, String separators) {
        char[] textArray = text.toCharArray();
        char[] sepArray = separators.toCharArray();
        String textWhite = "";
        for (char letter : textArray) {
            boolean sepFound = false;
            for (char separator : sepArray) {
                if (letter == separator) {
                    sepFound = true;
                }
            }
            if (sepFound == true) {
                textWhite += " ";
            }
            else {
                textWhite += letter;
            }
        }
        return split(textWhite);
    }

    public static void main(String[] args) {
        // String binString = "10001011";
        // System.out.println(toBase10(binString));
        String seps = ".,?!/";
        String text = "This? This is not, a test!";
        String[] splitText = split(text, seps);
        for (String word : splitText) {
            System.out.println(word);
        }
    }
}
