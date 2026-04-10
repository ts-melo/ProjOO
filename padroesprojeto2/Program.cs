using System;
using SistemaNotificacao.Core;
using SistemaNotificacao.Servicos;

// Acessando o Singleton
var config = ConfiguracaoGlobal.Instancia;
config.MaxTentativas = 2;
Console.WriteLine($"--- {config.NomeAplicacao} ---");
Console.WriteLine($"Conectado ao servidor: {config.ServidorEnvio}\n");

// Usando a Factory para disparar notificações
string[] canais = { "email", "sms", "push" };

foreach (var canal in canais)
{
    try 
    {
        var servico = NotificacaoFactory.Criar(canal);
        servico.Enviar("Seu código de verificação é 1234", "usuario_final");
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Erro: {ex.Message}");
    }
}