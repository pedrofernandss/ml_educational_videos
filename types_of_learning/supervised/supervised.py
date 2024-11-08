from manim import *

config.pixel_height = 1920  
config.pixel_width = 1080   
config.frame_height = 14.0  
config.frame_width = 7.875 

class SupervisedLearning(Scene):
    def construct(self):

        main_title = Text("Como as máquinas aprendem com dados?", font_size=32, color="#00ACE2")

        # Posiciona a primeira linha
        main_title.scale(0.8)
        main_title.move_to(UP)
        self.play(Write(main_title))
        self.wait(1)
                
        learning_types = BulletedList(
            "Aprendizado Supervisionado", 
            "Aprendizado Não Supervisionado", 
            font_size=30
        )

        learning_types.next_to(main_title, DOWN, buff=1)
        self.play(FadeIn(learning_types))
        self.wait(2)
        # Destaque na palavra "Aprendizado Supervisionado"
        self.play(learning_types[0].animate.scale(1.2).set_color(YELLOW))
        self.wait(2)

        self.play(FadeOut(main_title, learning_types))

        # Manter a cena por um tempo
        self.wait(2)

        # Criar um retângulo azul
        square = Rectangle(width=1.25, height=1.25, color="#00ACE2", fill_opacity=0.5)
        self.play(Create(square))

        # Criar texto que será colocado dentro do retângulo
        ai_label = Text("IA", font_size=32, color=WHITE)
        ai_label.move_to(square.get_center())  # Centraliza o ai_label dentro do retângulo

        # Adicionar animação de entrada do ai_label
        self.play(Write(ai_label))
        self.wait(2)

        input_arrow = Arrow(start=LEFT * 2.5, end=square.get_left(), color=WHITE)  # Início à esquerda do retângulo
        input_label = Text("Entrada", font_size=24, color=WHITE).next_to(input_arrow, LEFT, buff=0.15)
        input_arrow.next_to(square, LEFT, buff=0.15)  # Ajustar a posição da seta de input

        # Criar seta de output (direita)
        output_arrow = Arrow(start=square.get_right(), end=RIGHT * 2.5, color=WHITE)
        output_label = Text("Saída", font_size=24, color=WHITE).next_to(output_arrow, RIGHT, buff=0.15)
        output_arrow.next_to(square, RIGHT, buff=0.15)  # Ajustar a posição da seta de output

        # Adicionar animações
        self.play(Create(input_arrow), Write(input_label))
        self.wait(2)
        self.play(Create(output_arrow), Write(output_label))
        self.wait(2)

        self.play(FadeOut(square, ai_label, input_arrow, input_label, output_arrow, output_label))
        self.wait(3)

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

        self.wait(1)


        # Destacando a coluna "Col2" alterando a cor de fundo das células
        for cell in data_table.get_columns()[-1]:
            cell.set_fill(YELLOW, opacity=0.8)

        self.wait(1)

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
            run_time=1  # Duração da animação
        )

        self.play(
            model_box.animate.scale(1.5),  # Aumenta o tamanho do modelo
            run_time=1  # Define o tempo da animação
        )


        # Simulação de uma nova previsão
        new_data = MathTable([
            ["Tamanho (m^2)", "Quartos", "Localizacao"],
            ["100", "3", "Asa Sul"]], include_outer_lines=True)
        new_data.scale(0.8).next_to(model_box, UP, buff=2.5)
        self.wait(2)

        self.play(
            new_data.animate.move_to(model_box.get_center()).scale(0.0001),  # Move e reduz o tamanho
            run_time=2  # Duração da animação
        )

        predicted_price = MathTable([["756.400"]], color=YELLOW).move_to(model_box.get_center())

        predicted_price.set_z_index(-1) # Define o valor atrás do model_box
        
        # Ajusta para sair do modelo
        self.play(Write(predicted_price))
        self.play(predicted_price.animate.shift(DOWN * 3), run_time=2, color=YELLOW)  # Move para baixo para dar a ideia de que está "saindo" do modelo
        self.wait(1.5)

        self.play(FadeOut(model_box, model_label, data_table, new_data, predicted_price))

        image = ImageMobject("types_of_learning/supervised/assets/images/cis_logo.png")

        # Defina a posição da imagem (opcional)
        image.move_to(ORIGIN)  # Centraliza a imagem na tela

        # Adicione a imagem à cena
        self.play(FadeIn(image))

        # Exiba a cena por 3 segundos
        self.wait(3)