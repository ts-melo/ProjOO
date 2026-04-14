using NUnit.Framework;
using Cafeteria.Base;
using Cafeteria.Produtos;
using Cafeteria.DecoratorsConcretos;
using System.Runtime.CompilerServices;


namespace Cafeteria.Tests
{
    [TestFixture]

    public class BebidasTests
    {
        [Test]
        public void TestarExpresso()
        {
            Bebida bebida = new Expresso();
            Assert.That(bebida.Descricao, Is.EqualTo("Café expresso"));
            Assert.That(bebida.Custo(), Is.EqualTo(5.00));
        }

        [Test]
        public void TestarCha()
        {
            Bebida bebida = new Cha();
            Assert.That(bebida.Descricao, Is.EqualTo("Cha"));
            Assert.That(bebida.Custo(), Is.EqualTo(3.00));
        }

        [Test]
        public void TestarCappuccinoComCanela()
        {
            Bebida bebida = new Cappuccino();
            bebida = new Canela(bebida);
            Assert.That(bebida.Descricao, Is.EqualTo("Cappuccino, Canela"));
            Assert.That(bebida.Custo(), Is.EqualTo(7.00 + 0.50));
        }
    }

}