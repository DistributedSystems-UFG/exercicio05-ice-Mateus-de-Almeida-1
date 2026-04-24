module Demo
{
    interface Printer
    {   // Função original (tive que mudar de void para string para se adequar ao que o ex.6 pede)
        string printString(string s);

        // NOVO: imprime a string em maiúsculo (tive que mudar de void para string para se adequar ao que o ex.6 pede)
        string printUpperCase(string s);

        // NOVO: retorna a quantidade de caracteres (tive que mudar de void para string para se adequar ao que o ex.6 pede)
        string countChars(string s);
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
