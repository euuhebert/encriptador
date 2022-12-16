import random


def create_public_key(num):

  def mdc(num1, num2):
    rest = 1
    while (num2 != 0):
      rest = num1 % num2
      num1 = num2
      num2 = rest
    return num1

  while True:
    e = random.randrange(2, num)
    if (mdc(num, e) == 1):
      return e


def create_private_key(totiente, e):
  d = 0
  while ((d * e) % totiente != 1):
    d += 1
  return d


def encrypt(texto, e, n):
  msg_cifrada = ""
  for caractere in texto:
    c = (ord(caractere)**e) % n
    msg_cifrada += chr(c)
  return msg_cifrada


def decipher(texto, n, d):
  msg_decifrada = ""
  for caractere in texto:
    c = (ord(caractere)**d % n)
    msg_decifrada += chr(c)
  return msg_decifrada

print(
  "Esse programa cifra e decifra mensagens através de um algoritmo RSA, com o objetivo de manter restrição de acesso a uma área contaminada ambientalmente que contenha riscos a saúde pública.\n"
)


sair = False

while sair == False:

  msg = input("\nDigite a mensagem (limite/128 caracteres): ")
  if len(msg) > 0 and len(msg) <= 128:
    p = 29
    q = 37
    n = p * q
    y = p - 1
    x = q - 1
    totiente = x * y
    e = create_public_key(totiente)

    print(f"\nChave Pública: ({e}, {n})")

    d = create_private_key(totiente, e)
    print(f"Chave Privada: ({d}, {n})")

    msg = encrypt(msg, e, n)
    print("\n\x1B[4mMensagem Cifrada\x1B[0m: " + msg)

    j = 1
    while j == 1:
     
      print("\n\x1B[3mPara decifrar a mensagem digite as chaves privadas!\x1B[0m")
      chave_d = input("\nDigite respectivamente a primeira chave privada: ")
      chave_n = input("\nDigite respectivamente a segunda chave privada: ")
     
      try:
        if chave_d.isdigit and chave_n.isdigit:
          chave_d = int(chave_d)
          chave_n = int(chave_n)
          if chave_d == d and chave_n == n:
            msg = decipher(msg, n, d)
            print("\n\x1B[4m\nMensagem Decifrada\x1B[0m: " + msg)
            i = 0
            j = 0

          else:
            print("\n\033[1;31mVerifique se todas as chaves privadas estão corretas e digite-as novamente!\033[0;0m")
            j = 1

      except:
        print("\n\033[1;31mA chave precisa ser numérica!\033[0;0m")

  else:
    print("\n\033[1;31mSua mensagem não pode estar vazia e nem exceder 128 caracteres!\033[0;0m")

  u = 1
  while u == 1:
    opcao = input(
      "\n\x1B[3mDigite 1 para continuar escrevendo ou qualquer número para encerrar a operação: \x1B[0m"
    )

    try:
      if opcao.isdigit:
        opcao = int(opcao)
        if opcao != 1:
          sair = True
          u = 0
        else:
          u = 0
          sair = False
         

    except:
      print("\n\033[1;31mPor favor, digite um número inteiro!\033[0;0m")
      u = 1
