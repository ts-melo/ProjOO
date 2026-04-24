using System;

namespace SistemaMonitoramentoAmazonia
{
    public class Universidades : IObservadorPCD
    {
        public string Nome { get; private set; }

        public Universidades(string nome) => Nome = nome;

        public void Atualizar(string nomePCD, double temp, double ph, double umidade)
        {
            Console.WriteLine($"Universidade {Nome} recebeu atualização do PCD {nomePCD}: Temperatura={temp}, pH={ph}, Umidade={umidade}");
        }
    }
}