using Cafeteria.Base;
using Cafeteria.Decorators;

namespace Cafeteria.DecoratorsConcretos
{
    public class Canela : AddDecorator
    {
        public Canela(Bebida bebida) : base(bebida) { }

        public override string Descricao => _bebida.Descricao + ", Canela";
        public override double Custo() => _bebida.Custo() + 0.50;
    }
}