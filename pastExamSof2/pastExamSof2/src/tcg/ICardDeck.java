package tcg;

import java.util.*;

public interface ICardDeck {
    void insertCard(AbstractCard card);

    AbstractCard drawCard();

    List<AbstractCard> drawThree();

    int getDeckSize();

    boolean isEmpty();
}
