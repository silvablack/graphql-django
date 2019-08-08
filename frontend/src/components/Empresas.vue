<template>
  <div class="listEmpresa">
    <div v-for="item in empresas" :key="item.id">
      <h3>{{ item.id }} - {{ item.descricao }} <a href="#" @click="loadFormEmpresa(item)">Editar</a> - <a href="#" @click="deleteEmpresa(item)">Excluir</a></h3>
    </div>

    <div class="addEmpresa">
      <div class="input">
      <input v-model="empresa.codigo" placeholder="Código" />
      </div>
      <div class="input">
      <input v-model="empresa.descricao" placeholder="Descrição" />
      </div>
      <h3>
        <a v-if="create" href="#" @click="addEmpresa">Adicionar Empresa</a>
        <a v-if="edit" href="#" @click="editEmpresa">Atualizar Empresa</a> 
      </h3>
    </div>
  </div>
</template>

<script>
import apolloClient from '../providers/graphql'
import gql from 'graphql-tag'

export default {
  name: 'Empresas',
  data: function() {
    return {
      create: true,
      edit: false,
      empresas: [],
      empresa: {
        id: '',
        codigo: '',
        descricao: '',
        ativo: ''
      }
    }
  },
  mounted() {
    this.getEmpresas()
  },
  methods: {
    async getEmpresas() {
      const res = await apolloClient.query({
        query: gql`
          query getEmpresas {
            empresas {
              id
              codigo
              descricao
              ativo
            }
          }
        `
      })
      this.empresas = res.data.empresas
    },
    async deleteEmpresa(empresa) {
      const res = await apolloClient.mutate({
        mutation: gql`
          mutation updateEmpresa($id: ID!, $descricao: String!, $codigo: Int!) {
            updateEmpresa(id: $id, input: {
              descricao: $descricao
              codigo: $codigo
              ativo: false
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
          id: empresa.id,
          descricao: empresa.descricao,
          codigo: empresa.codigo
        }
      })
      const index = this.empresas.findIndex((element)=>{
        return element.id == empresa.id ? true : false
      })
      this.empresas.splice(index, 1)
    },
    loadFormEmpresa(empresa) {
      this.empresa = empresa
      this.create = false
      this.edit = true
    },
    async editEmpresa() {
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
    async addEmpresa() {
      const res = await apolloClient.mutate({
        mutation: gql`
          mutation createEmpresa($descricao: String!, $codigo: Int!) {
            createEmpresa(input: {
              codigo: $codigo
              descricao: $descricao
            }) {
              ok
              empresa {
                codigo
                descricao
              }
            }
          }
        `,
        variables: {
          codigo: this.empresa.codigo,
          descricao: this.empresa.descricao
        }
      })
      this.empresas.push(res.data.createEmpresa.empresa) 
      this.empresa.codigo = null
      this.empresa.descricao = null
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.listEmpresa {
  width: 100%;
  margin: 5px;
}
.input{
  margin:5px;
}
.addEmpresa {
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
