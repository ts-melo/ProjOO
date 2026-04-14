using ExHomeTheater.Subsistemas;
using System;

namespace ExHomeTheater.Fachada
{
    public class HomeTheaterFachada{
        private readonly TV _tv;
        private readonly Som _som;
        private readonly playerMedia _player;
        private readonly luzAmbiente _luz;

        public HomeTheaterFachada(TV tv, Som som, playerMedia pm, luzAmbiente luz)
        {
            _tv = tv;
            _som = som;
            _player = pm;
            _luz = luz;
        }

        public void AssistirFilme(string filme)
        {
            Console.WriteLine("Preparando para assistir filme...");
            _luz.Ligar();
            _tv.Ligar();
            _tv.ConfigHDMI();
            _som.Ligar();
            _som.ConfigurarVolume(20);
            _player.Ligar();
            _player.Play(filme);
            Console.WriteLine("Aproveite o filme!");
        }

        public void DesligarTudo()
        {
            Console.WriteLine("desligando");
            _player.Desligar();
            _som.Desligar();
            _tv.Desligar();
            _luz.Desligar();
            Console.WriteLine("Tudo desligado");
        }
    }
}