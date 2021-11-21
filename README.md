# Optimal_Design_Active_Set_Approach

## Compliance optimization with obstacle constraints: an active set approach
This source code implements an active set algorithm to solve compliance optimization problems with obstacle constraints in support of the manuscript Compliance optimization with obstacle constraints: an active set approach.

## About

Author: Nha Van Tran
Department of Mathematics, Louisiana State University, Baton Rouge, LA 70803, USA. E-mail: vtran32@lsu.edu or tvnha.hcmus@gmail.com

Advisor: Blaise Bourdin
Department of Mathematics & Statistics, McMaster University, Hamilton, ON Canada. 
Formerly: Department of Mathematics, Louisiana State University, Baton Rouge, LA 70803, USA. E-mail: bourdin@mcmaster.ca

https://github.com/NhaVanTran/Optimal_Design_Active_Set_Approach

## How it works

The active set method (see AS_phase_field_opt.py) is implemented in FEniCS computing platform (https://fenicsproject.org/), version 2018.1.0, and then compared to a classical penalty algorithm (see DA_phase_field_opt.py) implemented in Dolfin-Adjoint (http://www.dolfin-adjoint.org/en/latest/about/index.html), version 2018.1. 

All the default parameters that are used for numerical examples can be found in the file user_parameters.py.

Take the compliance optimization problem with one obstacle as an example, and we use the command below to execute the active set algorithm in the file AS_phase_field_opt.py.

>>mpirun -np 8 python3 AS_phase_field_opt.py --solver_alpha.gradient_absolute_tol 5.e-8 --solver_alpha.gradient_relative_tol 5.e-8 --solver_alpha.gradient_t_tol 5.e-8 --problem.initial_guess.is_constant 0 --problem.initial_guess.sin_px 10 --problem.initial_guess.sin_py 10 --problem.const.delta 1.e-3 --mesh.structured_mesh 1 --mesh.cell_size 0.005 --material.ell 0.025 --problem.const.kappa 5.e-5 --ex 2 --problem.case 7100 --problem.const.eta 0.08 --problem.force.gy -1 --problem.obstacle.ub_u_y 1.e8 --problem.obstacle.lb_u_y -0.02 post_processing.TAO_saving_frequency 200|& tee -a ex27100_validation_delta_1e3_rerun.txt
./run_AS_phase_field_influence_initial_guess_examples_0921_FEniCS_2018_1.sh

Here, the algorithm stops when the gradient tolerance is about 5e-8. Some parameters, such as kappa, eta, and obstacles, can be adjusted to account for different scenarios described in the manuscript.

Then we execute the command below to solve the same problem using the penalty method, in DA_phase_field_opt.py, which is implemented in Dolfin-Adjoint 2018.1.

>>mpiexec -n 8 python3 DA_phase_field_opt.py --ex 2 --problem.case 7100 --gtol 5.e-8 --problem.initial_guess.is_constant 0 --problem.initial_guess.sin_px 10 --problem.initial_guess.sin_py 10 --problem.const.delta 1.e-3 --mesh.structured_mesh 1 --mesh.cell_size 0.005 --material.ell 0.025 --problem.obstacle.lb_u_y -0.02 --problem.obstacle.ub_u_y 1e8 --problem.const.eta 0.08 --problem.const.kappa 5.e-5 --problem.force.gy -1 post_processing.TAO_saving_frequency 200|& tee -a chao1_DA_ex27100_validating_delta_1e3.txt

For simplicity, within the FEniCS environment, the reader can run the command below to generate all the results of the examples mentioned in the manuscript. 
>>./run_AS_phase_field_0921_FEniCS_2018_1.sh

And run the command line
>>./run_DA_chaos1_phase_field_validating_examples.sh
to get the result of the examples for validations which are compared with the penalty method by running 

## Notes
The optimization is nonlinear and nonconvex, and the domain Omega is randomly partitioned to run in parallel. It is therefore expected that the active set may not converge sometimes or that more than one execution may be required.
