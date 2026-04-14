using System;
using Cafeteria.Base;

namespace Cafeteria.Produtos
{
    public class Cha : Bebida
    {
        public Cha() => Descricao = "Cha";
        public override double Custo() => 3.00;
        
    }
}