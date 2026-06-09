from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q, F
from django.db import models
from django.contrib import messages
from partidas.models import Partida, Evento
from times.models import Time
from jogadores.models import Jogador
from campeonatos.models import Campeonato

def dashboard(request):
    # Totais gerais
    total_partidas = Partida.objects.filter(status='EN').count()
    total_gols = Evento.objects.filter(tipo='GOL').count()
    total_times = Time.objects.count()
    total_jogadores = Jogador.objects.count()

    # Partidas e status
    ultimas_partidas = Partida.objects.filter(status='EN').order_by('-data')[:5]
    ao_vivo = Partida.objects.filter(status='AO')
    partidas = Partida.objects.all().order_by('data')  # Lista todas para o painel principal

    # Artilheiros
    artilheiros = Jogador.objects.annotate(
        gols=Count('eventos', filter=Q(eventos__tipo='GOL'))
    ).filter(gols__gt=0).order_by('-gols')[:10]

    # Cartões
    cartoes_amarelos = Evento.objects.filter(tipo='CAR').count()
    cartoes_vermelhos = Evento.objects.filter(tipo='VER').count()

    # --- SISTEMA DE DESEMPENHO CRIADO POR CAUÃ ---
    # Este bloco varre os 16 times e calcula o retrospecto de cada um dinamicamente
    times = Time.objects.all()
    desempenho_times = []
    
    for t in times:
        # Conta vitórias (como mandante ou visitante)
        vitorias = Partida.objects.filter(status='EN').filter(
            (Q(time_casa=t) & Q(gols_casa__gt=F('gols_visitante'))) |
            (Q(time_visitante=t) & Q(gols_visitante__