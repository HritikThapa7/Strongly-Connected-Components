from neomodel import StructuredNode, UniqueIdProperty, RelationshipTo, RelationshipFrom, config

config.DATABASE_URL = 'bolt://neo4j:neo4j@hritik@127.0.0.1:7687'

class User(StructuredNode):
    title = UniqueIdProperty()
    follow = RelationshipTo('User', 'FOLLOWS')

   




if __name__ == "__main__":
    with open("i.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            a, b = [c.strip() for c in line.split()][:2]
            user1 = User(title= str(a)).save()
            user2 = User(title=str(b)).save()
            user1.follow.connect(user2)
