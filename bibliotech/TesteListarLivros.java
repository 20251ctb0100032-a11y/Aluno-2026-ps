import java.util.List;

public class TesteListarLivros {

    public static void main(String[] args) {

        LivroDAO dao = new LivroDAO();

        // Agora o método retorna uma lista de objetos Livro, não de Strings
        List<Livro> livros = dao.listarLivros();

        System.out.println("=== LIVROS PUBLICADOS A PARTIR DE 2000 ===");

        if (livros.isEmpty()) {

            System.out.println("Nenhum livro encontrado.");

        } else {

            boolean encontrou = false;

            for (Livro livro : livros) {

                // Filtro do Desafio Prático usando o getter getAno()
                if (livro.getAno() >= 2000) {

                    System.out.println(
                        livro.getId() + " - " +
                        livro.getTitulo() + " - " +
                        livro.getAutor() + " (" +
                        livro.getAno() + ")"
                    );

                    encontrou = true;
                }
            }

            if (!encontrou) {
                System.out.println("Nenhum livro publicado a partir de 2000.");
            }
        }
    }
}