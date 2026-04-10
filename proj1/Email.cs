using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Email : Notificacao
    {
        public override void Enviar(string msg, string destino)
            => Console.WriteLine($"[E-mail] Para: {destino} | Msg: {msg}");
    }
}
