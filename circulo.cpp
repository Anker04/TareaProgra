#include <iostream>
#include <cmath>

class Circulo {
private:
    double radio;

public:
    // Constructor
    Circulo(double r) : radio(r) {}

    // Métodos
    double calcularArea() {
        return M_PI * radio * radio;
    }

    double calcularPerimetro() {
        return 2 * M_PI * radio;
    }

    void cambiarRadio(double nuevoRadio) {
        radio = nuevoRadio;
    }
};

int main() {

    Circulo miCirculo(5.0); 

    double area = miCirculo.calcularArea();
    std::cout << "El área del círculo es: " << area << std::endl;

    double perimetro = miCirculo.calcularPerimetro();
    std::cout << "El perímetro del círculo es: " << perimetro << std::endl;

    return 0;
}
