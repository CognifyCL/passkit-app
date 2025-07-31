import grpc
import passkit_io.single_use_coupons.coupon_pb2 as coupon_pb2
import passkit_io.single_use_coupons.a_rpc_pb2_grpc as a_rpc_pb2_grpc
from passkit_io.common.personal_pb2 import Person


    # Read the CA, certificate, and private key files
    with open('../certs/ca-chain.pem', 'rb') as ca_file:
        root_certificates = ca_file.read()

    with open('../certs/certificate.pem', 'rb') as cert_file:
        certificate_chain = cert_file.read()

    with open('../certs/key.pem', 'rb') as key_file:
        private_key = key_file.read()

    # Create SSL credentials for gRPC
    credentials = grpc.ssl_channel_credentials(
        root_certificates=root_certificates,
        private_key=private_key,
        certificate_chain=certificate_chain
    )

    # Create a secure gRPC channel
    channel = grpc.secure_channel('grpc.pub1.passkit.io:443', credentials)

    # Create a stub
    couponsStub = a_rpc_pb2_grpc.SingleUseCouponsStub(channel)

    # Update coupon
    coupon = coupon_pb2.Coupon()
    coupon.id = ""
    coupon.offerId = ""  # Get offerId from createOffer call or dashboard
    coupon.campaignId = ""  # Get campaignId from createCampaign call or dashboard

    person = Person()
    person.displayName = "Percy PassKit"
    person.surname = "PassKit"
    person.forename = "Perc"
    person.emailAddress = ""

    coupon.person.CopyFrom(person)
    response = couponsStub.updateCoupon(coupon)
    print(response)


