#Reconhecimento de Fala em Python

Este script Python utiliza a biblioteca SpeechRecognition para realizar o reconhecimento de fala. Ele captura a entrada de áudio do microfone, ajusta para o ruído ambiente e tenta transcrever a fala usando o serviço de reconhecimento de fala do Google para o idioma português do Brasil.

## Pré-requisitos
- Certifique-se de ter a biblioteca SpeechRecognition instalada. Você pode instalá-la usando:
  ```python
  pip install SpeechRecognition
  ```

## Uso
1. Descomente a linha `# print(sr.Microphone().list_microphone_names())` para ver os microfones disponíveis e seus índices.
2. Ajuste o parâmetro `rec.pause_threshold` de acordo com suas preferências.
3. Execute o script.
4. Comece a falar quando solicitado.

## Explicação do Código
```python
import speech_recognition as sr

# Inicializa o reconhecedor
rec = sr.Recognizer()

# Descomente a linha abaixo para listar os microfones disponíveis
# print(sr.Microphone().list_microphone_names())

# Captura áudio do microfone
with sr.Microphone() as microfone:
    # Ajusta para o ruído ambiente
    rec.adjust_for_ambient_noise(microfone)
    
    # Solicita ao usuário para começar a falar
    print("Pode começar a falar:")
    
    # Define o limite de pausa e escuta o áudio
    rec.pause_threshold = 1.6
    audio = rec.listen(microfone)
    
    # Tenta transcrever a fala usando a API do Google
    try:
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio.")
    except sr.RequestError as e:
        print(f"Erro na requisição para o serviço de reconhecimento de fala; {e}")
```

Sinta-se à vontade para personalizar o código conforme suas necessidades. Se encontrar algum problema, verifique o índice do microfone e certifique-se de ter uma conexão à internet estável para o serviço de reconhecimento de fala do Google.