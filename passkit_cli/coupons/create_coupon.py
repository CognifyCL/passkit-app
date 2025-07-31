import grpc
import passkit_io.single_use_coupons.coupon_pb2 as coupon_pb2
import passkit_io.single_use_coupons.a_rpc_pb2_grpc as coupons_grpc
from passkit_io.common.personal_pb2 import Person

from ..shared.grpc_connection import create_stubs


def create_coupon(campaign_id: str, offer_id: str, forename: str, surname: str, email: str) -> str:
    """Create a coupon and return its ID."""
    stubs = create_stubs()
    coupon = coupon_pb2.Coupon()
    coupon.offerId = offer_id
    coupon.campaignId = campaign_id

    person = Person()
    person.displayName = f"{forename} {surname}"
    person.surname = surname
    person.forename = forename
    person.emailAddress = email
    coupon.person.CopyFrom(person)

    response = stubs['coupons'].createCoupon(coupon)
    return response.id

