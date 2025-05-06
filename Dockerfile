
FROM public.ecr.aws/lambda/python:3.12
WORKDIR /var/task  # Define o diretório correto


COPY lambda_function.py /var/task/

# Copia o diretório da aplicação para a Lambda
COPY app/automation /var/task/app/automation

# Copia os requisitos e instala as dependências
COPY requirements.txt /var/task/


# Define variáveis de ambiente para garantir o caminho correto do Python
ENV PYTHONPATH="/var/task:/opt/python:/usr/local/lib/python3.12:/root/.local/bin"

# Comando de entrada para a Lambda
CMD ["lambda_function.lambda_handler"]