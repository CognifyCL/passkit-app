import grpc

import passkit_io.member.a_rpc_pb2_grpc as members_grpc
import passkit_io.single_use_coupons.a_rpc_pb2_grpc as coupons_grpc
import passkit_io.core.a_rpc_templates_pb2_grpc as templates_grpc


from ..config import CA_FILE, CERT_FILE, KEY_FILE, HOST, PORT


def create_channel():
    """Create a secure gRPC channel using configured credentials."""
    with open(CA_FILE, 'rb') as ca_file, open(CERT_FILE, 'rb') as cert_file, open(KEY_FILE, 'rb') as key_file:
        credentials = grpc.ssl_channel_credentials(
            root_certificates=ca_file.read(),
            private_key=key_file.read(),
            certificate_chain=cert_file.read(),
        )
    return grpc.secure_channel(f"{HOST}:{PORT}", credentials)


def create_stubs(channel=None):
    """Return a dictionary of commonly used stubs."""
    if channel is None:
        channel = create_channel()
    return {
        'members': members_grpc.MembersStub(channel),
        'coupons': coupons_grpc.SingleUseCouponsStub(channel),
        # Only membership and coupon stubs are provided
        'templates': templates_grpc.TemplatesStub(channel),
    }
