public class circulo {
    private double radio;
    
    public circulo(double radio){
        this.radio = radio;
    }

    public double CalcularArea() {
        return Math.PI * radio * radio;
    }

    public double CalcularPerimetro (){
        return 2 * Math.PI * radio;
    }
        
    public void CambiarRadio( double NuevoRadio){
        this.radio = NuevoRadio;
    }

    public static void main(String[] args){

        circulo miCirculo = new circulo(5.0); 

        double area = miCirculo.CalcularArea();
        System.out.println("El area del circulo es: " + area);

        double perimetro = miCirculo.CalcularPerimetro();
        System.out.println("El perimetro del circulo es: " + perimetro);
    }
}
