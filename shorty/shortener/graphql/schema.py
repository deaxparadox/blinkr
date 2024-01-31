import graphene
from graphene_django import DjangoObjectType


# This will be used to filter the database
from django.db.models import Q

from shortener.models import URL
from shortener.models import URL

class URLType(DjangoObjectType):
    """
    Create a new GraphQL tpe for the `URL` model by adding the following lines.
    """
    class Meta:
        model = URL


class Query(graphene.ObjectType):
    """
    Create a Query type for the `URL` model

    This code creates a Query class with one field named `urls`, which is a list of 
    previously defined `URLType`. When resolving the Query through the `resolve_urls` method, 
    you return all the URLs stored in the database. 


    For url query filterations: the following query search for all the urls
    consisting of "learn" keyword:

    query {
        urls(url:"learn") {
            fullUrl,
            urlHash,
            clicks,
            createdAt
        }
    }

    For pagination, issue the following query:

    query {
        urls(first: 2, skip: 1) {
            id
            fullUrl
            urlHash
            clicks
            createdAt
        }
    }

    """

    urls = graphene.List(
        URLType,
        url=graphene.String(),       # for database queries
        first=graphene.Int(),
        skip=graphene.Int(),
    )

    def resolve_urls(
        self, 
        info,
        url=None,                   # for database queries
        first=None,
        skip=None,
        **kwargs
    ):
        queryset =  URL.objects.all()

        # filtering the urls in the database
        if url:
            _filter = Q(full_url__icontains=url)
            queryset = queryset.filter(_filter)

        if first:
            queryset = queryset[:first]
        if skip:
            queryset = queryset[skip:]

        return queryset
    


class CreateURL(graphene.Mutation):
    """
    This class inherits the `graphene.Mutation` helper to have the capabilities of a GraphQL Mutation. 
    It also has a property name `url`, defining the content returned by the server after the Mutation is completed.
    In this case, it will be the `URLType` data structure.
    """

    url = graphene.Field(URLType)

    class Arguments:
        """
        This defines what data will be accept by the server.
        Here, you are expecting a parameter named `full_url` and a `String` content. 
        """
        full_url =graphene.String()

    

    def mutate(self, info, full_url):
        """
        This `mutate` method does a lot of the work by receiving the data from the client and saving it to the database. In the end, it returns the class itself containing the newly created item.
        """
        url = URL(full_url=full_url)
        url.save()

        return CreateURL(url=url)


class Mutation(graphene.ObjectType):
    """
    Create a Mutation class to hold all the Mutations for your app by adding these lines
    """
    create_url = CreateURL.Field()






# NOTE: All the query must be added to the main Schema `shorty.schema.py`