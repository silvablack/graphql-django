<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Empresas />
  </div>
</template>

<script>
import apolloClient from './providers/graphql'
import Empresas from './components/Empresas'
import gql from 'graphql-tag'

export default {
  name: 'app',
  components: {
    Empresas
  },
  data: function() {
    return {
      empresas: ''
    }
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
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
