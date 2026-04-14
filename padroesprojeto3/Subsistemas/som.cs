using System;

namespace ExHomeTheater.Subsistemas
{
    public class som
    {
        public void Ligar()=> Console.Write("Som ligado");
        public void Desligar()=> Console.Write("Som desligado");
        public void ConfigurarVolume(int volume)=> Console.WriteLine($"Volume configurado para {volume}");        
    }

}