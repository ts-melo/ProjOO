using System;

namespace ExHomeTheater.Subsistemas
{
    public class playerMedia
    {
        public void Ligar()=> Console.Write("Ligando sistema de midia");
        public void Desligar()=> Console.Write("Desligando sistema de midia");
        public void Play(string filme)=> Console.WriteLine($"Reproduzindo filme: {filme}");
        
    }

}