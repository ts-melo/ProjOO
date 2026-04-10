namespace SistemaNotificacao.Core;

public sealed class ConfiguracaoGlobal
{
    private static ConfiguracaoGlobal? _instancia;
    private static readonly object _lock = new object();

    public string NomeAplicacao { get; set; } = "Sistema Alerta v1.0";
    public string ServidorEnvio { get; set; } = "smtp.servidor.com";
    public int MaxTentativas { get; set; } = 3;

    private ConfiguracaoGlobal() { }

    public static ConfiguracaoGlobal Instancia
    {
        get
        {
            lock (_lock)
            {
                _instancia ??= new ConfiguracaoGlobal();
                return _instancia;
            }
        }
    }
}