import graphene
import rh.schema


class Query(rh.schema.Query, graphene.ObjectType):
    pass


class Mutation(rh.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)