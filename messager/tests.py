import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from messager.models import Message


class Tests:

    @pytest.mark.django_db
    def test_message_creation(self):
        message = Message.objects.create(title='title1', content='content1')
        assert (message.title == 'title1')
        assert (message.content == 'content1')
        assert (message.view_counter == 0)
        assert (Message.objects.all().count() == 1)
        # if all assertions succeded, it means we successfully created a new Message object

    @pytest.mark.django_db
    def test_message_creation_with_message_length_exceeding_limit(self):
        with pytest.raises(Exception):
            Message.objects.create(title='test title', content='A' * 161)
        assert (Message.objects.all().count() == 0)
        # we assert that the creation of message with content longer than 160 characters is impossible

    @pytest.mark.django_db
    def test_API_root(self):
        client = APIClient()
        response = client.get('')
        data = response.data
        assert (data['messages'] == 'http://testserver/messages/')
        # the API root only leads to messages

    @pytest.mark.django_db
    def test_API_empty_messages(self):
        client = APIClient()
        response = client.get('/messages/')
        data = response.data
        assert (len(data) == 0)
        # the data should be empty

    @pytest.mark.django_db
    def test_API_with_inserted_messages_in_system(self):
        Message.objects.create(title='title1', content='content1')
        Message.objects.create(title='title2', content='content2')
        client = APIClient()
        response = client.get('/messages/')
        data = response.data
        message1 = data[0]
        message2 = data[1]
        assert (message1['title'] == 'title1')
        assert (message1['url'] == 'http://testserver/messages/1/')
        assert (message1['view_counter'] == 0)
        assert (message2['title'] == 'title2')
        assert (message2['url'] == 'http://testserver/messages/2/')
        assert (message2['view_counter'] == 0)
        # we check whether we can get 2 messages, which were previously inserted

    @pytest.mark.django_db
    def test_message_creation_without_authentication(self):
        client = APIClient()
        response = client.post('/messages/', {"title": "title1", "content": "content1"})
        assert (response.status_code == 403)
        # the server should return 403 since the access to message creation is forbidden without login

    @pytest.mark.django_db
    def test_message_creation_with_authentication(self):
        User.objects.create_user(
            username='test',
            password='testpass',
        )
        client = APIClient()
        client.login(username='test', password='testpass')
        response = client.post('/messages/', {"title": "title1", "content": "content1"})
        assert (response.status_code == 201)  # 201 means created
        assert (Message.objects.all().count() == 1)
        data = response.data
        assert (data['title'] == 'title1')
        assert (data['content'] == 'content1')
        assert (data['view_counter'] == 0)
        # the message creation should succeed, since we logged in

    @pytest.mark.django_db
    def test_message_retrieval_without_authentication(self):
        client = APIClient()
        Message.objects.create(title='title1', content='content1')
        response = client.get('/messages/1/')
        data = response.data
        assert (data['title'] == 'title1')
        assert (data['content'] == 'content1')
        assert (data['view_counter'] == 0)
        # we should be able to retrieve message details without authentication

    @pytest.mark.django_db
    def test_message_destruction_without_authentication(self):
        Message.objects.create(title='title1', content='content1')

        client = APIClient()
        response = client.delete('/messages/1/')
        assert (response.status_code == 403)
        # the server should return 403 since the access to message destruction is forbidden without login

    @pytest.mark.django_db
    def test_message_destruction_with_authentication(self):
        User.objects.create_user(
            username='test',
            password='testpass',
        )
        Message.objects.create(title='title1', content='content1')
        client = APIClient()
        client.login(username='test', password='testpass')
        response = client.delete('/messages/1/')
        assert (response.status_code == 204)
        # 204 means there's no content to display, but the delete was successful

    @pytest.mark.django_db
    def test_nonexistent_message_destruction_with_authentication(self):
        User.objects.create_user(
            username='test',
            password='testpass',
        )
        client = APIClient()
        client.login(username='test', password='testpass')
        response = client.delete('/messages/1/')
        assert (response.status_code == 404)
        # the server should return 404, which indicates that there is no such message
