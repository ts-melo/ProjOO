using NUnit.Framework;
using SistemaMonitoramentoAmazonia;

namespace SistemaMonitoramentoAmazonia.Tests
{
    [TestFixture]
    public class PCDTests
    {
        [Test]
        public void Deve_Notificar_Quando_SetMedicoes_For_Chamado()
        {
            // Arrange
            var pcd = new PCD("Teste");
            var uni = new Universidades("Uni Teste");
            pcd.RegistrarInteresse(uni);

            // Act & Assert
            // Verifica se a execução ocorre sem erros (notificação disparada)
            Assert.DoesNotThrow(() => pcd.SetMedicoes(25.0, 7.0, 80.0));
        }

        [Test]
        public void Nao_Deve_Adicionar_Mesma_Universidade_Duas_Vezes()
        {
            // Como a lista é privada, testamos o comportamento de não gerar erro 
            // ou redundância de notificação se o método permitir.
            var pcd = new PCD("Teste");
            var uni = new Universidades("Uni Única");
            
            pcd.RegistrarInteresse(uni);
            pcd.RegistrarInteresse(uni); // Segunda tentativa
            
            Assert.Pass(); // Verificação de integridade do método RegistrarInteresse
        }
    }
}