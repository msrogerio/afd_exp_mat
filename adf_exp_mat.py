"""
    ``Autor``: Marlon Rogério

    ``AUTÔMATO DE PILA``

    ``Considerar``:
    t ∈ EA;
    se x,y ∈, então (x) ∈ EA, x+y  ∈ EA e x-y ∈ EA

    ``Alfabetos``:
        Σ = {t, (, ), +, -}; 
        Γ = {x} 

    t ∈ N 

    Autômato para reconhecer expressão matemática

    ``Estados``: {ap, fp}
    ``Regras`` (R): 
        ap <- ( | Γ λ/x     
        ap <- t | Γ λ/λ 
        fp <- ) | Γ x/λ
        fp <- + | Γ λ/λ
        fp <- - | Γ λ/λ

    δ {
        ap <- ( -> ap
        ap <- t -> fp
        fp <- ) -> fp
        fp <- + | - -> ap
    }

"""
E = ['ap', 'fp']
Γ = [] #λ
i = E[0] #ap
F = E[1] #fp
e_atual = i

expressao = input('Digite a expressão matemática: ')

for t in expressao:
    if e_atual==E[0] and t == '(':
        e_atual = E[0]
        # Γ -= λ
        Γ = ['x']
    if e_atual==E[0] and t.isdigit():
        e_atual = E[1]
        # Γ -= λ
        # Γ += λ

    if e_atual==E[1] and t == ')':
        e_atual = E[1]
        Γ.pop() # Γ -= x
        # Γ += λ

    if e_atual==E[1] and t == '+' or t == '-':
        e_atual = E[0]
        # Γ -= λ
        # Γ += λ
if e_atual == F and not Γ:
    print('Expressão aceita!')
else:
    print('Expressão não aceita!')