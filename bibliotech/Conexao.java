import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexao {

    private static final String URL =
        "jdbc:mariadb://localhost:3306/bibliotech";
    private static final String USUARIO = "bibliotech";
    private static final String SENHA = "LC"; 

    public static Connection conectar()
            throws SQLException {

        return DriverManager.getConnection(
            URL, USUARIO, SENHA
        );
    }
}