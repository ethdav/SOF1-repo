package tcg;

public class EffectCard extends AbstractCard{
    protected String cardInstructions;
    protected int cardTurnCount;
    protected boolean cardCoinToss;

    EffectCard(
        String cardName, 
        String cardInstructions, 
        int cardTurnCount, 
        boolean cardCoinToss
    ) throws IllegalArgumentException
    {
        super(cardName, CardType.EFFECT);
        if (cardTurnCount < 0 || cardTurnCount > 3) {
            throw new IllegalArgumentException();
        }
        this.cardInstructions = cardInstructions;
        this.cardCoinToss = cardCoinToss;
        calculateRarity();
    }

    @Override
    void calculateRarity() {
        if (cardTurnCount == 1) {
            this.cardRarity = Rarity.COMMON;
        }
        else if (cardTurnCount == 2) {
            this.cardRarity = Rarity.UNCOMMON;
        }
        else if (cardTurnCount == 3) {
            if (cardCoinToss) {
                this.cardRarity = Rarity.UNCOMMON;
            }
            else {
                this.cardRarity = Rarity.RARE;
            }
        }
        else {
            this.cardRarity = Rarity.EPIC;
        }
    }

    public String getCardInstructions() {
        return cardInstructions;
    }

    public int getCardTurnCount() {
        return cardTurnCount;
    }

    public boolean getCardCoinToss() {
        return cardCoinToss;
    }

    @Override
    public String toString() {
        return super.toString() + "," + cardInstructions + "," + cardTurnCount;
    }
}
