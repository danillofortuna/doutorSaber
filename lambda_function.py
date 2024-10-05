import logging
import ask_sdk_core.utils as ask_utils
import urllib.request
import json

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Substitua pela sua chave da API da OpenAI
OPENAI_API_KEY = "change_me"

class PerguntaIntentHandler(AbstractRequestHandler):
    """Handler para a intenção PerguntaIntent."""
    
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("PerguntaIntent")(handler_input)

    def handle(self, handler_input):
        # Captura a pergunta do slot da Alexa
        slots = handler_input.request_envelope.request.intent.slots
        user_question = slots['Question'].value

        # Faz a chamada para a API do GPT e obtém a resposta
        gpt_response = get_gpt_response(user_question)
        
        # Constrói a resposta para a Alexa
        speak_output = gpt_response

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(True)  # Define se a sessão deve encerrar
                .response
        )

def get_gpt_response(user_question):
    """Faz a requisição à API da OpenAI e retorna a resposta."""
    
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "Você é o Doutor Saber, e se alguém perguntar seu nome, diga que é Doutor Saber. Não faça nenhuma pergunta após finalizar sua resposta."},
            {"role": "user", "content": user_question}
            ],
        "max_tokens": 400  # Define o número máximo de tokens para a resposta
    }
    
    # Faz a requisição à API
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['choices'][0]['message']['content']
    except Exception as e:
        logger.error(f"Erro ao acessar a API do GPT: {e}")
        return "Desculpe, não tive energia suficiente para chamar o doutor saber. Mas a fada azul mandou um beijo."

# Outros handlers, como o LaunchRequestHandler, para gerenciar a execução da skill
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler para o evento de abertura da skill."""
    
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speak_output = "Olá, eu sou o doutor saber. O que você quer saber hoje?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Handler para parar a skill."""
    
    def can_handle(self, handler_input):
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speak_output = ""

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(True)  # Encerra a sessão imediatamente
                .response
        )

# Configuração do SkillBuilder
sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(PerguntaIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())

lambda_handler = sb.lambda_handler()
