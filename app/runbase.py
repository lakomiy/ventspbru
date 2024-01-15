from models.models import Base, Session
from models.user import User
from models.post import Post
from models.collback_db import CollbackDb

from sqlalchemy.orm import Session as SessionType, joinedload


def create_user(session: SessionType, username: str, is_staff=False) -> User:
    user = User(username=username, is_staff=is_staff)
    session.add(user)
    session.commit()
    return user




def get_all_users(session: SessionType) -> list[User]:
    users = session.query(User).all()
    return users


def show_users(session: SessionType):
    users = get_all_users(session)
    for user in users:
        print(user)


def callback_db(session: SessionType, username:str, phonenumber:str):
    user_callback = CollbackDb(username=username, phonenumber=phonenumber)
    session.add(user_callback)
    session.commit()
    return user_callback








# def create_posts(session: SessionType, author: Author, *titles: str) -> list[Post]:
#     posts = [Post(author=author, title=title) for title in titles]
#     session.add_all(posts)
#     session.commit()
#     return posts


# def get_posts_with_authors_and_users(session: SessionType):
#     posts = (
#         session.query(Post)
#         .options(
#             joinedload(Post.author).joinedload(Author.user),
#         )
#         .all()
#     )
#     for post in posts:
#         print("-----")
#         print(post)
#         print("*", post.author)
#         print("+++", post.author.user)


def main():
    session: SessionType = Session()
    # john = create_user(session, "john")
    # author = create_author(session, john, "John Smith")
    # print(john)
    # print(author)

    # admin = create_user(session, "admin", is_staff=True)
    # nick = create_user(session, "nick")
    # bob = create_user(session, "bob")
    # author_bob = create_author(session, bob, "Bob Black")
    # show_users(session)
    # show_users_with_authors(session)
    # show_authors_with_users(session)
    # author_bob = find_author_by_user_username(session, "bob")
    # author_john = find_author_by_user_username(session, "john")
    #
    # create_posts(session, author_john, "L1", "L2")
    # create_posts(session, author_bob, "Lesson SQL", "Lesson PG")
    # get_posts_with_authors_and_users(session)
    # Vasy = callback_db(session, "Vasy", '+79627205448')

    session.close()


if __name__ == "__main__":
    # Base.metadata.drop_all()
    Base.metadata.create_all()
    # print(Base.metadata.tables)
    main()