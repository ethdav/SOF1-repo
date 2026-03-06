package geometry;

public class Circle extends Shape{
    double radius;

    public Circle() {
        super();
        radius = 1.0;
    }

    public Circle(double newRad) {
        super();
        radius = newRad;
    }

    public Circle(double newRad, String newColor, boolean fill) {
        super(newColor, fill);
        radius = newRad;
    }

    @Override
    public String toString() {
        String shapeString = "A Circle with radius " + this.radius 
                            + " which is a subclass of " + super.toString();
        return shapeString;
    }

    public double getRadius() {
        return this.radius;
    }

    public void setRadius(double newRad) {
        this.radius = newRad;
    }

    public double getArea() {
        return Math.pow(this.radius, 2) * Math.PI;
    }

    public double getPerimeter() {
        return 2 * Math.PI * this.radius;
    }

    public static void main(String[] args) {
        Circle circle1 = new Circle();
        Circle circle2 = new Circle(3.0);
        Circle circle3 = new Circle(2.0, "pink", false);
        circle1.setColor("mauve");
        System.out.println(circle1.toString());
        System.out.println(circle2.toString());
        System.out.println(circle3.toString());
        System.out.println(circle3.getArea());
    }
}
