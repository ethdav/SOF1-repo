package tcg;

public abstract class AbstractCard {
    protected String cardName;
    protected CardType cardType;
    protected Rarity cardRarity;
    protected int cardCount = 0;

    public enum CardType{
        CHARACTER,
        EFFECT,
        POWER
    }

    public enum Rarity{
        COMMON,
        UNCOMMON,
        RARE,
        EPIC
    }

    AbstractCard(String cardName, CardType cardType) {
        this.cardName = cardName;
        this.cardType = cardType;
        this.cardCount += 1;
    }

    public String getCardName() {
        return cardName;
    }

    public Rarity getCardRarity() {
        return cardRarity;
    }

    public int getCardCount() {
        return cardCount;
    }

    public CardType getCardType() {
        return cardType;
    }

    public void setCardName(String newName) {
        cardName = newName;
    }

    abstract void calculateRarity();

    @Override
    public String toString() {
        return cardType + "," + cardName + "," + cardRarity;
    }
}
