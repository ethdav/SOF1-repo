package geometry;

public class Line {
    Point start, end;
    String color;

    public Line(Point starPoint, Point endPoint) {
        start = starPoint;
        end = endPoint;
        color = "black";
    }

    public String getColor() {
        return this.color;
    }

    public void setColor(String newColor) {
        color = newColor;
        start.setColor(newColor);
        end.setColor(newColor);
    }

    public Point getStart() {
        return this.start;
    }

    public Point getEnd() {
        return this.end;
    }

    public double getLength() {
        return Math.sqrt(Math.pow(end.x - start.x, 2) 
                        + Math.pow(end.y - start.y, 2));
    }

    public void setStart(Point newStart) {
        start = newStart;
    }

    public void setEnd(Point newEnd) {
        end = newEnd;
    }

    public String toString() {
        return "start: " + start.toString() + "\n"
                + "end: " + end.toString() + "\n"
                + "color = " + color + ", length = " + this.getLength();
    }

    public static void main(String[] args) {
        Point start = new Point(3,4);
        Point end = new Point(11, -13);
        Line line1 = new Line(start, end);
        line1.setColor("chartreuse");
        System.out.println(line1.toString());
        System.out.println(start.getColor());
    }
}
