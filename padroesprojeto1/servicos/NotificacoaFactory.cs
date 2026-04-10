namespace SistemaNotificacao.Servicos;

public static class NotificacaoFactory
{
    public static INotificacao Criar(string tipo)
    {
        return tipo.ToLower() switch
        {
            "email" => new EmailNotificacao(),
            "sms" => new SmsNotificacao(),
            "push" => new PushNotificacao(),
            _ => throw new ArgumentException("Canal de notificação desconhecido.")
        };
    }
}