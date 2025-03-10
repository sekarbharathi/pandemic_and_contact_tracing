# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import contact_tracing_pb2 as contact__tracing__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in contact_tracing_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ContactTracingServiceStub(object):
    """The ContactTracing service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendOutbreakLocation = channel.unary_unary(
                '/contact_tracing.ContactTracingService/SendOutbreakLocation',
                request_serializer=contact__tracing__pb2.OutbreakLocationRequest.SerializeToString,
                response_deserializer=contact__tracing__pb2.OutbreakLocationResponse.FromString,
                _registered_method=True)


class ContactTracingServiceServicer(object):
    """The ContactTracing service definition
    """

    def SendOutbreakLocation(self, request, context):
        """Sends the outbreak location and returns users in that location
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContactTracingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendOutbreakLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.SendOutbreakLocation,
                    request_deserializer=contact__tracing__pb2.OutbreakLocationRequest.FromString,
                    response_serializer=contact__tracing__pb2.OutbreakLocationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'contact_tracing.ContactTracingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('contact_tracing.ContactTracingService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ContactTracingService(object):
    """The ContactTracing service definition
    """

    @staticmethod
    def SendOutbreakLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/contact_tracing.ContactTracingService/SendOutbreakLocation',
            contact__tracing__pb2.OutbreakLocationRequest.SerializeToString,
            contact__tracing__pb2.OutbreakLocationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
