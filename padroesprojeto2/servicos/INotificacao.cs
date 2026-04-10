namespace SistemaNotificacao.Servicos;

public interface INotificacao
{
    void Enviar(string mensagem, string destino);
}