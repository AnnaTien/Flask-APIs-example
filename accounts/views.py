from flask import Flask, request
from flask_restplus import Resource, Api, Namespace, fields
import logging

accounts_namespace = Namespace("User Accounts App", path='/users', description='APIs of user accounts ')


class UserProfile(Resource):
    """
    API to generate token required for the token

    Example Input payload :


    Example Output :
        {
            "message" : "Ok user profile information retrieved successfully",
            "user" : {
                "first_name" : "Ravi",
                "last_name": "M",
                "email" : "ravi@example.com"
            }
        }
    """

    def mock_the_user_information(self):
        """
        # TODO - you can implement your own way of login with your favorite database;
        or even the inherent implementations of the Flask login; I'm not focusing on that

        :param username:
        :param password:
        :return:
        """
        return {
            "first_name": "Ravi",
            "last_name": "M",
            "email": "ravi@example.com"
        }

    def get(self):
        """
        API to get the user profile information

        :return:
        """
        payload_data = request.get_json()
        logging.debug("payload data is {}".format(payload_data))
        user_information = self.mock_the_user_information()
        return {"message": "Ok user profile information retrieved successfully", "user": user_information}


accounts_namespace.add_resource(UserProfile, "/profile")
