using System;
using ExHomeTheater.Subsistemas;
using ExHomeTheater.Fachada;

namespace ExHomeTheater
{
    class Program
    {
        static void Main(string[] args)
        {
            TV minhaTV = new TV();
            Som meuSom = new Som();
            playerMedia meuPlayer = new playerMedia();
            luzAmbiente minhaLuz = new luzAmbiente();

            HomeTheaterFachada controle = new HomeTheaterFachada(minhaTV, meuSom, meuPlayer, minhaLuz);

            controle.AssistirFilme("ATLA");
            controle.DesligarTudo();

         }
    }

}
