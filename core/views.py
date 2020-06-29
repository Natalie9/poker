from django.http import JsonResponse
from rest_framework.decorators import api_view

from Modelos.teste import fazer_verficacao, compara_maos


@api_view(['POST'])
def IndexViewSet(request):
    import json

    response = json.loads(request.body)
    res1 = fazer_verficacao(list(response['mao1']))
    res2 = fazer_verficacao(list(response['mao2']))
    vencedora = compara_maos(res1, res2)
    print(vencedora)
    return JsonResponse(vencedora)
