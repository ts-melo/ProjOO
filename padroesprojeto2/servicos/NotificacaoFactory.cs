using System;
namespace SistemaNotificacao.Servicos;

public static class NotificacaoFactory
{
    public static INotificacao Criar(string tipo)
    {
        INotificacao servico = tipo.ToLower() switch
        {
            "email" => new EmailNotificacao(),
            "sms" => new SmsLegacyAdapter(),
            "push" => new PushNotificacao(),
            _ => throw new ArgumentException("Canal de notificação desconhecido.")
        };

        return new NotificacaoProxy(servico);
    }
}