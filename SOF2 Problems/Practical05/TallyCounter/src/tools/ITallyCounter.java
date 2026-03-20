package tools;

public interface ITallyCounter {
    public void increment() throws InvalidOperationException;
    public void reset();
    public int read();
}
