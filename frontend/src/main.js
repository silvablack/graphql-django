import Vue from 'vue'
import App from './App.vue'

import VueApollo from 'vue-apollo'
import apolloClient from './providers/graphql'

Vue.use(VueApollo)
Vue.config.productionTip = false

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

new Vue({
  apolloProvider,
  render: h => h(App)
}).$mount('#app')
