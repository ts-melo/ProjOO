using System;
namespace SistemaNotificacao.Servicos;

public class SmsNotificacao : INotificacao
{
    public void Enviar(string msg, string dst) => 
        Console.WriteLine($"[SMS] Destino: {dst} | Msg: {msg}");
}