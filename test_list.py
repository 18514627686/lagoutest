def output_letter(letter):

    l = []

    for item in letter:

        l.append(item)

    return l

if __name__ == "__main__":

    print(output_letter('kevin'))

#此方法的输出为：

#['k', 'e', 'v', 'i', 'n]

def output_letter(letter):

   return [l for l in letter if 'k' in l]

if __name__ == "__main__":

    print(output_letter(['kevin', 'did', 'automation', 'well']))
