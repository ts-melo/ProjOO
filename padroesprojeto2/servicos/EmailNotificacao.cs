namespace SistemaNotificacao.Servicos;

public class EmailNotificacao : INotificacao
{
    public void Enviar(string msg, string dst) => 
        Console.WriteLine($"[E-mail] Destino: {dst} | Msg: {msg}");
}