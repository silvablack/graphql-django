<template>
  <div class="list-filial">
    <div v-for="item in filiais" :key="item.id">
      <h3>{{ item.id }} - {{ item.descricao }} - {{item.empresa.descricao}} <a href="#" @click="loadFormFilial(item)">Editar</a> - <a href="#" @click="deleteFilial(item)">Excluir</a></h3>
    </div>

    <div class="add-filial">
      <div class="input">
      <input v-model="filial.codigo" placeholder="Código" />
      </div>
      <div class="input">
      <input v-model="filial.cnpj" placeholder="CNPJ" />
      </div>
      <div class="input">
      <input v-model="filial.descricao" placeholder="Descrição" />
      </div>
      <div class="input">
      <input v-model="filial.empresa.id" placeholder="Empresa ID" />
      </div>
      <div class="input">
      <input v-model="filial.empresa.codigo" placeholder="Empresa COD" />
      </div>
      <div class="input">
      <input v-model="filial.empresa.descricao" placeholder="Empresa Descricao" />
      </div>
      <h3>
        <a v-if="create" href="#" @click="addFilial">Adicionar Filial</a>
        <a v-if="edit" href="#" @click="editFilial">Atualizar Filial</a> 
      </h3>
    </div>
  </div>
</template>

<script>
import apolloClient from '../providers/graphql'
import gql from 'graphql-tag'

export default {
  name: 'Filiais',
  data: function() {
    return {
      create: true,
      edit: false,
      filiais: [],
      filial: {
        id: '',
        codigo: '',
        cnpj: '',
        descricao: '',
        ativo: '',
        empresa: {
            id: '',
            codigo: '',
            descricao: '',
            ativo: ''
        }
      }
    }
  },
  mounted() {
    this.getFiliais()
  },
  methods: {
    async getFiliais() {
      const res = await apolloClient.query({
        query: gql`
          query getFilial {
            filiais {
                id
                codigo
                descricao
                cnpj
                empresa{
                    id
                    descricao
                }
                ativo
            }
        }
        `
      })
      this.filiais = res.data.filiais
    },
    async deleteFilial(filial) {
      const res = await apolloClient.mutate({
        mutation: gql`
          mutation updateFilial($id: ID!, $descricao: String!, $codigo: Int!, $cnpj: String!, $empresa: ID!) {
            updateFilial(id: $id, input: {
              descricao: $descricao
              cnpj: $cnpj
              codigo: $codigo
              empresa: [{
                  id: $empresa 
              }]
              ativo: false
              }) {
              ok
              filial{
                id
                descricao
                cnpj
                codigo
                ativo
              }
            }
          }
        `,
        variables: {
          id: filial.id,
          codigo: filial.codigo,
          descricao: filial.descricao,
          cnpj: filial.cnpj,
          empresa: filial.empresa.id
        }
      })
      const index = this.filiais.findIndex((element)=>{
        return element.id == filial.id ? true : false
      })
      this.filiais.splice(index, 1)
    },
    loadFormFilial(filial) {
      this.filial = filial
      this.create = false
      this.edit = true
    },
    async editFilial() {
      const res = await apolloClient.mutate({
        mutation: gql`
          mutation updateEmpresa($id: ID!, $descricao: String!, $codigo: Int!, $ativo: Boolean!) {
            updateEmpresa(id: $id, input: {
              descricao: $descricao
              codigo: $codigo
              ativo: $ativo
              }) {
              ok
              empresa{
                id
                descricao
                codigo
                ativo
              }
            }
          }
        `,
        variables: {
          id: this.empresa.id,
          descricao: this.empresa.descricao,
          codigo: this.empresa.codigo,
          ativo: this.empresa.ativo
        }
      })
    },
    async addFilial() {
      const res = await apolloClient.mutate({
        mutation: gql`
            mutation createFilial($descricao: String!, $codigo: Int!, $cnpj: String!, $empresa: ID!) {
                createFilial(input: {
                    codigo: $codigo,
                    descricao: $descricao,
                    cnpj: $cnpj,
                    empresa: [{
                        id: $empresa
                    }]
                }) {
                    ok
                    filial {
                        id
                        codigo
                        cnpj
                        descricao
                        empresa{
                            descricao
                        }
                    }
                }
            }
        `,
        variables: {
          codigo: this.filial.codigo,
          descricao: this.filial.descricao,
          cnpj: this.filial.cnpj,
          empresa: this.filial.empresa.id
        }
      })
      this.filiais.push(res.data.createFilial.filial) 
      this.filiais.codigo = null
      this.filiais.descricao = null
      this.filiais.cnpj = null
      this.filiais.empresa.id = null
      this.filiais.empresa.codigo = null
      this.filiais.empresa.descricao = null
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.list-filial {
  width: 100%;
  margin: 5px;
}
.input{
  margin:5px;
}

.add-filial {
  width: 100%;
  margin: 10px;
  border: 1px solid #000;
  padding: 10px;
  border-radius: 5px 5px 5px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
