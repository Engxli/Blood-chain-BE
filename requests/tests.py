import json
from functools import partial

import pytest
from django.contrib.auth import get_user_model
from graphene_django.utils.testing import graphql_query

from requests.models import Request


@pytest.fixture
@pytest.mark.django_db
def request_() -> Request:
    User = get_user_model()
    user1 = User.objects.create(username="user1", password="ILoveDjango!")
    user2 = User.objects.create(username="user2", password="ILoveDjango!")
    request = Request.objects.create(
        owner=user1,
        blood_type=Request.BloodType.Omin,
        severity=Request.Severity.HIGH,
        quantity=500,
        details="No details yet!",
    )
    request.donors.add(user1, user2)
    return request


@pytest.mark.django_db
def test_request_query(
    client_query: partial[graphql_query], request_: Request
) -> None:
    blood_type = {
        "A+": "A__1",
        "A-": "A_",
        "B+": "B__3",
        "B-": "B_",
        "O+": "O__5",
        "O-": "O_",
        "AB+": "AB__7",
        "AB-": "AB_",
    }
    response = client_query(
        f"""
        query{{
            request(id: {request_.id}) {{
                id
                createdAt
                modifiedAt
                owner {{
                id
                username
                }}
                bloodType
                severity
                quantity
                details
                donors {{
                id
                username
                }}
            }}
        }}
        """
    )
    content = json.loads(response.content)
    assert "errors" not in content
    data = content["data"]["request"]
    assert data["owner"]["id"] == str(request_.owner.id)
    assert data["owner"]["username"] in request_.owner.username
    assert data["bloodType"] in blood_type[request_.blood_type]
    assert data["severity"] in request_.severity
    assert data["quantity"] == request_.quantity
    assert data["details"] in request_.details
    for donor in data["donors"]:
        assert donor["id"] in [
            str(donors.id) for donors in request_.donors.all().iterator()
        ]
        assert donor["username"] in [
            donors.username for donors in request_.donors.all().iterator()
        ]


@pytest.fixture
@pytest.mark.django_db
def requests() -> list[Request]:
    User = get_user_model()
    user1 = User.objects.create(username="admin1", password="ILoveDjango!")
    user2 = User.objects.create(username="admin2", password="ILoveDjango!")
    user3 = User.objects.create(username="admin3", password="ILoveDjango!")
    request1 = Request.objects.create(
        owner=user1,
        blood_type=Request.BloodType.Omin,
        severity=Request.Severity.HIGH,
        quantity=500,
        details="No details yet!",
    )
    request1.donors.add(user1, user2)
    request2 = Request.objects.create(
        owner=user2,
        blood_type=Request.BloodType.Omin,
        severity=Request.Severity.HIGH,
        quantity=500,
        details="No details yet!",
    )
    request2.donors.add(user1, user3)

    return [request1, request2]


@pytest.mark.django_db
def test_requests_query(
    client_query: partial[graphql_query], requests: list[Request]
) -> None:
    blood_type = {
        "A+": "A__1",
        "A-": "A_",
        "B+": "B__3",
        "B-": "B_",
        "O+": "O__5",
        "O-": "O_",
        "AB+": "AB__7",
        "AB-": "AB_",
    }
    response = client_query(
        """
        query{
            requests {
                        id
                        createdAt
                        modifiedAt
                        owner {
                        id
                        username
                        }
                        bloodType
                        severity
                        quantity
                        details
                        donors {
                        id
                        username
                    }
                }
            }
        """
    )
    content = json.loads(response.content)

    assert "errors" not in content
    data = content["data"]["requests"]
    for request, data_request in zip(requests, data):
        assert data_request["owner"]["id"] == str(request.owner.id)
        assert data_request["owner"]["id"] == str(request.owner.id)
        assert data_request["owner"]["username"] in request.owner.username
        assert data_request["bloodType"] in blood_type[request.blood_type]
        assert data_request["severity"] in request.severity
        assert data_request["quantity"] == request.quantity
        assert data_request["details"] in request.details
        for donor in data_request["donors"]:
            assert donor["id"] in [
                str(donors.id) for donors in request.donors.all().iterator()
            ]
            assert donor["username"] in [
                donors.username for donors in request.donors.all().iterator()
            ]