package tcg;

public class IncompatiblePowerException extends Exception{
    protected String power1, power2;
    private String message;

    public IncompatiblePowerException(String message, String power1, String power2) {
        this.message = message;
        this.power1 = power1;
        this.power2 = power2;
    }

    @Override
    public String toString() {
        return message + power1 + "," + power2;
    }
}
