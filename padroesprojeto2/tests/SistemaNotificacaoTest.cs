using Xunit;
using SistemaNotificacao.Core;
using SistemaNotificacao.Servicos;

namespace SistemaNotificacao.Tests;
public class SistemaNotificacaoTests
{
    [Fact]
    public void Singleton_DeveGarantirInstanciaUnica()
    {
        var i1 = ConfiguracaoGlobal.Instancia;
        var i2 = ConfiguracaoGlobal.Instancia;
        Assert.Same(i1, i2);
    }

    [Fact]
    public void Factory_DeveRetornarSmsComAdapter()
    {
        var servico = NotificacaoFactory.Criar("sms");
        Assert.NotNull(servico);
        Assert.IsType<NotificacaoProxy>(servico);
    }

    [Fact]

    public void Proxy_DeveImpedirEnvioExcessivo()
    {
        var config = ConfiguracaoGlobal.Instancia;
        config.MaxTentativas = 2; // Configuramos para 2 tentativas
        var emailReal = new EmailNotificacao();
        var proxy = new NotificacaoProxy(emailReal);

        proxy.Enviar("Teste 1", "destino1");
        proxy.Enviar("Teste 2", "destino2");
    }
}