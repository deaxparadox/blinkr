import graphene
from graphene_django import DjangoObjectType


from shortener.models import URL


"""
Create a new GraphQL tpe for the `URL` model by adding the following lines.
"""
class URLType(DjangoObjectType):
    class Meta:
        model = URL


"""
Create a Query type for the `URL` model

This code creates a Query class with one field named `urls`, which is a list of 
previously defined `URLType`. When resolving the Query through the `resolve_urls` method, 
you return all the URLs stored in the database. 
"""
class Query(graphene.ObjectType):
    urls = graphene.List(URLType)

    def resolve_urls(self, info, **kwargs):
        return URL.objects.all()


"""
This class inherits the `graphene.Mutation` helper to have the capabilities of a GraphQL Mutation. 
It also has a property name `url`, defining the content returned by the server after the Mutation is completed.
In this case, it will be the `URLType` data structure.
"""
class CreateURL(graphene.Mutation):
    url = graphene.Field(URLType)

    """
    This defines what data will be accept by the server.
    Here, you are expecting a parameter named `full_url` and a `String` content. 
    """
    class Arguments:
        full_url =graphene.String()

    
    """
    This `mutate` method does a lot of the work by receiving the data from the client and saving it to the database. In the end, it returns the class itself containing the newly created item.
    """
    def mutate(self, info, full_url):
        url = URL(full_url=full_url)
        url.save()
        return CreateURL(url=url)


"""
Create a Mutation class to hold all the Mutations for your app by adding these lines
"""
class Mutation(graphene.ObjectType):
    create_url = CreateURL.Field()






# NOTE: All the query must be added to the main Schema `shorty.schema.py`