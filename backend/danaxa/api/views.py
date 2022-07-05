from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.http import FileResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import time
from . import draw

#here is target class of main endpoint of this project
class SplineDrawer(generics.GenericAPIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        try:
            #in form-data sent to this api, pairs of xs and ys (these are keys) should be string like list: x0,x1,x2,x3...
            #and ys: y0,y1,y2,y3,... with no spaces
            received_xs = list(request.data['xs'].split(","))
            received_ys = list(request.data['ys'].split(","))
            xs = []
            ys = []
            for i in received_xs:
                xs.append(int(i))
            for i in received_ys:
                ys.append(int(i))

            #image sholud be sent with "file" key
            file = request.data['file']

            #making a unique file name with time of receiving the image
            FILE_NAME = f"{int(time.time())}{file}"

            #saving the received image to DIR: media/received/{FILE_NAME}
            default_storage.save(f"media/received/{FILE_NAME}", ContentFile(file.read()))


            default_storage.save(f"media/sent/{FILE_NAME}", ContentFile(file.read()))

            #calling the draw function
            draw.draw(xs, ys, f"media/received/{FILE_NAME}", f"media/sent/{FILE_NAME}")

            #returning the drawn image as response
            return FileResponse(open(f"media/sent/{FILE_NAME}", 'rb'))
        except KeyError:
            print("THERE IS A PROBLEM!!")
        return HttpResponseNotFound()



