#!/bin/bash
sudo service mariadb start > /dev/null 2>&1
export DB_USER=bibliotech
if [ -z "$DB_PASSWORD" ]; then
    read -rs -p "Digite a senha do MariaDB: " DB_PASSWORD
    echo
    export DB_PASSWORD
fi

javac -cp ".:lib/*" *.java

echo "=== BIBLIOTECH ==="
echo "1. Listar Livros"
echo "2. Buscar Livro por ID"
echo "3. Testar Empréstimo"
read -p "Escolha uma opção (1-3): " opcao

case $opcao in
    1) java -cp ".:lib/*" TesteListarLivros ;;
    2) java -cp ".:lib/*" TesteBuscarLivro ;;
    3) java -cp ".:lib/*" TesteEmprestimo ;;
    *) echo "Opção inválida!" ;;
esac
