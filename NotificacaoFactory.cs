using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class NotificacaoFactory
    {
        private static readonly Dictionary<string, Func<Notificacao>> _notificacoes = new Dictionary<string, Func<Notificacao>>
        {
            { "email", () => new Email() },
            { "sms", () => new SMS() },
            { "push", () => new PushNotification() }
        };
        public static Notificacao Criar(string tipo)
        {
            string chave = tipo.ToLower();
            if(_notificacoes.ContainsKey(chave))
            {
                return _notificacoes[chave]();
            }
            throw new NotSupportedException($"O tipo '{tipo}' não está registrado.");
        }

        public static void RegistrarTipo(string nome, Func<Notificacao> criador)
        {
            _notificacoes[nome.ToLower()] = criador;
        }
    }
}
