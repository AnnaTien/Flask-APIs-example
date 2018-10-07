from flask import Flask, request
from flask_restplus import Resource, Api, Namespace, fields
import logging

auth_namespace = Namespace("Auth App", path='/auth', description='APIs for authentication ')

auth_login_fields = auth_namespace.model('LoginAPIPayload', {
    'username': fields.String,
    'password': fields.String
})


class LoginAPIView(Resource):
    """
    API to generate token required for the token

    Example Input payload :
        payload = {
            "username": "MyUsername",
            "password": "SecretPassword",
        }

    Example Output :
        {
            "message" : "Token generated successfully",
            "token" : "xxxzzzzzyyyy.......aaabaaaaabbbbbb1111"
        }
    """

    def mock_the_login(self, username=None, password=None):
        """
        # TODO - you can implement your own way of login with your favorite database;
        or even the inherent implementations of the Flask login; I'm not focusing on that

        :param username:
        :param password:
        :return:
        """
        return "{}-{}".format(username, password)

    @auth_namespace.expect(auth_login_fields)
    def post(self):
        """
        To generate the auth token, from the username and password

        :return:
        """
        payload_data = request.get_json()
        logging.debug("payload data is {}".format(payload_data))
        token = self.mock_the_login(
            username=payload_data.get("username"),
            password=payload_data.get("password")
        )
        return {"message": "Token generated successfully", "token": token}


auth_namespace.add_resource(LoginAPIView, "/login")
