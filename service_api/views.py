from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from service_api.encryption import Vigenere
from service_api.encryption import ProtokolBB84

from rest_framework.decorators import parser_classes
from service_api.textParser import PlainTextParser

from service_api.models import Pengukuran
from service_api.models import Konfigurasi


import json

from datetime import datetime


vigenere = Vigenere()
protokol_bb84 = ProtokolBB84()

@api_view(['POST'])
@parser_classes([PlainTextParser])
def baca_sensor(request):

    # Data dari request masih berupa plain text
    body_request = request.data 

    # Dilakukan quantum encryption menggunakan protokol BB84
    classical_cipher = protokol_bb84.enkripsi(body_request)


    # Dekripsi dari classical encryption method (Vigenere)
    kunci = "wota konservatif"

    plain_text = vigenere.dekripsi(kunci, classical_cipher)

    # Dimasukkan kedalam database lewat model dulu
    data = json.loads(body_request)


    pengukuran = Pengukuran(
        suhu_air = data['suhu_air'],
        ph = data['ph'],
        total_solid_dissolve = data['total_solid_dissolve']
    )

    pengukuran.save()


    return Response()

