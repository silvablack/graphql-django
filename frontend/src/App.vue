<template>
  <div id="app">
    <img alt="Vue logo" style="width:100px" src="./assets/logo.png">
    <Empresas />
    <Filiais />
  </div>
</template>

<script>
import apolloClient from './providers/graphql'
import Empresas from './components/Empresas'
import Filiais from './components/Filiais'
import gql from 'graphql-tag'

export default {
  name: 'app',
  components: {
    Empresas,
    Filiais
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
  margin-top: 20px;
}
</style>
