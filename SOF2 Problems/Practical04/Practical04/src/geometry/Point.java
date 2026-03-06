package geometry;

public class Point {
    double x, y;
    String color;

    public Point() {
        x = 0.0;
        y = 0.0;
        color = "black";
    }

    public Point(int xPos, int yPos) {
        x = xPos;
        y = yPos;
        color = "black";
    }

    public void setColor(String newColor) {
        color = newColor;
    }

    public String getColor() {
        return this.color;
    }

    public String toString() {
        return "x = " + this.x 
                + ", y = " + this.y;
    }

    public static void main(String[] args) {
        Point point1 = new Point(5, -7);
        point1.setColor("blue");
        System.out.println(point1.toString());
    }
}
