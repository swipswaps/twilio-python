# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ServiceTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.notify.v1.services.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://notify.twilio.com/v1/Services',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "733c7f0f-6541-42ec-84ce-e2ae1cac588c",
                "date_created": "2016-03-09T20:22:31Z",
                "date_updated": "2016-03-09T20:22:31Z",
                "apn_credential_sid": null,
                "gcm_credential_sid": null,
                "fcm_credential_sid": null,
                "messaging_service_sid": null,
                "facebook_messenger_page_id": "4",
                "alexa_skill_id": null,
                "default_apn_notification_protocol_version": "3",
                "default_gcm_notification_protocol_version": "3",
                "default_fcm_notification_protocol_version": "3",
                "default_alexa_notification_protocol_version": "3",
                "log_enabled": true,
                "type": "S",
                "delivery_callback_url": "Hello",
                "delivery_callback_enabled": true,
                "url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "bindings": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings",
                    "notifications": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications",
                    "segments": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Segments",
                    "users": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users"
                }
            }
            '''
        ))

        actual = self.client.notify.v1.services.create()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://notify.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://notify.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "733c7f0f-6541-42ec-84ce-e2ae1cac588c",
                "date_created": "2016-03-09T20:22:31Z",
                "date_updated": "2016-03-09T20:22:31Z",
                "apn_credential_sid": null,
                "gcm_credential_sid": null,
                "fcm_credential_sid": null,
                "messaging_service_sid": null,
                "facebook_messenger_page_id": "4",
                "alexa_skill_id": null,
                "default_apn_notification_protocol_version": "3",
                "default_gcm_notification_protocol_version": "3",
                "default_fcm_notification_protocol_version": "3",
                "default_alexa_notification_protocol_version": "3",
                "log_enabled": true,
                "type": "S",
                "delivery_callback_url": "Hello",
                "delivery_callback_enabled": true,
                "url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "bindings": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings",
                    "notifications": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications",
                    "segments": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Segments",
                    "users": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users"
                }
            }
            '''
        ))

        actual = self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.notify.v1.services.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://notify.twilio.com/v1/Services',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://notify.twilio.com/v1/Services?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://notify.twilio.com/v1/Services?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "services"
                },
                "services": [
                    {
                        "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "733c7f0f-6541-42ec-84ce-e2ae1cac588c",
                        "date_created": "2016-03-09T20:22:31Z",
                        "date_updated": "2016-03-09T20:22:31Z",
                        "apn_credential_sid": null,
                        "gcm_credential_sid": null,
                        "fcm_credential_sid": null,
                        "messaging_service_sid": null,
                        "facebook_messenger_page_id": "4",
                        "alexa_skill_id": null,
                        "default_apn_notification_protocol_version": "3",
                        "default_gcm_notification_protocol_version": "3",
                        "default_fcm_notification_protocol_version": "3",
                        "default_alexa_notification_protocol_version": "3",
                        "log_enabled": true,
                        "type": "S",
                        "delivery_callback_url": "Hello",
                        "delivery_callback_enabled": true,
                        "url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "bindings": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings",
                            "notifications": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications",
                            "segments": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Segments",
                            "users": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.notify.v1.services.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://notify.twilio.com/v1/Services?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://notify.twilio.com/v1/Services?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "services"
                },
                "services": []
            }
            '''
        ))

        actual = self.client.notify.v1.services.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://notify.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "733c7f0f-6541-42ec-84ce-e2ae1cac588c",
                "date_created": "2016-03-09T20:22:31Z",
                "date_updated": "2016-03-09T20:22:31Z",
                "apn_credential_sid": null,
                "gcm_credential_sid": null,
                "fcm_credential_sid": null,
                "default_apn_notification_protocol_version": "3",
                "default_gcm_notification_protocol_version": "3",
                "default_fcm_notification_protocol_version": "3",
                "default_alexa_notification_protocol_version": "3",
                "messaging_service_sid": null,
                "alexa_skill_id": null,
                "facebook_messenger_page_id": "4",
                "log_enabled": true,
                "type": "S",
                "delivery_callback_url": "Hello",
                "delivery_callback_enabled": true,
                "url": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "bindings": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings",
                    "notifications": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications",
                    "segments": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Segments",
                    "users": "https://notify.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users"
                }
            }
            '''
        ))

        actual = self.client.notify.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
