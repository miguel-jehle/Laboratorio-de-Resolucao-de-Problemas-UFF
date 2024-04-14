n1, n2, n3, n4 = map(float,input().split())
media = ((2*n1) + (3*n2) + (4*n3) + n4)/10
if media >= 7:
    print(f"Media: {media:.1f}")
    print('Aluno aprovado.')
elif 5 <= media <= 6.9:
    print(f"Media: {media:.1f}")
    print('Aluno em exame.')
    n5 = float(input())
    print(f"Nota do exame: {n5:.1f}")
    media_final = (n5 + media)/2
    if media_final >= 5:
        print('Aluno aprovado.')
        print(f"Media final: {media_final:.1f}")
    else:
        print('Aluno reprovado.')
        print(f"Media final: {media_final:.1f}")  
elif media < 5:
    print(f"Media: {media:.1f}")
    print('Aluno reprovado.')