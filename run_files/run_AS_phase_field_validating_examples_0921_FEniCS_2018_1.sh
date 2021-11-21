#!/bin/bash
####################################################################
### delta=1e-3
####################################################################
###################################################################
## Validating examples (active-set method vs penalty method)
###################################################################
##Ex1
mpirun -np 8 python3 AS_phase_field_opt.py --solver_alpha.gradient_absolute_tol 5.e-8 --solver_alpha.gradient_relative_tol 5.e-8 --solver_alpha.gradient_t_tol 5.e-8 --problem.initial_guess.is_constant 1 --problem.const.delta 1.e-3 --mesh.structured_mesh 1 --mesh.cell_size 0.005 --material.ell 0.025 --problem.const.kappa 5.e-5 --ex 1 --problem.case 7000 --problem.const.eta 0.08 --problem.force.gy -1 --problem.obstacle.ub_u_y 1.e8 --problem.obstacle.lb_u_y -1e8 post_processing.TAO_saving_frequency 200|& tee -a ex17000_validation_delta_1e3.txt

#mpirun -np 8 python3 AS_phase_field_opt.py --solver_alpha.gradient_absolute_tol 5.e-8 --solver_alpha.gradient_relative_tol 5.e-8 --solver_alpha.gradient_t_tol 5.e-8 --problem.initial_guess.is_constant 0 --problem.initial_guess.sin_px 10 --problem.initial_guess.sin_py 10 --problem.const.delta 1.e-3 --mesh.structured_mesh 1 --mesh.cell_size 0.005 --material.ell 0.025 --problem.const.kappa 5.e-5 --ex 1 --problem.case 7001 --problem.const.eta 0.08 --problem.force.gy -1 --problem.obstacle.ub_u_y 1.e8 --problem.obstacle.lb_u_y -1e8 post_processing.TAO_saving_frequency 200|& tee -a ex17001_validation_delta_1e3.txt
##Ex2 One active lower bound
mpirun -np 8 python3 AS_phase_field_opt.py --solver_alpha.gradient_absolute_tol 5.e-8 --solver_alpha.gradient_relative_tol 5.e-8 --solver_alpha.gradient_t_tol 5.e-8 --problem.initial_guess.is_constant 0 --problem.initial_guess.sin_px 10 --problem.initial_guess.sin_py 10 --problem.const.delta 1.e-3 --mesh.structured_mesh 1 --mesh.cell_size 0.005 --material.ell 0.025 --problem.const.kappa 5.e-5 --ex 2 --problem.case 7100 --problem.const.eta 0.08 --problem.force.gy -1 --problem.obstacle.ub_u_y 1.e8 --problem.obstacle.lb_u_y -0.02 post_processing.TAO_saving_frequency 200|& tee -a ex27100_validation_delta_1e3_rerun.txt


# ex 2.2 non active upper and lower bounds
mpirun -np 8 python3 AS_phase_field_opt.py --solver_alpha.gradient_absolute_tol 5.e-8 --solver_alpha.gradient_relative_tol 5.e-8 --solver_alpha.gradient_t_tol 5.e-8 --problem.initial_guess.is_constant 0 --problem.initial_guess.sin_px 10 --problem.initial_guess.sin_py 10 --problem.const.delta 1.e-3 --mesh.structured_mesh 1 --mesh.cell_size 0.005 --material.ell 0.025 --problem.const.kappa 5.e-5 --ex 2 --problem.case 7110 --problem.const.eta 0.3 --problem.force.gy -1 --problem.obstacle.ub_u_y 1.e8 --problem.obstacle.lb_u_y -1.e8 post_processing.TAO_saving_frequency 200|& tee -a ex27110_validation_delta_1e3_rerun.txt

##Ex 3
mpirun -np 8 python3 AS_phase_field_opt.py --solver_alpha.gradient_absolute_tol 5.e-8 --solver_alpha.gradient_relative_tol 5.e-8 --solver_alpha.gradient_t_tol 5.e-8 --problem.initial_guess.is_constant 0 --problem.initial_guess.sin_px 2 --problem.initial_guess.sin_py 2 --ex 3 --problem.case 7200 --problem.const.delta 1.e-3 --problem.const.eta 0.3 --problem.force.gy -10. --problem.obstacle.ub_u_y 0.25 --problem.obstacle.lb_u_y -0.035 --problem.const.kappa 5.e-5 --mesh.structured_mesh 1 --mesh.cell_size 0.005 --material.ell 0.025 --post_processing.TAO_saving_frequency 200|& tee -a ex3_7200_validation_delta_1e3_rerun.txt

mpirun -np 8 python3 AS_phase_field_opt.py --solver_alpha.gradient_absolute_tol 5.e-8 --solver_alpha.gradient_relative_tol 5.e-8 --solver_alpha.gradient_t_tol 5.e-8 --problem.initial_guess.is_constant 0 --problem.initial_guess.sin_px 2 --problem.initial_guess.sin_py 2 --ex 3 --problem.case 7201 --problem.const.delta 1.e-3 --problem.const.eta 0.35 --problem.force.gy -10. --problem.obstacle.ub_u_y 0.25 --problem.obstacle.lb_u_y -0.035 --problem.const.kappa 5.e-5 --mesh.structured_mesh 1 --mesh.cell_size 0.005 --material.ell 0.025 --post_processing.TAO_saving_frequency 200|& tee -a ex3_7201_eta_variation_delta_1e3_rerun.txt
