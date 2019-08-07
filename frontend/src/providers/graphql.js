import { ApolloClient } from 'apollo-client'
import { createHttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'

const link = createHttpLink({
    uri: 'http://localhost:8000/graphql/'
})

const cache = new InMemoryCache()


const apolloClient = new ApolloClient({
    link,
    cache
})

export default apolloClient 
