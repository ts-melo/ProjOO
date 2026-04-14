using System;

namespace ExHomeTheater
{
    //subsistemas ou dispositivos

    public class televisao
    {
        public void Ligar()=> Console.WriteLine("Tv ligada");
        public void Desligar()=> Console.WriteLine("Tv desligada");
        public void ConfigHDMI()=> Console.WriteLine("HDMI configurado");
    }

    public class som
    {
        public void Ligar()=> Console.Write("Som ligado");
        public void Desligar()=> Console.Write("Som desligado");
        public void ConfigurarVolume(int volume)=> Console.WriteLine($"Volume configurado para {volume}");        
    }

    public class playerMedia
    {
        public void Ligar()=> Console.Write("Ligando sistema de midia");
        public void Desligar()=> Console.Write("Desligando sistema de midia");
        public void Play(string filme)=> Console.WriteLine($"Reproduzindo filme: {filme}");
        
    }

    public class luzAmbiente
    {
        public void Ligar()=> Console.WriteLine("Luz ambiente ligada");
        public void Desligar()=> Console.WriteLine("Luz ambiente desligada");
        public void ConfigurarIntensidade(int intensidade)=> Console.WriteLine($"Intensidade da luz configurada para {intensidade}");
        
    }

}
