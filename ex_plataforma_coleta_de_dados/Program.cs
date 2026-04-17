using System;

namespace SistemaMonitoramentoAmazonia
{
    class Program
    {
        static void Main(string[] args)
        {
            PCD pcd1 = new PCD("PCD1");
            Universidades uniSJC = new Universidades("UNIFESP");
            Universidades uniSP = new Universidades("USP");
            Universidades uniRJ = new Universidades("UFRJ");

//faculdades registram interesse em receber dados de determinados PCDs
            pcdSP.RegistrarInteresse(uniSJC);
            pcdRJ.RegistrarInteresse(uniSP);
            pcdSJC.RegistrarInteresse(uniRJ);
//PCDs recebem novas medições e notificam as faculdades interessadas
            pcdSJC.setMedicoes(30.5, 6.8, 80);
        }
    }
}