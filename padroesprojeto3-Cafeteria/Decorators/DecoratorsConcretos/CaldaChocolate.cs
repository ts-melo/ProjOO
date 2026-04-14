using Cafeteria.Base;
using Cafeteria.Decorators;

namespace Cafeteria.DecoratorsConcretos
{
    public class CaldaChocolate : AddDecorator
    {
        public CaldaChocolate(Bebida bebida) : base(bebida) { }

        public override string Descricao => _bebida.Descricao + ", Calda de Chocolate";
        public override double Custo() => _bebida.Custo() + 3.00;
    }
}