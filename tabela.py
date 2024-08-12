def mostrar_tabela_pontuacao(tabela_pontuacao):
  """Mostra a tabela de pontuação após o jogo."""
  print("\nTabela de Pontuação:")
  print("---------------------------")
  print("Jogador | Pontos")
  print("---------------------------")
  for nome, pontos in tabela_pontuacao.items():
      print(f"{nome: <10} | {pontos: <6}")
  print("---------------------------")