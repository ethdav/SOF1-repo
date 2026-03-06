package geometry;

public class Square extends Rectangle{
    
    public Square() {
        super();
    }

    public Square(double side) {
        super(side, side);
    }

    public Square(double side, String newColor, boolean fill) {
        super(side, side, newColor, fill);
    }

    @Override
    public String toString() {
        String shapeString = "A Sqaure with side = " + this.length
                            + " which is a subclass of " + super.toString();
        return shapeString;
    }

    public double getSide() {
        return this.length;
    }

    public void setSide(double newSide) {
        this.length = newSide;
        this.width = newSide;
    }

    @Override
    public void setWidth(double newWidth) {
        this.setSide(newWidth);
    }

    @Override
    public void setLength(double newLength) {
        this.setSide(newLength);
    }

    public static void main(String[] args) {
        Square square1 = new Square(5.0);
        square1.setSide(3);
        System.out.println(square1.getSide());
        System.out.println(square1.getArea());
    }
}
