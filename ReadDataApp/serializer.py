from rest_framework import serializers


class batchcreationSerializer(serializers.Serializer):

    uid = serializers.CharField(max_length=1000)
    batch_title = serializers.CharField(max_length=25)
    batch_description = serializers.CharField(max_length=500)


class updateBatchSerializer(serializers.Serializer):

    batch_description = serializers.CharField(max_length=500)
    uid = serializers.CharField(max_length=1000)
