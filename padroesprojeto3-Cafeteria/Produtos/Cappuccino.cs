using System;
using Cafeteria.Base;

namespace Cafeteria.Produtos
{
    public class Cappuccino : Bebida
    {
        public Cappuccino() => Descricao = "Cappuccino";
        public override double Custo() => 7.00;
        
    }
}