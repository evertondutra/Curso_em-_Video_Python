algo = input('Digite algo: ')
print(f'{algo} é só espaços? {algo.isspace()}')
print(f'{algo} é numérico? {algo.isnumeric()}')
print(f'{algo} é alfabético? {algo.isalpha()}')
print(f'{algo} é alfanumérico? {algo.isalnum()}')
print(f'{algo} esta em maiúscula? {algo.isupper()}')
print(F'{algo} esta em minúscula? {algo.islower()}')
print(f'{algo} esta capitalizado? {algo.istitle()}')