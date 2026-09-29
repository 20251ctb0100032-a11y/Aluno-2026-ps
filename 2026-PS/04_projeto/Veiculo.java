public class Veiculo {

    private String modelo;
    private String placa;
    private int ano;
    private int combustivel;
    private boolean ligado;

    public Veiculo(String modelo, String placa, int ano, int combustivel) {
        this.modelo = modelo;
        this.placa = placa;
        this.ano = ano;
        this.combustivel = combustivel;
        this.ligado = false;
    }

    // Getters
    public String getModelo() {
        return modelo;
    }

    public String getPlaca() {
        return placa;
    }

    public int getAno() {
        return ano;
    }

    public int getCombustivel() {
        return combustivel;
    }

    public boolean isLigado() {
        return ligado;
    }

    // Setter com validação
    public boolean setModelo(String modelo) {
        if (modelo == null || modelo.trim().isEmpty()) {
            return false;
        }
        this.modelo = modelo;
        return true;
    }

    // Método de comportamento
    public boolean ligar() {
        if (ligado || combustivel <= 0) {
            return false;
        }
        ligado = true;
        return true;
    }

    // Método de comportamento
    public boolean abastecer(int litros) {
        if (litros <= 0) {
            return false;
        }

        combustivel += litros;

        if (combustivel > 100) {
            combustivel = 100;
        }

        return true;
    }

    // Método de comportamento
    public boolean dirigir(int consumo) {
        if (!ligado || consumo <= 0 || combustivel < consumo) {
            return false;
        }

        combustivel -= consumo;
        return true;
    }

    // Resumo do veículo
    public String resumo() {
        return "Modelo: " + modelo +
               "\nPlaca: " + placa +
               "\nAno: " + ano +
               "\nCombustível: " + combustivel +
               "\nLigado: " + ligado;
    }
}