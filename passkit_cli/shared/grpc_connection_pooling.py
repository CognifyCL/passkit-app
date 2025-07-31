import grpc
import threading

import passkit_io.member.a_rpc_pb2_grpc as members_grpc
import passkit_io.single_use_coupons.a_rpc_pb2_grpc as coupons_grpc
import passkit_io.core.a_rpc_templates_pb2_grpc as templates_grpc

from ..config import CA_FILE, CERT_FILE, KEY_FILE, HOST, PORT


def build_credentials():
    with open(CA_FILE, 'rb') as ca_file, open(CERT_FILE, 'rb') as cert_file, open(KEY_FILE, 'rb') as key_file:
        return grpc.ssl_channel_credentials(
            root_certificates=ca_file.read(),
            private_key=key_file.read(),
            certificate_chain=cert_file.read(),
        )


def grpc_connection_pool(pool_size: int = 5):
    """Yield stubs from a pool of channels."""
    credentials = build_credentials()
    channel_pool = [grpc.secure_channel(f"{HOST}:{PORT}", credentials) for _ in range(pool_size)]
    lock = threading.Lock()
    index = 0

    def get_stubs():
        nonlocal index
        with lock:
            channel = channel_pool[index]
            index = (index + 1) % pool_size
        return {
            'members': members_grpc.MembersStub(channel),
            'coupons': coupons_grpc.SingleUseCouponsStub(channel),
            'templates': templates_grpc.TemplatesStub(channel),
        }

    try:
        yield get_stubs
    finally:
        for channel in channel_pool:
            channel.close()

