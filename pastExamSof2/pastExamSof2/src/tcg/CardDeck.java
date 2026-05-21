package tcg;

import java.util.*;

import tcg.AbstractCard.Rarity;

public class CardDeck implements ICardDeck{
    int MAX_DECK_SIZE = 18;
    int MIN_CHARACTER_CARDS = 1;
    int MAX_EPIC_CARDS = 3;
    int MAX_CARD_COPIES = 3;
    List<AbstractCard> cards = new LinkedList<>();

    CardDeck(
        PowerCard[] powerCards, 
        CharacterCard[] characterCards,
        EffectCard[] effectCards
    ) throws IllegalArgumentException 
    {
        int numEpicCards = 0;
        Map<String, Integer> copies = new HashMap<>();
        for (PowerCard pwrCard : powerCards) {
            cards.add(pwrCard);
            if (pwrCard.cardRarity == Rarity.EPIC) {
                numEpicCards += 1;
            }
            copies.put(pwrCard.cardName, copies.getOrDefault(pwrCard.cardName, 0) + 1);
        }
        for (CharacterCard charCard : characterCards) {
            cards.add((int)(Math.random() * cards.size()), charCard);
            if (charCard.cardRarity == Rarity.EPIC) {
                numEpicCards += 1;
            }
            copies.put(charCard.cardName, copies.getOrDefault(charCard.cardName, 0) + 1);
        }
        for (EffectCard effCard : effectCards) {
            cards.add((int)(Math.random() * cards.size()), effCard);
            if (effCard.cardRarity == Rarity.EPIC) {
                numEpicCards += 1;
            }
            copies.put(effCard.cardName, copies.getOrDefault(effCard.cardName, 0) + 1);
        }

        if (cards.size() > MAX_DECK_SIZE) {
            throw new IllegalArgumentException();
        }
        if (numEpicCards > MAX_EPIC_CARDS) {
            throw new IllegalArgumentException();
        }
        if (characterCards.length < MIN_CHARACTER_CARDS) {
            throw new IllegalArgumentException();
        }
        for (int cardCopy : copies.values()) {
            if (cardCopy > MAX_CARD_COPIES) {
                throw new IllegalArgumentException();
            }
        }
    }

    public void insertCard(AbstractCard card) {
        cards.add(0, card);
    }

    public AbstractCard drawCard() {
        return cards.remove(cards.size());
    }

    public List<AbstractCard> drawThree() {
        List<AbstractCard> topThree = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            topThree.add(cards.remove(cards.size()));
        }
        return topThree;
    }

    public int getDeckSize() {
        return cards.size();
    }

    public boolean isEmpty() {
        if (cards.size() == 0) {
            return true;
        }
        return false;
    }
}
