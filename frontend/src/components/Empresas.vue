<template>
  <div class="empresa">
    <div v-for="item in empresas" :key="item.id">
      <h3>{{ item.codigo }} - {{ item.descricao }} <a href="#" @click="editEmpresa">Editar</a> - <a href="#" @click="deleteEmpresa">Excluir</a></h3>
    </div>

    <div>
      <h3><a href="#" @click="addEmpresa">Adicionar Empresa</a> </h3>
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
      empresas: ''
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
              codigo
              descricao
            }
          }
        `
      })
      this.empresas = res.data.empresas
    },
    async deleteEmpresa() {
      const res = await apolloClient.query({
        query: gql`
          query getEmpresas {
            empresas {
              codigo
              descricao
            }
          }
        `
      })
      this.empresas = res.data.empresas
    },
    editEmpresa() {

    },
    addEmpresa() {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
