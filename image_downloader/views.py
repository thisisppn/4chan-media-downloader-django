from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from image_downloader.chan_class.thread import FourchanThread
def download_thread_images(request):
    if request.method == "GET":
        thread_url = request.GET.get('thread_url')
        four_thread = FourchanThread(thread_url)
        four_thread.download_images()
        return HttpResponse(thread_url)