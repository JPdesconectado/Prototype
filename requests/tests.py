from django.test import TestCase
from .models import SolicitacaoTransito, SolicitacaoEducacao, SolicitacaoIluminacao, SolicitacaoUPA, Endereco
from users.models import ProfileUser
from users.tests import create_user

def criar_endereco(bairro, rua, numero, complemento):
    endereco = Endereco.objects.create(bairro = bairro, rua = rua, numero = numero, complemento = complemento)
    return endereco

class SolicitacaoTransitoTestCase(TestCase):
    def setUp(self):
        endereco = criar_endereco('Centro', 'Espadinha', 267, 'apartamento')
        user = create_user('jhony')
        SolicitacaoTransito.objects.create(nome = user, tipo = 'Sinalização', endereco = endereco,  imagem = '',  comentario ='')

    def test_transito(self):
        user = ProfileUser.objects.get(username='jhony')
        endereco = Endereco.objects.get(bairro = 'Centro', rua = 'Espadinha')
        transito = SolicitacaoTransito.objects.get(nome = user, tipo = 'Sinalização')
        self.assertEqual(transito.tipo, 'Sinalização')
        self.assertEqual(user.username, 'jhony')
        self.assertEqual(endereco.bairro, 'Centro')


class SolicitacaoEducacaoTestCase(TestCase):
    def setUp(self):
        user = create_user('jhony')
        SolicitacaoEducacao.objects.create(nome = user, cadastro_pf = '09228901969', rg = '345823', comentario = '')

    def test_educacao(self):
        user = ProfileUser.objects.get(username='jhony')
        educacao = SolicitacaoEducacao.objects.get(nome = user, rg = '345823')
        self.assertEqual(user.username, 'jhony')
        self.assertEqual(educacao.cadastro_pf, '09228901969')

class SolicitacaoIluminacaoTestCase(TestCase):
    def setUp(self):
        user = create_user('jhony')
        SolicitacaoIluminacao.objects.create(nome = user, conta_luz = 'arquivo/contaluz.pdf',  rg = '345823')
         
    def test_iluminacao(self):
         user = ProfileUser.objects.get(username='jhony')
         iluminacao = SolicitacaoIluminacao.objects.get(nome = user, rg='345823')
         self.assertEqual(user.username, 'jhony')
         self.assertEqual(iluminacao.conta_luz, 'arquivo/contaluz.pdf')

class SolicitacaoUpaTestCase(TestCase):
    def setUp(self):
        user = create_user('jhony')
        SolicitacaoUPA.objects.create(nome = user, rg = '345823', card_sus = '203354673', comprovante_residencia = 'arquivo/contaAgua.pdf') 

    def test_upa(self):
        user = ProfileUser.objects.get(username='jhony') 
        upa = SolicitacaoUPA.objects.get(nome = user, rg = '345823')
        self.assertEqual(user.username, 'jhony')
        self.assertEqual(upa.comprovante_residencia, 'arquivo/contaAgua.pdf')
        self.assertEqual(upa.card_sus, '203354673')
                      
class EnderecoTestCase(TestCase):
    def setUp(self):
        endereco = criar_endereco(bairro ='Centro', rua = 'Expedicionários', numero = 14, complemento = 'casa')

    def test_endereco(self):
        endereco = Endereco.objects.get(bairro = 'Centro', rua = 'Expedicionários')
        self.assertEqual(endereco.bairro, 'Centro')