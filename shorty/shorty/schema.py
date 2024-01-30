import graphene
import shortener.graphql.schema

class Query(shortener.graphql.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)