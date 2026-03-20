package tools;

public class BasicTallyCounter implements ITallyCounter {
    int counter, digits;

    public BasicTallyCounter() {
        counter = 0;
        digits = 3;
    }

    @Override
    public void increment() throws InvalidOperationException {
        if (String.valueOf(counter + 1).length() <= digits) {
            counter++;
        }
        else {
            throw new InvalidOperationException();
        }
    }

    @Override
    public void reset() {
        counter = 0;
    }

    @Override
    public int read() {
        return counter;
    }

    public String toString() {
        return String.format("%03d", counter);
    }
}
