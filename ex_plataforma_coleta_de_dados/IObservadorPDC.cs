namespace SistemaMonitoramentoAmazonia
{
    public interface IObservadorPCD
    {
        public void Atualizar(string nomePCD, double temp, double ph, double umidade);
    }
}