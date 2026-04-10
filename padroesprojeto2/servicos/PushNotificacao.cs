using System;
namespace SistemaNotificacao.Servicos;

public class PushNotificacao : INotificacao
{
    public void Enviar(string msg, string dst) => 
        Console.WriteLine($"[Push] Destino: {dst} | Msg: {msg}");
}