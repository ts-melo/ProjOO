using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    //singleton
    public class SistemaConfig
    {
        private static SistemaConfig _instance;
        public string NomeApp { get; set; } = "notificador";
        public int MaxTent { get; set; } = 3;

        private SistemaConfig() { }

        public static SistemaConfig GetInstance()
        {
            if (_instance == null)
            {
                _instance = new SistemaConfig();
            }
            return _instance;
        }
    }
}
