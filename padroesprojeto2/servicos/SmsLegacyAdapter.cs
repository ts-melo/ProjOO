namespace SistemaNotificacao.Servicos;
using System;
// A classe externa que não podemos mudar
public class LegacySMS
{
    public void EnviarMensagemDireta(string tel, string texto) 
    {
        Console.WriteLine($"[Legacy SMS] Via API Externa: {tel} -> {texto}");
    }
}
public class SmsLegacyAdapter : INotificacao
{
    private readonly LegacySMS _legacyService;

    public SmsLegacyAdapter()
    {
        _legacyService = new LegacySMS();
    }

    public void Enviar(string mensagem, string destino)
    {
        _legacyService.EnviarMensagemDireta(destino, mensagem);
    }
}