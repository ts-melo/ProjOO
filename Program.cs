using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            UnitTests.ExecutarTodos();

            // 2. Simulação normal do sistema
            Console.WriteLine("=== SIMULAÇÃO DO SISTEMA ===");

            var config = SistemaConfig.GetInstance();
            Console.WriteLine($"Configuração: {config.NomeApp} | Máx Tentativas: {config.MaxTent}");

            Notificacao messenger = NotificacaoFactory.Criar("push");
            messenger.Enviar("Você tem uma nova mensagem", "User123");

            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}
