using Cafeteria.Base;

namespace Cafeteria.Decorators
{
    public abstract class AddDecorator : Bebida
    {
        protected Bebida _bebida;

        protected AddDecorator(Bebida bebida)
        {
            _bebida = bebida;
            
        }
    }
}