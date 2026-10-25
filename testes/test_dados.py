"""Seus testes do Marco 1 (veja a seção 6 do ENUNCIADO_MARCO1.md).

Regras: pelo menos 8 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou np.allclose.
"""
import unittest
import numpy as np

from elevatoria import dados
from elevatoria.dados import por_tag
from elevatoria.serie import SerieTemporal


class TestPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, por_tag devolve uma lista vazia."""
        self.assertEqual(por_tag([], "PT101"), [])

class TestMediaMovelRegressao(unittest.TestCase):
    """na issue 4, media_movel estava devolvendo um valor a menos."""

    def teste_tamanho_600_janela_30(self):
        """como relatado, deveria dar 571 valores"""
        s = SerieTemporal.de_lista(np.arange(600.0))
        self.assertEqual(len(s.media_movel(30)),571)

    def teste_janela_igual_ao_tamanho(self):
        """a janela do tamanho da série precisar dar o valor da média do tubo"""
        s = SerieTemporal.de_lista([2.0,4.0,6.0,8.0])
        r = s.media_movel(4)
        self.assertEqual(len(r),1)
        self.assertAlmostEqual(float(r[0]),5.0)

    def teste_primeira_janela_entra_no_resultado(self):
        """o primeiro valor precisa ser a média de self[0:janela]"""
        s = SerieTemporal.de_lista([1.0,2.0,3.0,10.0,20.0])
        self.assertTrue(np.allclose(s.media_movel(3),[2.0,5.0,11.0]))

    def teste_janela_um_devolve_a_propria_serie(self):
        """a janela 1 devolve a mesma série, porque não 'suaviza' nada"""
        s = SerieTemporal.de_lista([3.0,1.0,4.0,1.0,5.0])
        self.assertTrue(np.allclose(s.media_movel(1),s))
        

# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #4 (escreva-os ANTES de corrigir o defeito e confirme que falham).


if __name__ == "__main__":
    unittest.main()
