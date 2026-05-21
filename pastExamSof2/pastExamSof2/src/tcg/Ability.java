package tcg;

public class Ability {
    protected String abilityName;
    protected String abilityPowerType;
    protected int abilityPowerStrength;
    protected int abilityDamage;
    
    public Ability() {
        abilityName = "WildCard";
        abilityPowerType = "ANY";
        abilityPowerStrength = 2;
        abilityDamage = 100;
    }

    public Ability(String aName, String aPwrType, int aPwrStrength, int aDmg) throws IllegalArgumentException{
        if (aDmg < 0 || aDmg > 200 || aDmg%10 == 0 ) {
            if (aPwrStrength < 0 || aPwrStrength > 5) {
                throw new IllegalArgumentException();
            }
        }
        abilityName = aName;
        abilityPowerType = aPwrType;
        abilityPowerStrength = aPwrStrength;
        abilityDamage = aDmg;
    }

    public String getAbilityName() {
        return abilityName;
    }

    public String getAbilityPowerType() {
        return abilityPowerType;
    }

    public int getAbilityPowerStrength() {
        return abilityPowerStrength;
    }

    public int getAbilityDamage() {
        return abilityDamage;
    }

    public boolean nerf() {
        if (abilityDamage == 0) {
            return false;
        }
        else if (abilityDamage == 70) {
            if (abilityPowerStrength > 0) {
                abilityPowerStrength -= 1;
            }
        }
        abilityDamage -= 10;
        return true;
    }

    public boolean buff() {
        if (abilityDamage == 200) {
            return false;
        }
        else if (abilityDamage == 130) {
            if (abilityPowerStrength < 5) {
                abilityPowerStrength += 1;
            }
        }
        abilityDamage += 10;
        return true;
    }

    @Override
    public String toString() {
        return abilityName + "," + abilityPowerType + "," 
                + abilityPowerStrength + "," + abilityDamage;
    }
}
