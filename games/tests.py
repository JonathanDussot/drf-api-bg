from django.contrib.auth.models import User
from .models import Game
from rest_framework import status
from rest_framework.test import APITestCase


class GameListViewTests(APITestCase):
    """
    To test functionality with the Game model; listing games, logged in user
    can create games, and that a logged out user can't
    """
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_games(self):
        adam = User.objects.get(username='adam')
        Game.objects.create(owner=adam, title='a title')
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_game(self):
        self.client.login(username='adam', password='pass')
        response = self.client.game('/games/', {'title': 'a title'})
        count = Game.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_game(self):
        response = self.client.game('/games/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GameDetailViewTests(APITestCase):
    """
    To test each user can modify their own posts and noone else's
    """
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Game.objects.create(
            owner=adam, title='a title', content='adams content'
        )
        Game.objects.create(
            owner=brian, title='another title', content='brians content'
        )

    def test_can_retrieve_game_using_valid_id(self):
        response = self.client.get('/games/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_game_using_invalid_id(self):
        response = self.client.get('/games/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_game(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/games/1/', {'title': 'a new title'})
        game = Game.objects.filter(pk=1).first()
        self.assertEqual(game.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_game(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/games/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)