from pyfiglet import Figlet


def compression_ratio(original_size, encoded_size):
    ratio = (1 - (encoded_size / original_size)) * 100
    return ratio

class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.code = ''

def shannon_fano_coding(nodes):
    if len(nodes) == 1:
        return
    total_probability = sum(node.probability for node in nodes)
    left_prob = 0
    for i, node in enumerate(nodes):
        if left_prob > total_probability / 2:
            break
        left_prob += node.probability
    partition = i
    for i, node in enumerate(nodes):
        if i < partition:
            node.code += '0'
        else:
            node.code += '1'
    shannon_fano_coding(nodes[:partition])
    shannon_fano_coding(nodes[partition:])

def main():
    # text = input("Введите текст для кодирования: ")
    texts = open('C:/sofa/ra/racinLab2/133.txt','r')
    text_file = texts.readlines()
    text = ''.join(text_file)



    symbols = list(set(text)) #короче сет делает множество из символов проше говоря данные будут содержать только уникальные хуементы а повторяющиеся нахуй адалены вот!
    print(symbols)
    
    probabilities = [text.count(symbol) / len(text) for symbol in symbols] #список вероятностей для каждой букв
    print(probabilities)
    print("\n\n\n") #да быдло код но я так вижу Понял?
    for proba in probabilities:
        print(f"{proba}")

    nodes = [Node(symbol, prob) for symbol, prob in zip(symbols, probabilities)]
    nodes.sort(key=lambda x: x.probability, reverse=True)
    shannon_fano_coding(nodes)
    print("Symbol  Probability  Code")
    for node in nodes:
        print(f"{node.symbol}\t{node.probability}\t{node.code}")
    print("\n\n\n")

    encoded_text = ""
    for char in text:
        for node in nodes:
            if char == node.symbol:
                encoded_text += node.code
                break
    # print(f"Закодированный текст: {encoded_text}")


    original_size = len(text) * 8  # Предполагаем, что каждый символ занимает 8 бит
    encoded_size = len(encoded_text)

    print(f"Исходный размер текста: {original_size} бит")
    print(f"Размер закодированного текста: {encoded_size} бит")
    print(f"Степень сжатия: {compression_ratio(original_size, encoded_size):.2f}%")


if __name__ == "__main__":
    f = Figlet(font="slant")
    print(f.renderText('KODIROVANIE DOMAShNEVA'))
    main()

    
