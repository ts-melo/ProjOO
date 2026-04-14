using Cafeteria.Base;
using Cafeteria.Decorators;

namespace Cafeteria.DecoratorsConcretos
{
    public class Leite : AddDecorator
    {
        public Leite(Bebida bebida) : base(bebida) { }

        public override string Descricao => _bebida.Descricao + ", Leite";
        public override double Custo() => _bebida.Custo() + 1.00;
    }
}