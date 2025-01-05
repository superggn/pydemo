from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorldView(APIView):
    @extend_schema(
        summary="Say Hello",
        description="Returns a friendly greeting.",
        responses={200: 'A friendly message'}
    )
    def get(self, request):
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Post Hello",
        description="Post Returns a friendly greeting.",
        responses={200: 'Post A friendly message'}
    )
    def post(self, request):
        return Response({"message": "Hello, this is post!"}, status=status.HTTP_200_OK)


class EchoView(APIView):
    @extend_schema(
        summary="summary is Echo Input",
        description="description is Echos back the input provided.",
        request={"type": "object", "properties": {"input": {"type": "string"}}},
        responses={200: 'response is Echoed input'}
    )
    def post(self, request):
        input_text = request.data.get("input", "No input provided")
        return Response({"echo": input_text}, status=status.HTTP_200_OK)


# from drf_spectacular.utils import extend_schema, OpenApiExample
# from rest_framework.views import APIView
# from rest_framework.response import Response

class MyRequestSerializer(serializers.Serializer):
    my_field = serializers.CharField()


@extend_schema(
    summary="Example API with request and response examples",
    description="This API demonstrates how to include request and response examples.",
    request=MyRequestSerializer,
    examples=[
        OpenApiExample(
            name="Example Request - 1",
            description="description: An example of a valid request",
            value={"input_key": "high land"},
            request_only=True,  # 表示这是一个请求示例
        ),
        OpenApiExample(
            name="Example Request - 2",
            description="description: SkyWalker",
            value={"input_key": "I'm on the high ground"},
            request_only=True,  # 表示这是一个请求示例
        ),
        OpenApiExample(
            name="Example Response - 1",
            description="description response - 1",
            value={"output_key": "1"},
            response_only=True,  # 表示这是一个响应示例
        ),
        OpenApiExample(
            name="Example Response - x",
            description="description response - x",
            value={"output_key": "output_value xxx"},
            response_only=True,  # 表示这是一个响应示例
        ),
    ],
    # responses=None,
    responses={
        200: "Success response example",
    },
)
class ExampleView(APIView):
    def post(self, request):
        # 假装处理逻辑
        return Response({"output_key": "output_value view view view"})
