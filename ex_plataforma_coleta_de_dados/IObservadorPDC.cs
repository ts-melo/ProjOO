namespace SistemaMonitoramentoAmazonia
{
    public interface IObservadorPCD
    {
        public void Atualizar(strinf nomePCD, double temp, double ph, double umidade);
    }
}