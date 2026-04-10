using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class SMS : Notificacao
    {
        public override void Enviar(string msg, string destino)
            => Console.WriteLine($"[SMS] Para: {destino} | Msg: {msg}");

    }
}
