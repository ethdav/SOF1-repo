package tools;

public class TallyCounter {
    int counter, digits;

    public TallyCounter() {
        counter = 0;
        digits = 3;
    }

    public TallyCounter(int maxDigits) throws InvalidOperationException {
        if (maxDigits < 3) {
            throw new InvalidOperationException();
        }
        counter = 0;
        digits = maxDigits;
    }

    public void increment() throws InvalidOperationException {
        if (String.valueOf(counter + 1).length() <= digits) {
            counter++;
        }
        else {
            throw new InvalidOperationException();
        }
    }

    public void decrement() throws InvalidOperationException {
        if (counter != 0) {
            counter--;
        }
        else {
            throw new InvalidOperationException();
        }
    }

    public int read() {
        return counter;
    }

    public void reset() {
        counter = 0;
    }

    public String toString() {
        return String.format("%03d", counter);
    }
}
