import tcg.*;

// DO ALL YOUR TESTING IN HERE
public class Testing {
    public static void main(String[] args) throws Exception {
        try {
            Ability ability1 = new Ability();
            Ability ability2 = new Ability("BigBalls", "notball", 2, 230);
            Ability[] abilityList = {ability1, ability2};
            CharacterCard charCard1 = new CharacterCard("BallMan", "ball", 330, abilityList);
            System.out.println(charCard1);
        }
        catch (IllegalArgumentException e) {
            System.out.println("Illegal Arg caught");
            throw e;
        }
        catch (IncompatiblePowerException e) {
            System.out.println(e);
        }
    }
}
