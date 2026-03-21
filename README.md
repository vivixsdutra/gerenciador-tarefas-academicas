## Observação

Projeto em desenvolvimento.

# Gerenciador de Tarefas Acadêmicas

Projeto em Python desenvolvido para a disciplina de Engenharia de Software.

## Objetivo
Criar um sistema para gerenciamento de tarefas acadêmicas, com suporte a cadastro, edição, remoção, conclusão e filtros de tarefas.

## Arquitetura do Sistema

O sistema segue uma abordagem orientada a objetos, utilizando a classe `GerenciadorTarefas` para centralizar a lógica da aplicação.

As tarefas são armazenadas em um dicionário, onde:
- a chave representa o ID da tarefa
- o valor representa os dados da tarefa

Essa estrutura permite acesso rápido, organização dos dados e facilita a implementação de testes automatizados.

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

### ✔️ Implementadas
- Criar tarefa (com validações)
- Geração automática de ID

### 🔜 Planejadas
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


## Testes Automatizados

O projeto utilizará testes unitários com `pytest`.

Serão criados testes para:
- fluxos válidos
- entradas inválidas
- regras de negócio

## CI/CD

Será implementado um pipeline utilizando GitHub Actions para:
- executar testes automaticamente
- validar o funcionamento do sistema
