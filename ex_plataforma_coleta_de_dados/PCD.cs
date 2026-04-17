using System;
using System.Collections.Generic;

namespace SistemaMonitoramentoAmazonia
{
    public class PCD
    {
        private List<IObservadorPCD> _universidades = new List<IObservadorPCD>();
        private double _temperatura;
        private double _ph;
        private double _umidade;

        public PCD(string nome) => Nome = nome;

        public void RegistrarInteresse(IObservadorPDC uni)
        {
            if (!_universidades.Contains(uni))
            {
                _universidades.Add(uni);
            }
        }

        public void setMedicoes(double temp, double ph, double umidade)
        {
            _temperatura = temp;
            _ph = ph;
            _umidade = umidade;
            Notificar();
        }

        private void Notificar()
        {
            foreach (var uni in _universidades)
            {
                uni.Atualizar(Nome, _temperatura, _ph, _umidade);
            }
        }

    }
}