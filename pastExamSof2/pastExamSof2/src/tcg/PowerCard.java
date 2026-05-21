package tcg;

public class PowerCard extends AbstractCard{
    protected int cardPowerStrength;

    public PowerCard(String cardName, int cardPowerStrength) throws IllegalArgumentException{
        super(cardName, CardType.POWER);
        if (cardPowerStrength < 1 || cardPowerStrength > 5) {
            throw new IllegalArgumentException();
        }
        this.cardPowerStrength = cardPowerStrength;
        calculateRarity();
    }

    @Override
    void calculateRarity() {
        if (cardPowerStrength == 1) {
            this.cardRarity = Rarity.COMMON;
        }
        else if (cardPowerStrength == 2 || cardPowerStrength == 3) {
            this.cardRarity = Rarity.UNCOMMON;
        }
        else if (cardPowerStrength == 4) {
            this.cardRarity = Rarity.RARE;
        }
        else {
            this.cardRarity = Rarity.EPIC;
        }
    }

    public int getCardPowerStrength() {
        return cardPowerStrength;
    }

    @Override
    public String toString() {
        return super.toString() + "," + cardPowerStrength;
    }
}
