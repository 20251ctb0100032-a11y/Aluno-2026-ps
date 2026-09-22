public class  hq2 {

    // Exibe apenas o nome do produto
    static void exibirProduto(String nome) {
        System.out.println("Produto: " + nome);
    }

    // Exibe o nome e o preço do produto
    static void exibirProduto(String nome, double preco) {
        System.out.println("Produto: " + nome + " | Preço: R$ " + preco);
    }

    public static void main(String[] args) {

        exibirProduto("Hambúrguer");
        exibirProduto("Pizza", 29.90);
        exibirProduto("Refrigerante", 5.50);
    }
}