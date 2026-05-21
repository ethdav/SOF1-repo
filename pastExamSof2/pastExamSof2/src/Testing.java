import tcg.*;

// DO ALL YOUR TESTING IN HERE
public class Testing {
    public static void main(String[] args) throws Exception {
        try {
            Ability ability1 = new Ability();
            Ability ability2 = new Ability("BigBalls", "ball", 2, 230);
            Ability[] abilityList = {ability1, ability2};
            CharacterCard charCard1 = new CharacterCard("BallMan", "ball", 330, abilityList);
            CharacterCard[] charList = {charCard1};
            PowerCard pwrCard1 = new PowerCard("POWERRRR", 5);
            PowerCard[] pwrList = {pwrCard1};
            EffectCard effCard1 = new EffectCard("ballEffect", "This card has no instructions", 0, false);
            EffectCard effCard2 = new EffectCard("Cherry Magic", "this card is gay", 3, true);
            System.out.println(effCard2.getCardRarity());
            EffectCard[] effList = {effCard1, effCard2};
            System.out.println(charCard1);
            CardDeck newDeck = new CardDeck(pwrList, charList, effList);
            System.out.println(newDeck.getDeckSize());
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
