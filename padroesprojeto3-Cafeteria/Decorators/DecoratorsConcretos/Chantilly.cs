using Cafeteria.Base;
using Cafeteria.Decorators;

namespace Cafeteria.DecoratorsConcretos
{
    public class Chantilly : AddDecorator
    {
        public Chantilly(Bebida bebida) : base(bebida) { }

        public override string Descricao => _bebida.Descricao + ", Chantilly";
        public override double Custo() => _bebida.Custo() + 2.00;
    }
}