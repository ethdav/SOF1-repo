package geometry;

public class Rectangle extends Shape {
    double width, length;

    public Rectangle() {
        super();
        width = 1.0;
        length = 1.0;
    }

    public Rectangle(double newWidth, double newLength) {
        super();
        width = newWidth;
        length = newLength;
    }

    public Rectangle(double newWidth, double newLength, String newColor,       boolean fill) {
        super(newColor, fill);
        width = newWidth;
        length = newLength;
    }

    public double getWidth() {
        return this.width;
    }

    public double getLength() {
        return this.length;
    }

    public void setWidth(double newWidth) {
        this.width = newWidth;
    }

    public void setLength(double newLength) {
        this.length = newLength;
    }

    public double getArea() {
        return this.width * this.length;
    }

    public double getPerimeter() {
        return (2 * this.width) + (2 * this.length);
    }

    @Override
    public String toString() {
        String shapeString = "A Rectangle with width = " + this.width 
                            + " and length = " + this.length 
                            + " which is a subclass of " + super.toString();
        return shapeString;
    }

    public static void main(String[] args) {
        Rectangle rect1 = new Rectangle();
        Rectangle rect2 = new Rectangle(2.5, 4);
        Rectangle rect3 = new Rectangle(5, 5, "ochre", false);
        System.out.println(rect1.toString());
        System.out.println(rect2.toString());
        System.out.println(rect3.toString());
        System.out.println(rect3.getArea() + "   " + rect3.getPerimeter());
    }
}
