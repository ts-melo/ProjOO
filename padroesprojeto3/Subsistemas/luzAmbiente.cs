using System;

namespace ExHomeTheater.Subsistemas
{


    public class luzAmbiente
    {
        public void Ligar()=> Console.WriteLine("Luz ambiente ligada");
        public void Desligar()=> Console.WriteLine("Luz ambiente desligada");
        public void ConfigurarIntensidade(int intensidade)=> Console.WriteLine($"Intensidade da luz configurada para {intensidade}");
        
    }

}