public class TesteLivroDAO {

    public static void main(String[] args) {

        LivroDAO dao = new LivroDAO();

        boolean excluido1 = dao.excluirLivro(2);
        System.out.println("O Pequeno Príncipe excluído: " + excluido1);

        boolean excluido2 = dao.excluirLivro(3);
        System.out.println("Dom Casmurro excluído: " + excluido2);

        boolean excluido3 = dao.excluirLivro(4);
        System.out.println("O Hobbit excluído: " + excluido3);
    }
}