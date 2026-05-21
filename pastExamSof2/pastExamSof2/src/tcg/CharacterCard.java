package tcg;

import java.util.*;

public class CharacterCard extends AbstractCard{
    protected int cardHealth;
    protected String cardPowerType;
    protected List<Ability> cardAbilities = new ArrayList<>();
    private String message = "CharacterCard: Ability %s does not match power type.";

    public CharacterCard(
        String cardName, 
        String cardPowerType,
        int cardHealth, 
        Ability[] cardAbilities
    ) throws IllegalArgumentException, IncompatiblePowerException
    {
        super(cardName, CardType.CHARACTER);
        if (cardHealth < 120 || cardHealth > 400 || cardHealth%10 != 0) {
            throw new IllegalArgumentException();
        }
        
        int listLen = 0;
        for(Ability ability : cardAbilities) {
            if (ability.abilityPowerType != cardPowerType && ability.abilityPowerType != "ANY") {
                throw new IncompatiblePowerException(
                    String.format(message, ability.abilityName), 
                    cardPowerType, 
                    ability.abilityPowerType);
            }
            this.cardAbilities.add(ability);
            listLen+=1;
        }
        if (listLen != 2) {
            throw new IllegalArgumentException();
        }

        this.cardPowerType = cardPowerType;
        this.cardHealth = cardHealth;
        calculateRarity();
    }

    @Override
    void calculateRarity() {
        Ability ability1 = cardAbilities.get(0);
        Ability ability2 = cardAbilities.get(1);
        int bothAbilityDmg = ability1.abilityDamage + cardAbilities.get(1).abilityDamage;
        boolean isTypeAny = false;
        if (ability1.abilityPowerType == "ANY" || ability2.abilityPowerType == "ANY") {
            isTypeAny = true;
        }

        if (isTypeAny) {
            if (cardHealth >= 220 && cardHealth <= 400 && bothAbilityDmg > 300) {
                cardRarity = Rarity.EPIC;
            }
            else if (cardHealth >= 120 && cardHealth <= 400) {
                cardRarity = Rarity.RARE;
            }
        }
        else {
            if (cardHealth >= 120 && cardHealth <= 200 && bothAbilityDmg > 200) {
                cardRarity = Rarity.UNCOMMON;
            }
            else {
                cardRarity = Rarity.COMMON;
            }
        }
    }

    public String getCardPowerType() {
        return cardPowerType;
    }

    public int getCardHealth() {
        return cardHealth;
    }

    public int getAbilityDamage(int position) throws IllegalArgumentException{
        if (position < 0 || position > 1) {
            throw new IllegalArgumentException();
        }
        return cardAbilities.get(position).abilityDamage;
    }

    public int getAbilityPowerStrength(int position) throws IllegalArgumentException{
        if (position < 0 || position > 1) {
            throw new IllegalArgumentException();
        }
        return cardAbilities.get(position).abilityPowerStrength;
    }

    @Override
    public String toString() {
        return super.toString() + "," + cardHealth + "," + cardPowerType + ","
        + cardAbilities.get(0).toString() + ","
        + cardAbilities.get(1).toString();
    }
}
