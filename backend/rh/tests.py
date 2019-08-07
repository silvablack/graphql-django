from django.test import TestCase
from graphene.test import Client
from rh.schema import schema


class APITestCase(TestCase):

    def test_empresas(self):
        client = Client(schema)
        executed = client.execute('''
        query getEmpresas {
              empresas {
                id
                codigo
                descricao   
              }
            }
        ''')
        assert executed == {
            'data': {
                'empresas': 'hello!'
            }
        }