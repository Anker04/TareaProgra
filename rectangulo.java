public class rectangulo {

    private double longitud;
    private double ancho;

    public rectangulo(double longitud, double ancho) {
        this.longitud = longitud;
        this.ancho = ancho;
    }

    public double calcularArea() {
        return longitud * ancho;
    }

    public double calcularPerimetro() {
        return 2 * (longitud + ancho);
    }

    public void cambiarLongitud(double nuevaLongitud) {
        this.longitud = nuevaLongitud;
    }

    public void cambiarAncho(double nuevoAncho) {
        this.ancho = nuevoAncho;
    }

    public static void main(String[] args) {
        rectangulo miRectangulo = new rectangulo(5.0, 3.0); // Puedes cambiar los valores aquí

        double area = miRectangulo.calcularArea();
        System.out.println("El área del rectángulo es: " + area);

        double perimetro = miRectangulo.calcularPerimetro();
        System.out.println("El perímetro del rectángulo es: " + perimetro);
    }
}
