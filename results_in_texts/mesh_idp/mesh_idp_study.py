import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import matplotlib.ticker as ticker
import numpy as np
################################################################################
# mesh independence, tol = 5e-8, AS_results_728, intial guess Sin 2...
################################################################################
h_sin2_unstruct = [0.006305, 0.006012, 0.005656, 0.005248, 0.005105, 0.004791, 0.004534, 0.004326]
obj_sin2_unstruct = [0.0207272716, 0.0207452449, 0.0206492072, 0.0206898833, 0.0206967696, 0.0206091320, 0.0206582665, 0.0205589481]


h_sin2_struct = [0.01, 0.009, 0.008, 0.007, 0.006, 0.005]
obj_sin2_struct = [0.0206462378, 0.0206219971, 0.0205891882, 0.0205678700, 0.0206141686 , 0.0204774893]
fig1 = plt.figure(1)
sin2_unstruct, = plt.plot(h_sin2_unstruct, obj_sin2_unstruct, color='black', linestyle='solid', linewidth = 2, marker='^', markerfacecolor='black', markersize=6)

sin2_struct, = plt.plot(h_sin2_struct, obj_sin2_struct, color='red', linestyle='dashed', linewidth = 2, marker='v', markerfacecolor='red', markersize=6)

plt.legend([sin2_unstruct, sin2_struct], ['Un-structured mesh', 'Structured mesh'], prop={'size': 7})
# naming the x axis
plt.xlabel('Mesh size $h$')
# naming the y axis
plt.ylabel('Objective values')
# giving a title to my graph
plt.title('Mesh convergence: Initial guess with n = 2')
plt.savefig('mesh_convergence_sin2.png')
plt.savefig('mesh_convergence_sin2.pdf')

################################################################################
# mesh independence, tol = 5e-8, AS_results_728, Initial guess Sin 5
################################################################################
h_sin5_unstruct = [0.006305, 0.006012, 0.005656, 0.005105, 0.004791, 0.004534]
obj_sin5_unstruct = [0.0207544648, 0.0207897967, 0.0207295073, 0.0206644171, 0.0207171220, 0.0206710260]

h_sin5_struct = [0.01, 0.009, 0.008, 0.007, 0.006, 0.005]
obj_sin5_struct = [0.0207813684, 0.0207272041, 0.0207012443, 0.0206522523, 0.0206177754, 0.0204917724]

fig2 = plt.figure(2)
sin5_unstruct, = plt.plot(h_sin5_unstruct, obj_sin5_unstruct, color='black', linestyle='solid', linewidth = 2, marker='^', markerfacecolor='black', markersize=6)

sin5_struct, = plt.plot(h_sin5_struct, obj_sin5_struct, color='red', linestyle='dashed', linewidth = 2, marker='v', markerfacecolor='red', markersize=6)

plt.legend([sin5_unstruct, sin5_struct], ['Un-structured mesh', 'Structured mesh'], prop={'size': 7})
# naming the x axis
plt.xlabel('Mesh size $h$')
# naming the y axis
plt.ylabel('Objective values')
# giving a title to my graph
plt.title('Mesh convergence: Initial guess with n = 5')
plt.savefig('mesh_convergence_sin5.png')
plt.savefig('mesh_convergence_sin5.pdf')


################################################################################
# mesh independence, tol = 5e-8, AS_results_728, Initial guess Sin 8
################################################################################
h_sin8_unstruct = [0.006305, 0.006012, 0.005656, 0.005248, 0.005105, 0.004791, 0.004534, 0.004326]
obj_sin8_unstruct = [ 0.0208209448, 0.0207129972, 0.0207270600, 0.0206713798, 0.0207070926, 0.0206866406, 0.0206798336, 0.0206613286]

h_sin8_struct = [0.01, 0.009, 0.008, 0.007, 0.006, 0.005]
obj_sin8_struct = [0.0207785683, 0.0206833805, 0.0205801592, 0.0206160805, 0.0205305313, 0.0204831945]

fig3 = plt.figure(3)
sin8_unstruct, = plt.plot(h_sin8_unstruct, obj_sin8_unstruct, color='black', linestyle='solid', linewidth = 2, marker='^', markerfacecolor='black', markersize=6)

sin8_struct, = plt.plot(h_sin8_struct, obj_sin8_struct, color='red', linestyle='dashed', linewidth = 2, marker='v', markerfacecolor='red', markersize=6)

plt.legend([sin8_unstruct, sin8_struct], ['Un-structured mesh', 'Structured mesh'], prop={'size': 7})
# naming the x axis
plt.xlabel('Mesh size $h$')
# naming the y axis
plt.ylabel('Objective values')
# giving a title to my graph
plt.title('Mesh convergence: Initial guess with n = 8')
plt.savefig('mesh_convergence_sin8.png')
plt.savefig('mesh_convergence_sin8.pdf')

################################################################################
# mesh independence, tol = 5e-8, AS_results_728, Initial guess Sin 10, attempt 1
################################################################################
h_sin10_att1_unstruct = [0.006305, 0.006012, 0.005656, 0.005248, 0.005105, 0.004791, 0.004534, 0.004326]
obj_sin10_att1_unstruct = [0.0208705570, 0.0209509680, 0.0206437843, 0.0206298853, 0.0206972522, 0.0206741676, 0.0206093105, 0.0206295608]

h_sin10_att1_struct = [0.01, 0.009, 0.008, 0.007, 0.006, 0.005]
obj_sin10_att1_struct = [0.0208628143, 0.0207991637, 0.0207851629, 0.0206433383,  0.0205090044, 0.0204797046]

fig4 = plt.figure(4)
sin10_at1_unstruct, = plt.plot(h_sin10_att1_unstruct, obj_sin10_att1_unstruct, color='black', linestyle='solid', linewidth = 2, marker='^', markerfacecolor='black', markersize=6)

sin10_at1_struct, = plt.plot(h_sin10_att1_struct, obj_sin10_att1_struct, color='red', linestyle='dashed', linewidth = 2, marker='v', markerfacecolor='red', markersize=6)

plt.legend([sin10_at1_unstruct, sin10_at1_struct], ['Un-structured mesh', 'Structured mesh'], prop={'size': 7})
# naming the x axis
plt.xlabel('Mesh size $h$')
# naming the y axis
plt.ylabel('Objective values')
# giving a title to my graph
plt.title('Mesh convergence: Initial guess with n = 10, Attempt 1')
plt.savefig('mesh_convergence_sin10_att1.png')
plt.savefig('mesh_convergence_sin10_att1.pdf')


################################################################################
# mesh independence, tol = 5e-8, AS_results_728, Initial guess Sin 10, attempt 2
################################################################################
h_sin10_att2_unstruct = [0.006305, 0.006012, 0.005656, 0.005248, 0.005105, 0.004791, 0.004534, 0.004326]
obj_sin10_att2_unstruct = [0.0208705460, 0.0209509680, 0.0206437646, 0.0206318508, 0.0206971963, 0.0206741681, 0.0206066239, 0.0206300754]

h_sin10_att2_struct = [0.01, 0.009, 0.008, 0.007, 0.006, 0.005]
obj_sin10_att2_struct = [0.0208624632, 0.0207990877, 0.0207851003, 0.0206462362, 0.0205135593, 0.0204800857]

fig5 = plt.figure(5)
sin10_at2_unstruct, = plt.plot(h_sin10_att2_unstruct, obj_sin10_att2_unstruct, color='black', linestyle='solid', linewidth = 2, marker='^', markerfacecolor='black', markersize=6)

sin10_at2_struct, = plt.plot(h_sin10_att2_struct, obj_sin10_att2_struct, color='red', linestyle='dashed', linewidth = 2, marker='v', markerfacecolor='red', markersize=6)

plt.legend([sin10_at2_unstruct, sin10_at2_struct], ['Un-structured mesh', 'Structured mesh'], prop={'size': 7})
# naming the x axis
plt.xlabel('Mesh size $h$')
# naming the y axis
plt.ylabel('Objective values')
# giving a title to my graph
plt.title('Mesh convergence: Initial guess with n = 10, Attempt 2')
plt.savefig('mesh_convergence_sin10_att2.png')
plt.savefig('mesh_convergence_sin10_att2.pdf')


###############################################################
# mesh independence, tol = 5e-8, all initial guesses
###############################################################


fig6 = plt.figure(6)
sin2_unstruct, = plt.plot(h_sin2_unstruct, obj_sin2_unstruct, color='black', linestyle='solid', linewidth = 2, marker='^', markerfacecolor='red', markersize=6)
sin2_struct, = plt.plot(h_sin2_struct, obj_sin2_struct, color='black', linestyle='solid', linewidth = 2, marker='v', markerfacecolor='red', markersize=6)

sin8_unstruct, = plt.plot(h_sin8_unstruct, obj_sin8_unstruct, color='green', linestyle='dashed', linewidth = 2, marker='P', markerfacecolor='yellow', markersize=6)
sin8_struct, = plt.plot(h_sin8_struct, obj_sin8_struct, color='green', linestyle='dashed', linewidth = 2, marker='*', markerfacecolor='yellow', markersize=6)

sin10_at1_unstruct, = plt.plot(h_sin10_att1_unstruct, obj_sin10_att1_unstruct, color='violet', linestyle='-.', linewidth = 2, marker='h', markerfacecolor='blue', markersize=6)
sin10_at1_struct, = plt.plot(h_sin10_att1_struct, obj_sin10_att1_struct, color='violet', linestyle='-.', linewidth = 2, marker='H', markerfacecolor='blue', markersize=6)


plt.legend([sin2_unstruct, sin2_struct, sin8_unstruct, sin8_struct, sin10_at1_unstruct, sin10_at1_struct], ['Un-structured mesh, n = 2', 'Structured mesh, n = 2', 'Un-structured mesh, n = 8', 'Structured mesh, n = 8', 'Un-structured mesh, n = 10', 'Structured mesh, n = 10',], prop={'size': 7})

# naming the x axis
plt.xlabel('Mesh size $h$')
# naming the y axis
plt.ylabel('Objective values')

# giving a title to my graph
plt.title('Mesh convergence study')
plt.savefig('mesh_convergence_all_initial_guess.png')
plt.savefig('mesh_convergence_all_initial_guess.pdf')


###############################################################
# mesh independence, tol = 5e-8, Attempt 1 vs Attempt 2
###############################################################
h_sin10_att1_unstruct = [0.006305, 0.006012, 0.005656, 0.005248, 0.005105, 0.004791, 0.004534, 0.004326]
obj_sin10_att1_unstruct = [0.0208705570, 0.0209509680, 0.0206437843, 0.0206298853, 0.0206972522, 0.0206741676, 0.0206093105, 0.0206295608]

h_sin10_att1_struct = [0.01, 0.009, 0.008, 0.007, 0.006, 0.005]
obj_sin10_att1_struct = [0.0208628143, 0.0207991637, 0.0207851629, 0.0206433383,  0.0205090044, 0.0204797046]

h_sin10_att2_unstruct = [0.006305, 0.006012, 0.005656, 0.005248, 0.005105, 0.004791, 0.004534, 0.004326]
obj_sin10_att2_unstruct = [0.0208705460, 0.0209509680, 0.0206437646, 0.0206318508, 0.0206971963, 0.0206741681, 0.0206066239, 0.0206300754]

h_sin10_att2_struct = [0.01, 0.009, 0.008, 0.007, 0.006, 0.005]
obj_sin10_att2_struct = [0.0208624632, 0.0207990877, 0.0207851003, 0.0206462362, 0.0205135593, 0.0204800857]


fig7 = plt.figure(7)
obj_struct_att1, = plt.plot(h_sin10_att1_struct, obj_sin10_att1_struct, color='black', linestyle='solid', linewidth = 2, marker='^', markerfacecolor='black', markersize=6)
obj_unstruc_att1, = plt.plot(h_sin10_att1_unstruct, obj_sin10_att1_unstruct, color='black', linestyle='dashed', linewidth = 2, marker='^', markerfacecolor='red', markersize=6)

obj_struct_att2, = plt.plot(h_sin10_att2_struct, obj_sin10_att2_struct, color='blue', linestyle='solid', linewidth = 2, marker='*', markerfacecolor='blue', markersize=6)
obj_unstruc_att2, = plt.plot(h_sin10_att2_unstruct, obj_sin10_att2_unstruct, color='blue', linestyle='dashed', linewidth = 2, marker='*', markerfacecolor='red', markersize=6)

plt.legend([obj_struct_att1, obj_unstruc_att1, obj_struct_att2, obj_unstruc_att2], ['Structured mesh, Attempt 1', 'Un-structured mesh, Attempt 1', 'Structured mesh,  Attempt 2', 'Un-structured mesh,  Attempt 2'], prop={'size': 7})

# naming the x axis
plt.xlabel('Mesh size $h$')
# naming the y axis
plt.ylabel('Objective values')

# giving a title to my graph
plt.title('Mesh convergence: One  Attempt 1 vs  Attempt 2')
plt.savefig('mesh_convergence_sin10_att1_vs_att2.png')
plt.savefig('mesh_convergence_sin10_att1_vs_att2.pdf')

################################################################################
###The difference between two attempts
################################################################################
obj_sin10_att1_unstruct_diff = [0.0208705570, 0.0209509680, 0.0206437843, 0.0206298853, 0.0206972522, 0.0206741676, 0.0206093105, 0.0206295608]
obj_sin10_att1_struct_diff = [0.0208628143, 0.0207991637, 0.0207851629, 0.0206433383,  0.0205090044, 0.0204797046]
obj_sin10_att2_unstruct_diff = [0.0208705460, 0.0209509680, 0.0206437646, 0.0206318508, 0.0206971963, 0.0206741681, 0.0206066239, 0.0206300754]
obj_sin10_att2_struct_diff = [0.0208624632, 0.0207990877, 0.0207851003, 0.0206462362, 0.0205135593, 0.0204800857]


obj_sin10_att1_unstruct_diff_array = np.array(obj_sin10_att1_unstruct_diff)
obj_sin10_att2_unstruct_diff_array = np.array(obj_sin10_att2_unstruct_diff)
obj_sin10_att1_struct_diff_array = np.array(obj_sin10_att1_struct_diff)
obj_sin10_att2_struct_diff_array = np.array(obj_sin10_att2_struct_diff)


difference_unstructured_mesh = np.subtract(obj_sin10_att1_unstruct_diff_array, obj_sin10_att2_unstruct_diff_array)
difference_structured_mesh = np.subtract(obj_sin10_att1_struct_diff_array, obj_sin10_att2_struct_diff_array)

print("difference of unstructured mesh results is", difference_unstructured_mesh)
print("difference of structured mesh results is", difference_structured_mesh)

np.savetxt('difference_att1_vs_att2_unstruct.txt', difference_unstructured_mesh)
np.savetxt('difference_att1_vs_att2_truct.txt', difference_structured_mesh)

h_sin10_att2_unstruct = [0.006305, 0.006012, 0.005656, 0.005248, 0.005105, 0.004791, 0.004534, 0.004326]
h_sin10_att2_struct = [0.01, 0.009, 0.008, 0.007, 0.006, 0.005]


fig8 = plt.figure(8)
unstruct_diff, = plt.plot(h_sin10_att2_unstruct, difference_unstructured_mesh, color='black', linestyle='solid', linewidth = 2, marker='^', markerfacecolor='black', markersize=6)

struct_diff, = plt.plot(h_sin10_att2_struct, difference_structured_mesh, color='red', linestyle='dashed', linewidth = 2, marker='v', markerfacecolor='red', markersize=6)

plt.legend([unstruct_diff, struct_diff], ['Un-structured mesh', 'Structured mesh'], prop={'size': 7})
# naming the x axis
plt.xlabel('Mesh size $h$')
# naming the y axis
plt.ylabel('Values')
# giving a title to my graph
plt.title('The difference between two attempts')
plt.savefig('mesh_convergence_diff_att1_vs_att2.png')
plt.savefig('mesh_convergence_diff_att1_vs_att2.pdf')
