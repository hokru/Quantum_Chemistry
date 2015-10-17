import numpy as np
import scipy.special as sp


class TwoElectronInteractionIntegral:

    def __init__(self, basis_set_array):
        self.basis_set_array = basis_set_array

    def calculate(self, i, j, k, l):
        basis_coefficients_i = self.basis_set_array[i].get_array_of_coefficients()
        basis_coefficients_j = self.basis_set_array[j].get_array_of_coefficients()
        basis_coefficients_k = self.basis_set_array[k].get_array_of_coefficients()
        basis_coefficients_l = self.basis_set_array[l].get_array_of_coefficients()
        f_mn = 0
        for a in range(0, len(basis_coefficients_i)):
            for b in range(0, len(basis_coefficients_j)):
                for c in range(0, len(basis_coefficients_k)):
                    for d in range(0, len(basis_coefficients_l)):

                        a_1 = basis_coefficients_i[a][1]
                        a_2 = basis_coefficients_j[b][1]
                        a_3 = basis_coefficients_k[c][1]
                        a_4 = basis_coefficients_l[d][1]

                        c_1 = basis_coefficients_i[a][0]
                        c_2 = basis_coefficients_j[b][0]
                        c_3 = basis_coefficients_k[c][0]
                        c_4 = basis_coefficients_l[d][0]

                        n_1 = ((2 * a_1) / np.pi)**(3/4)
                        n_2 = ((2 * a_2) / np.pi)**(3/4)
                        n_3 = ((2 * a_3) / np.pi)**(3/4)
                        n_4 = ((2 * a_4) / np.pi)**(3/4)

                        r_a = self.basis_set_array[i].get_coordinates()
                        r_b = self.basis_set_array[j].get_coordinates()
                        r_c = self.basis_set_array[k].get_coordinates()
                        r_d = self.basis_set_array[l].get_coordinates()
                        r_p = (a_1 * r_a + a_2 * r_b) / (a_1 + a_2)
                        r_q = (a_3 * r_c + a_4 * r_d) / (a_3 + a_4)

                        r_ab = np.linalg.norm(r_a - r_b)
                        r_cd = np.linalg.norm(r_c - r_d)
                        r_pq = np.linalg.norm(r_p - r_q)

                        s_ab = c_1 * c_2 * n_1 * n_2 * (np.pi / (a_1 + a_2))**(3/2) * np.exp(- a_1 * a_2 * r_ab**2 / (a_1 + a_2))
                        s_cd = c_3 * c_4 * n_3 * n_4 * (np.pi / (a_3 + a_4))**(3/2) * np.exp(- a_3 * a_4 * r_cd**2 / (a_3 + a_4))

                        if r_pq > 0:
                            f_0000 = (1/2) * (np.pi * (a_1 + a_2 + a_3 + a_4) / ((a_1 + a_2) * (a_3 + a_4) * r_pq**2))**(1/2) * sp.erf(((a_1 + a_2) * (a_3 + a_4) * r_pq**2 / (a_1 + a_2 + a_3 + a_4))**(1/2))
                        else:
                            f_0000 = 1

                        f_mn += 2 * (((a_1 + a_2) * (a_3 + a_4)) / (np.pi * (a_1 + a_2 + a_3 + a_4)))**(1/2) * s_ab * s_cd * f_0000

        return f_mn
