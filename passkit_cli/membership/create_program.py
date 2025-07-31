import grpc
import passkit_io.member
import passkit_io.member.a_rpc_pb2_grpc as member_grpc
from passkit_io.common.project_pb2 import ProjectStatus

from ..shared.grpc_connection import create_stubs


def create_program(name: str = "Quickstart Program") -> str:
    """Create a membership program and return its ID."""
    stubs = create_stubs()
    program = passkit_io.member.get_program_pb2().Program()
    program.name = name
    program.status.extend(["PROJECT_ACTIVE_FOR_OBJECT_CREATION", "PROJECT_DRAFT"])

    try:
        response = stubs['members'].createProgram(program)
        return response.id
    except grpc.RpcError as exc:
        raise RuntimeError(f"Failed to create program: {exc.details()}") from exc

