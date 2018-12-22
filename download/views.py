# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from download.tasks import download_single_track_task
from celery.result import AsyncResult
from utils.downloaders.pyLoad import PyLoad

pyLoad = PyLoad('http://192.168.1.5', 8001, 'pyload', 'pyload')

@api_view(['POST'])
def download(request):
    name = request.data.get('name', None)
    tracks = request.data.get('tracks', None)
    if name and tracks:
        result = pyLoad.download(name, tracks)
        return Response(result)
    else:
        return Response({'message': 'Invalid input!'}, 400)

@api_view(['GET'])
def get_progress_for_task(request, pid):
    # result = AsyncResult(task_id)
    # print "%s %s %s" % (result.state, result.status, result.info)
    # data = {
    #     'state': result.state,
    #     'details': result.info,
    # }
    # return Response(data)
    return Response(pyLoad.get_download_status(int(pid)))
