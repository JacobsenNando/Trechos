## Importa da biblioteca 
from winotify import Notification, audio

## Função
notificacao = Notification (app_id="APP da notificação", title="Titulo da notifição",
                            msg="Msg da notificação",
                            duration="short", icon=r"C:\Users\Suporte 6\Desktop\Hiimarte_logo")

## ADiciona som a noptificação
notificacao.set_audio(audio.LoopingAlarm, loop=False)

## Adiciona até 5 botões a notificação, que possuem link com algum lugar
notificacao.add_actions(label="escrito no botão", launch="link web ou direcionamento do botão")

## Mostra notificação
notificacao.show()
                                  
                                         
##  https://www.youtube.com/watch?v=dCp59j7e6to