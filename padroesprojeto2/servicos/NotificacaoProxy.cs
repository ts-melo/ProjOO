using System;
using SistemaNotificacao.Core;


namespace SistemaNotificacao.Servicos;

public class NotificacaoProxy : INotificacao
{
    private readonly INotificacao _servicoReal;
    private readonly ConfiguracaoGlobal _config;
    private int _tentativasRealizadas= 0;

    public NotificacaoProxy(INotificacao servicoReal)
    {
        _servicoReal = servicoReal;
        _config = ConfiguracaoGlobal.Instancia;
    }

    public void Enviar(string mensagem, string destino)
    {
        if(_tentativasRealizadas >= _config.MaxTentativas)
        {
            Console.WriteLine($"[Proxy] Limite de tentativas atingido para {destino}. Mensagem não enviada.");
            return;
        }
        Console.WriteLine($"[proxylog]{DateTime.Now}:Tentativa de envio para {destino}");

        _servicoReal.Enviar(mensagem, destino);
        _tentativasRealizadas++;

        Console.WriteLine($"[proxylog]{DateTime.Now} SUCESSO: Tentativa {_tentativasRealizadas} para {destino}");
    
    }

}