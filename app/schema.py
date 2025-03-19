import graphene
from app.mutations import RegisterMutation, LoginMutation, LogoutMutation

class Mutation(graphene.ObjectType):
    register = RegisterMutation.Field()
    login = LoginMutation.Field()
    logout = LogoutMutation.Field()

schema = graphene.Schema(mutation=Mutation)
