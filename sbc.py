import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fzy

# Conjuntos Difusos

r_norm = np.linspace(-1,1,500)

corners_ng = np.array([-1.0,-1.0,-0.8,-0.6])
corners_nm = np.array([-0.8,-0.6,-0.4,-0.2])
corners_np = np.array([-0.5,-0.4,-0.2,-0.1])
corners_ni = np.array([-0.2,-0.1,0.0,0.0])
corners_ce = np.array([-0.1,0.0,0.1])
corners_pi = np.array([0.0,0.0,0.1,0.2])
corners_pp = np.array([0.1,0.2,0.4,0.5])
corners_pm = np.array([0.4,0.4,0.6,0.8])
corners_pg = np.array([0.6,0.8,1.0,1.0])

trap_ng = fzy.trapmf(r_norm, corners_ng)
trap_nm = fzy.trapmf(r_norm, corners_nm)
trap_np = fzy.trapmf(r_norm, corners_np)
trap_ni = fzy.trapmf(r_norm, corners_ni)
trap_ce = fzy.trimf(r_norm, corners_ce)
trap_pi = fzy.trapmf(r_norm, corners_pi)
trap_pp = fzy.trapmf(r_norm, corners_pp)
trap_pm = fzy.trapmf(r_norm, corners_pm)
trap_pg = fzy.trapmf(r_norm, corners_pg)


fuzzy_sets = [trap_ng, trap_nm, trap_np, trap_ni, trap_ce, trap_pi, trap_pp, trap_pm, trap_pg]

''' Visualizacion Conjuntos difusos
for z in fuzzy_sets:
    plt.plot(r_norm, z)
plt.show()
'''

corners_c1 = np.array([-1.0,-1.0,-0.8,-0.6])
corners_c2 = np.array([-0.8,-0.65,-0.35,-0.2])
corners_c3 = np.array([-0.3,-0.15,0.15,0.3])
corners_c4 = np.array([0.2,0.35,0.65,0.8])
corners_c5 = np.array([0.6,0.8,1.0,1.0])

trap_c1 = fzy.trapmf(r_norm, corners_c1)
trap_c2 = fzy.trapmf(r_norm, corners_c2)
trap_c3 = fzy.trapmf(r_norm, corners_c3)
trap_c4 = fzy.trapmf(r_norm, corners_c4)
trap_c5 = fzy.trapmf(r_norm, corners_c5)

categories = [trap_c1, trap_c2, trap_c3, trap_c4, trap_c5]

''' Visualizacion Categorias
for z in categories:
    plt.plot(r_norm, z)
plt.show()
'''

# Funcion de pertenencia: devuelve el valor de pertenencia de un valor 
def mu(val, fuzzy_set):
    val_idx = np.abs(r_norm - val).argmin()
    return fuzzy_set[val_idx]

# Implementacion funcion de_a
def de_a(corners_1,corners_2):
    sorted_fuzz = np.append(corners_1,corners_2)
    sorted_fuzz.sort()
    de_a = [sorted_fuzz[0],sorted_fuzz[1],sorted_fuzz[-2],sorted_fuzz[-1]]
    return fzy.trapmf(r_norm, de_a)

def de_a_corners(corners_1,corners_2):
    sorted_fuzz = np.append(corners_1,corners_2)
    sorted_fuzz.sort()
    de_a = [sorted_fuzz[0],sorted_fuzz[1],sorted_fuzz[-2],sorted_fuzz[-1]]
    return de_a


def rule_output(val, rule):
    E1, E2, E3 = val[0], val[1], val[2]
    TEMP, OX, P, S = rule[0], rule[1], rule[2], rule[3]
    thresh = min(mu(E1, TEMP), mu(E2, OX), mu(E3,P))
    binary_cut = fzy.lambda_cut(rule[3], thresh)
    output = np.array([S[i] if binary_cut[i] == 0 else thresh for i in range(len(S))])
    return output

def or_combination(sets):
    output_set = []
    for i in range(len(r_norm)):
        values = [s[i] for s in sets]
        output_set.append(max(values))
    return np.array(output_set)

def cog(s):
    if np.sum(s) == 0:
        return 0
    else:
        return np.sum(s*r_norm)/np.sum(s)


def inference_machine(E1, E2, E3, rules, defuzz_mode):
    out_sets = []
    activated_rules = []
    for i, rule in enumerate(rules):
        out = rule_output((E1,E2,E3), rule)
        if max(out) != 0: activated_rules.append(i+1)
        out_sets.append(out)
    combined_output = or_combination(out_sets.copy())
    defuzz = cog(combined_output)
    return defuzz, activated_rules



#### BASE DE CONOCIMIENTOS ####

rule_1 = [trap_ng, de_a(corners_ng,corners_nm), de_a(corners_ng,corners_nm), trap_c1]
rule_2 = [ de_a(corners_ng,corners_nm), trap_ng, de_a(corners_ng,corners_nm), trap_c1]
rule_3 = [ de_a(corners_ng,corners_nm), de_a(corners_ng,corners_nm), trap_ng, trap_c1]
rule_4 = [trap_pg, de_a(corners_pg,corners_pm), de_a(corners_pg,corners_pm), trap_c1]
rule_5 = [ de_a(corners_pg,corners_pm), trap_pg, de_a(corners_pg,corners_pm), trap_c1]
rule_6 = [ de_a(corners_pg,corners_pm), de_a(corners_pg,corners_pm), trap_pg, trap_c1]
rule_7 = [trap_nm, trap_nm, de_a(corners_ng, corners_nm), trap_c2]
rule_8 = [trap_nm, de_a(corners_ng, corners_nm), trap_nm,  trap_c2]
rule_9 = [de_a(corners_ng, corners_nm), trap_nm, trap_nm,  trap_c2]
rule_10 = [trap_pm, trap_pm, de_a(corners_pg, corners_pm), trap_c2]
rule_11 = [trap_pm, de_a(corners_pg, corners_pm), trap_pm,  trap_c2]
rule_12 = [de_a(corners_pg, corners_pm), trap_pm, trap_pm,  trap_c2]
rule_13 = [trap_nm, trap_nm, de_a(corners_nm, corners_np), trap_c3]
rule_14 = [trap_nm, de_a(corners_nm, corners_np), trap_nm,  trap_c3]
rule_15 = [de_a(corners_nm, corners_np), trap_nm, trap_nm,  trap_c3]
rule_16 = [trap_pm, trap_pm, de_a(corners_pm, corners_pp), trap_c3]
rule_17 = [trap_pm, de_a(corners_pm, corners_pp), trap_pm,  trap_c3]
rule_18 = [de_a(corners_pm, corners_pp), trap_pm, trap_pm,  trap_c3]
rule_19 = [trap_pp, de_a(corners_pp,corners_nm), de_a(corners_pp,corners_nm), trap_c4]
rule_20 = [ de_a(corners_pp,corners_nm), trap_pp, de_a(corners_pp,corners_nm), trap_c4]
rule_21 = [ de_a(corners_pp,corners_nm), de_a(corners_pp,corners_nm), trap_pp, trap_c4]
rule_22 = [trap_pp, de_a(corners_pp,corners_pm), de_a(corners_pp,corners_pm), trap_c4]
rule_23 = [ de_a(corners_pp,corners_pm), trap_pp, de_a(corners_pp,corners_pm), trap_c4]
rule_24 = [ de_a(corners_pp,corners_pm), de_a(corners_pp,corners_pm), trap_pp, trap_c4]
rule_25 = [trap_np, trap_np, de_a(corners_np, corners_nm), trap_c5]
rule_26 = [trap_np, de_a(corners_np, corners_nm), trap_np,  trap_c5]
rule_27 = [de_a(corners_np, corners_nm), trap_np, trap_np,  trap_c5]
rule_28 = [trap_pp, trap_pp, de_a(corners_pp, corners_pm), trap_c5]
rule_29 = [trap_pp, de_a(corners_pp, corners_pm), trap_pp,  trap_c5]
rule_30 = [de_a(corners_pp, corners_pm), trap_pp, trap_pp,  trap_c5]

rules = [rule_1, rule_2, rule_3, rule_4, rule_5, rule_6, rule_7, rule_8, rule_9, rule_10, rule_11, rule_12, rule_13, rule_14, rule_15, rule_16, rule_17, rule_18, rule_19, rule_20, rule_21, rule_22, rule_23, rule_24, rule_25, rule_26, rule_27, rule_28, rule_29, rule_30]

# Visalizacion Reglas
# fig, axs = plt.subplots(5, 4, figsize = (10,40)) #, sharex=True, sharey=True)
# for i, val in enumerate([0,7,14,21,28]):
#     axs[i,0].plot(r_norm, rules[val][0])
#     axs[i,0].set_title('E1')
#     axs[i,0].set_ylabel(f'Rule {i+1}', fontsize=18)

#     axs[i,1].plot(r_norm, rules[val][1])
#     axs[i,1].set_title('E2')

#     axs[i,2].plot(r_norm, rules[val][2])
#     axs[i,2].set_title(f'E3')

#     axs[i,3].plot(r_norm, rules[val][3])
#     axs[i,3].set_title(f'S')
# fig.tight_layout(pad=2.0)
# plt.show()
