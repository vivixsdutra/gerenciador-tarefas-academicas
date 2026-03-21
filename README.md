# Gerenciador de Tarefas Acadêmicas

Projeto em Python desenvolvido para a disciplina de Engenharia de Software.

## Objetivo
Criar um sistema para gerenciamento de tarefas acadêmicas, com suporte a cadastro, edição, remoção, conclusão e filtros de tarefas.

## Estrutura inicial
- `src/`: lógica do sistema
- `tests/`: testes automatizados
- `main.py`: ponto de entrada da aplicação

## Tecnologias
- Python
- Pytest
- GitHub Actions

## Modelo de Dados
Cada tarefa será representada por um dicionário com os seguintes campos:

- id: identificador único
- titulo: nome da tarefa
- disciplina: matéria relacionada
- descricao: detalhes da tarefa
- prioridade: baixa, media ou alta
- status: pendente, em andamento ou concluida
- prazo: data limite da tarefa

## Funcionalidades
- Criar tarefa
- Listar tarefas
- Buscar tarefa por ID
- Editar tarefa
- Remover tarefa
- Concluir tarefa
- Filtrar por disciplina
- Filtrar por prioridade
- Filtrar por status

## Regras de Negócio
- O título não pode ser vazio
- A disciplina não pode ser vazia
- A prioridade deve ser: baixa, media ou alta
- O status deve ser: pendente, em andamento ou concluida
- Não é permitido editar tarefas inexistentes
- Não é permitido remover tarefas inexistentes
- Não é permitido concluir tarefas já concluídas
- O prazo deve estar em um formato válido

## Estrutura do Sistema
O sistema será baseado em um dicionário onde:

- A chave será o ID da tarefa
- O valor será um dicionário com os dados da tarefa

Exemplo:

{
  1: { "titulo": "Estudar", ... },
  2: { "titulo": "Trabalho", ... }
}

## Funções Planejadas
- criar_tarefa()
- listar_tarefas()
- buscar_tarefa(id)
- editar_tarefa(id, dados)
- remover_tarefa(id)
- concluir_tarefa(id)
- filtrar_por_status(status)
- filtrar_por_prioridade(prioridade)
