package tools;

public class MainApp {
    public static void main(String[] args) {
        try {
            TallyCounter tallyCount = new TallyCounter();
            for (int i = 0; i < 300; i++) {
                tallyCount.increment();
            }
            for (int i = 0; i < 300; i++) {
                tallyCount.decrement();
            }
            System.out.println(tallyCount.toString());
        } catch (InvalidOperationException e) {
            System.out.println("Counter out of bounds.");
        }
        
    }
}
