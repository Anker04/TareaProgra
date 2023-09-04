#include <iostream>

class Rectangulo {
private:
    double longitud;
    double ancho;

public:
    // Constructor
    Rectangulo(double l, double a) : longitud(l), ancho(a) {}

    // Métodos
    double calcularArea() {
        return longitud * ancho;
    }

    double calcularPerimetro() {
        return 2 * (longitud + ancho);
    }

    void cambiarLongitud(double nuevaLongitud) {
        longitud = nuevaLongitud;
    }

    void cambiarAncho(double nuevoAncho) {
        ancho = nuevoAncho;
    }
}

int main() {
    
    Rectangulo miRectangulo(5.0, 3.0); 


    double area = miRectangulo.calcularArea();
    std::cout << "El área del rectángulo es: " << area << std::endl;

    double perimetro = miRectangulo.calcularPerimetro();
    std::cout << "El perímetro del rectángulo es: " << perimetro << std::endl;

    return 0;
}
