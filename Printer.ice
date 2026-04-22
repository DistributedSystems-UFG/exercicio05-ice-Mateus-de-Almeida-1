module Demo
{
    interface Printer
    {   // Função original
        void printString(string s);

        // NOVO: imprime a string em maiúsculo
        void printUpperCase(string s);

        // NOVO: retorna a quantidade de caracteres
        void countChars(string s);
    }
    
    // NOVO: objeto servidor
    interface Calculator
    {
        // Soma dois inteiros e retorna o resultado
        int add(int a, int b);

        // Subtrai dois inteiros e retorna o resultado
        int subtract(int a, int b);

        // Multiplica dois inteiros e retorna o resultado
        int multiply(int a, int b);
    }

}
