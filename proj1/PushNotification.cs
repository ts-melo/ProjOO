using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class PushNotification : Notificacao
    {
        public override void Enviar(string msg, string destino)
            => Console.WriteLine($"[Push] Para: {destino} | Msg: {msg}");

    }
}
