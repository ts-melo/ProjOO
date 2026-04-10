using Xunit;
using SistemaNotificacao.Core;
using SistemaNotificacao.Servicos;
public class SistemaNotificacaoTests
{
    [Fact]
    public void Singleton_DeveSerUnico()
    {
        var i1 = ConfiguracaoGlobal.Instancia;
        var i2 = ConfiguracaoGlobal.Instancia;
        Assert.Same(i1, i2);
    }

    [Fact]
    public void Factory_DeveRetornarTipoCorreto()
    {
        var obj = NotificacaoFactory.Criar("sms");
        Assert.IsType<SmsNotificacao>(obj);
    }
}