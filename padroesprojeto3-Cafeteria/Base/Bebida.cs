using System;

namespace Cafeteria.Base
{
    public abstract class Bebida
    {
        public virtual string Descricao { get; set; } = "Bebida desconhecida";
        public abstract double Custo();
    }
}