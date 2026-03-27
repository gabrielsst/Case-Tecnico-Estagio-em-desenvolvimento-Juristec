class Televisao:
    def __init__(self, canais_validos, canal_inicial=1, volume=10, volume_max=100):
        if canal_inicial not in canais_validos:
            raise ValueError("Canal inicial inválido")

        self.canais_validos = sorted(canais_validos)
        self.canal = canal_inicial
        self.volume = volume
        self.volume_max = volume_max
        self.mudo = False
        self._volume_anterior = volume

    def mudar_canal(self, novo_canal):
        if novo_canal in self.canais_validos:
            self.canal = novo_canal
        else:
            print("Canal inválido")

    def aumentar_volume(self):
        if not self.mudo and self.volume < self.volume_max:
            self.volume += 1

    def diminuir_volume(self):
        if not self.mudo and self.volume > 0:
            self.volume -= 1

    def alternar_mudo(self):
        if not self.mudo:
            self._volume_anterior = self.volume
            self.volume = 0
            self.mudo = True
        else:
            self.volume = self._volume_anterior
            self.mudo = False

    def __str__(self):
        status_mudo = "Ligado" if self.mudo else "Desligado"
        return f"Canal: {self.canal} | Volume: {self.volume}/{self.volume_max} | Mudo: {status_mudo}"