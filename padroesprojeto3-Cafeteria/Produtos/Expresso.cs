using Cafeteria.Base;

namespace Cafeteria.Produtos
{
    public class Expresso : Bebida
    {
        public Expresso() => Descricao = "Café expresso";
        public override double Custo() => 5.00;
        
    }
}