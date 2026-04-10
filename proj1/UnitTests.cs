using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class UnitTests
    {
        public static void ExecutarTodos()
        {
            Console.WriteLine(">>> INICIANDO TESTES DE UNIDADE <<<");

            Validar(TestarSingleton(), "Singleton: Garantir instância única");
            Validar(TestarFactoryEmail(), "Factory: Criar objeto Email");
            Validar(TestarFactorySMS(), "Factory: Criar objeto SMS");

            Console.WriteLine(">>> TESTES FINALIZADOS <<<\n");
        }

        private static void Validar(bool resultado, string nomeTeste)
        {
            if (resultado)
                Console.WriteLine($"[PASS] {nomeTeste}");
            else
                Console.WriteLine($"[FAIL] {nomeTeste}");
        }

        private static bool TestarSingleton()
        {
            var s1 = SistemaConfig.GetInstance();
            var s2 = SistemaConfig.GetInstance();
            return ReferenceEquals(s1, s2);
        }

        private static bool TestarFactoryEmail()
        {
            var n = NotificacaoFactory.Criar("email");
            return n is Email;
        }

        private static bool TestarFactorySMS()
        {
            var n = NotificacaoFactory.Criar("sms");
            return n is SMS;
        }
    }
}
