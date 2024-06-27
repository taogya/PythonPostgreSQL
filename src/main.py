

from models.user import User
from settings import Base, Session, engine

# テーブルが存在しない場合は作成
Base.metadata.create_all(engine)


def select_user(user_id: int):
    """ ユーザーを取得
    """
    with Session() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            print(f'Found user: {user.id}, {user.name}, {user.age}')
        else:
            print('User not found')


def create_user(name, age):
    """ ユーザーを作成
    """
    with Session() as session:
        user = User(name=name, age=age)
        session.add(user)
        session.commit()
        print(f'User created with id: {user.id}')


def update_user(user_id, name=None, age=None):
    """ ユーザーを更新
    """
    with Session() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.name = name or user.name
            user.age = age or user.age
            session.commit()
            print('User updated')
        else:
            print('User not found')


def remove_user(user_id):
    """ ユーザーを削除
    """
    with Session() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            print('User removed')
        else:
            print('User not found')


def main():
    # ユーザーを作成
    create_user('Alice', 25)
    create_user('Bob', 30)
    create_user('Charlie', 35)

    # ユーザーを取得
    select_user(1)
    select_user(2)
    select_user(3)

    # ユーザーを更新
    update_user(1, 'Alice2')
    update_user(2, age=31)

    # ユーザーを取得
    select_user(1)
    select_user(2)
    select_user(3)

    # ユーザーを削除
    remove_user(3)

    # ユーザーを取得
    select_user(1)
    select_user(2)
    select_user(3)


if __name__ == '__main__':
    main()
