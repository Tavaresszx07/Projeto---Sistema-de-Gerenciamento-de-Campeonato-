from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Time

class TimeListView(ListView):
    model = Time
    template_name = 'times/lista.html'
    context_object_name = 'times'

    def get_queryset(self):
        # Se os times antigos estiverem incompletos ou vazios, limpamos e criamos com os dados cheios
        # Isso garante que a tela vai atualizar com as infos certas
        if Time.objects.count() < 8:
            Time.objects.all().delete()  # Limpa os registros incompletos

        if not Time.objects.exists():
            data_hoje = timezone.now()
            
            # Lista com todos os campos que suas migrations criaram (nome, estadio, tecnico)
            times_completos = [
                {"nome": "Flamengo", "estadio": "Maracanã", "tecnico": "Filipe Luís"},
                {"nome": "Palmeiras", "estadio": "Allianz Parque", "tecnico": "Abel Ferreira"},
                {"nome": "São Paulo", "estadio": "Morumbis", "tecnico": "Zubeldía"},
                {"nome": "Santos", "estadio": "Vila Belmiro", "tecnico": "Carille"},
                {"nome": "Cruzeiro", "estadio": "Mineirão", "tecnico": "Diniz"},
                {"nome": "Atlético Mineiro", "estadio": "Arena MRV", "tecnico": "Milito"},
                {"nome": "Grêmio", "estadio": "Arena do Grêmio", "tecnico": "Renato Gaúcho"},
                {"nome": "Internacional", "estadio": "Beira-Rio", "tecnico": "Roger Machado"}
            ]

            for dados in times_completos:
                novo = Time(
                    nome=dados["nome"],
                    data_fundacao=data_hoje,
                    estadio=dados["estadio"],
                    tecnico=dados["tecnico"]
                )
                novo.save()

        return Time.objects.all()

class TimeDetailView(DetailView):
    model = Time
    template_name = 'times/detalhe.html'
    context_object_name = 'time'