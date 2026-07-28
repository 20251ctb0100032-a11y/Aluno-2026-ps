
public class Main {

    public static void main(String[] args) {

        Veiculo v1 = new Veiculo("Jo Sedan", "ABC1234", 2020, 15);
        Veiculo v2 = new Veiculo("Jo SUV", "DEF5678", 2022, 60);
        Veiculo v3 = new Veiculo("Jo Hatch", "GHI9012", 2018, 80);

        System.out.println("=== TESTE 1 ===");
        System.out.println(v1.resumo());

        System.out.println("\n=== TESTE 2 ===");
        if (!v1.setModelo("")) {
            System.out.println("Alteração recusada.");
        }

        System.out.println("\n=== TESTE 3 ===");
        if (!v1.abastecer(-10)) {
            System.out.println("Abastecimento recusado.");
        }

        System.out.println("\n=== TESTE 4 ===");
        if (v1.ligar()) {
            System.out.println("Veículo ligado.");
        }

        if (v1.dirigir(10)) {
            System.out.println("Veículo dirigiu.");
        }

        System.out.println(v1.resumo());

        System.out.println("\n=== TESTE 5 ===");
        if (!v1.dirigir(100)) {
            System.out.println("Não foi possível dirigir.");
        }

        System.out.println("\n=== ESTADO FINAL DOS OBJETOS ===");

        System.out.println("\nVeículo 1");
        System.out.println(v1.resumo());

        System.out.println("\nVeículo 2");
        System.out.println(v2.resumo());

        System.out.println("\nVeículo 3");
        System.out.println(v3.resumo());
    }
}