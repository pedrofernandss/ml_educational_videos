from manim import *

config.pixel_height = 1920  
config.pixel_width = 1080   
config.frame_height = 14.0  
config.frame_width = 7.875 

class SupervisedLearning(Scene):
    def construct(self):

        # Criar um retângulo azul
        square = Rectangle(width=1.25, height=1.25, color="#00ACE2", fill_opacity=0.5)
        self.play(Create(square))

        # Criar texto que será colocado dentro do retângulo
        ai_label = Text("IA", font_size=32, color=WHITE)
        ai_label.move_to(square.get_center())  # Centraliza o ai_label dentro do retângulo

        # Adicionar animação de entrada do ai_label
        self.play(Write(ai_label))
        self.wait(0.5)

        input_arrow = Arrow(start=LEFT * 2.5, end=square.get_left(), color=WHITE)  # Início à esquerda do retângulo
        input_label = Text("Entrada", font_size=24, color=WHITE).next_to(input_arrow, LEFT, buff=0.15)
        input_arrow.next_to(square, LEFT, buff=0.15)  # Ajustar a posição da seta de input

        # Criar seta de output (direita)
        output_arrow = Arrow(start=square.get_right(), end=RIGHT * 2.5, color=WHITE)
        output_label = Text("Saída", font_size=24, color=WHITE).next_to(output_arrow, RIGHT, buff=0.15)
        output_arrow.next_to(square, RIGHT, buff=0.15)  # Ajustar a posição da seta de output

        # Adicionar animações
        self.play(Create(input_arrow), Write(input_label))
        self.play(Create(output_arrow), Write(output_label))

        self.play(FadeOut(square, ai_label, input_arrow, input_label, output_arrow, output_label))
        self.wait(1)


        main_title = Text("Como as Máquinas Aprendem com Dados?", font_size=32, color="#00ACE2")

        # Posiciona a primeira linha
        main_title.scale(0.8)
        main_title.move_to(UP)
        self.play(Write(main_title))
        self.wait(1)
                
        learning_types = BulletedList(
            "Supervisionado", 
            "Não Supervisionado", 
            "Reforço", 
            "Semi-Supervisionado",
            font_size=30
        )

        learning_types.next_to(main_title, DOWN, buff=1)
        self.play(FadeIn(learning_types))
        self.wait(1)
        # Destaque na palavra "Supervisionado"
        self.play(learning_types[0].animate.scale(1.2).set_color(YELLOW))
        self.wait(2)

        self.play(FadeOut(main_title, learning_types))

        # Manter a cena por um tempo
        self.wait(2)

       # Tabela de dados
        data_table = MathTable(
            [["Tamanho (m^2)", "Quartos", "Localizacao", "Preco"],
             ["140", "3", "Asa Sul", "900.000"],
             ["50", "2", "Sobradinho", "300.000"],
             ["80", "3", "Cuzeiro", "450.000"],
             ["25", "1", "Asa Norte", "550.000"]],
            include_outer_lines=True
        )
        data_table.scale(0.5).shift(UP)
        self.play(Write(data_table))

        self.wait(2)


        # Destacando a coluna "Col2" alterando a cor de fundo das células
        for cell in data_table.get_columns()[-1]:
            cell.set_fill(YELLOW, opacity=0.8)

        self.wait(3)

        # Adicionando espaçamento entre a tabela e o retângulo
        self.play(data_table.animate.shift(UP * 1.5))  # Movendo a tabela para cima

        # Criando o modelo de IA (retângulo)
        model_box = Rectangle(width=1.25, height=1.25, color="#00ACE2", fill_opacity=1).shift(DOWN)
        model_label = Text("IA", font_size=24).move_to(model_box.get_center())

        # Mostrar o retângulo e o texto "IA"
        self.play(Create(model_box), Write(model_label))

        # Animação da tabela entrando na caixa de IA
        self.play(
            data_table.animate.move_to(model_box.get_center()).scale(0.1),  # Move e reduz o tamanho
            run_time=2  # Duração da animação
        )

        self.play(
            model_box.animate.scale(1.5),  # Aumenta o tamanho do modelo
            run_time=2  # Define o tempo da animação
        )


        # # Simulação de uma nova previsão
        # new_data = MathTable([["120", "4", "Bairro Residencial"]], include_outer_lines=True)
        # new_data.scale(0.6).next_to(model_box, DOWN, buff=1)
        # predicted_price = Text("R$ 700.000", font_size=24).next_to(new_data, RIGHT)

        # # Adiciona a nova previsão ao modelo
        # self.play(Write(new_data))
        # self.play(Create(predicted_price))
        # self.wait(2)

        # # Resumo e transição para o próximo conceito
        # summary_text = Text("O modelo aprendeu a prever preços de imóveis", font_size=24, color=YELLOW).to_edge(DOWN)
        # self.play(Write(summary_text))
        # self.wait(3)

        # # Limpar a tela para o próximo conceito
        # self.play(FadeOut(summary_text, title, data_table, model_box, model_label, training_arrow, new_data, predicted_price))