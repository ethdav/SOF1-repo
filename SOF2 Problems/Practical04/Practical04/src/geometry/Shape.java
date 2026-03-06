package geometry;

public class Shape {
    String color;
    boolean filled;

    public Shape() {
        color = "red";
        filled = true;
    }

    public Shape(String c, boolean fill) {
        color = c;
        filled = fill;
    }

    public String getColor() {
        return this.color;
    }

    public void setColor(String new_color) {
        this.color = new_color;
    }

    public boolean isFilled() {
        return this.filled;
    }

    public void setFilled(boolean new_state) {
        this.filled = new_state;
    }

    public String toString() {
        String shapeString = "A Shape with color " + this.color + " and ";
        if (filled) {
            shapeString += "filled.";
        } else {
            shapeString += "not filled.";
        }
        return shapeString;
    }

    public static void main() {
        Shape shape1 = new Shape();
        Shape shape2 = new Shape("blue", false);
        System.out.println(shape1.toString());
        System.out.println(shape2.toString());
    }
}
