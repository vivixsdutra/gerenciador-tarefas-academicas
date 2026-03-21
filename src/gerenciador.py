class GerenciadorTarefas:
    def _init_(self):
        # Armazena as tarefas
        self.tarefas = {}

        # Controla o próximo ID para a próxima tarefa
        self.proximo_id = 1

    def criar_tarefa(self, titulo, disciplina, descricao, prioridade, prazo):
        # Validações dos dados fornecidos
        if not titulo or titulo.strip() == "":
            raise ValueError("Título não pode ser vazio")

        if not disciplina or disciplina.strip() == "":
            raise ValueError("Disciplina não pode ser vazia")

        prioridades_validas = ["baixa", "media", "alta"]
        if prioridade not in prioridades_validas:
            raise ValueError("Prioridade inválida")

        # Criando a tarefa com os dados fornecidos
        tarefa = {
            "titulo": titulo,
            "disciplina": disciplina,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": "pendente",
            "prazo": prazo
        }

        # Salvar tarefa
        id_tarefa = self.proximo_id
        self.tarefas[id_tarefa] = tarefa

        # Atualizar contador
        self.proximo_id += 1

        return id_tarefa