import grpc
import passkit_io
import passkit_io.member
import passkit_io.member.a_rpc_pb2_grpc as member_grpc
from passkit_io.common.personal_pb2 import Person

from ..shared.grpc_connection import create_stubs


def enrol_member(program_id: str, tier_id: str, forename: str, surname: str, email: str) -> str:
    """Enrol a member into a program and return the member ID."""
    stubs = create_stubs()
    member = passkit_io.member.get_member_pb2().Member()
    member.programId = program_id
    member.tierId = tier_id

    person = Person()
    person.displayName = f"{forename} {surname}"
    person.surname = surname
    person.forename = forename
    person.emailAddress = email
    member.person.CopyFrom(person)

    try:
        response = stubs['members'].enrolMember(member)
        return response.id
    except grpc.RpcError as exc:
        raise RuntimeError(f"Failed to enrol member: {exc.details()}") from exc

