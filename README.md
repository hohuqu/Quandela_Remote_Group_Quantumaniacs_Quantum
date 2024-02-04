# Quandela_Remote_Group_Quantumaniacs_Quantum

## Collaborators: 
* Phuong Khanh Tran
* Quan Huu Ho
* Malihe Yadavar
* Marcin Kepa

## Introduction
This project repository is a part of iQuHACK 2024, MIT's annual quantum hackathon. 

## About iQuHACK 2024
* [iQuHACK 2024](https://www.iquise.mit.edu/iQuHACK/2024-02-02)
* [Quandela Challenge](https://github.com/iQuHACK/2024_Quandela_Remote)

## Solution
We initiated our exploration by constructing a quantum circuit using the Perceval library for quantum computing. Our primary focus was implementing a Toffoli-sign gate within the realm of deterministic polarization-encoded qubits<sup>[1]</sup>, drawing inspiration from the insights presented in the research paper "Efficient Toffoli gates using qudits" [2]. In addition, we delved into the intricacies of non-deterministic post-selection and the beamsplitter test [3]. Our comprehensive solution encompassed the incorporation of Hadamard gates, beamsplitters, and post-selection [4]. To evaluate the performance and fidelity of our approach, we subjected it to analysis using the Perceval algorithm.

Expanding our horizons into quantum optics [5], we assessed second-order correlation function (g2) values. This exploration allowed us to calculate the entanglement parameter (S) across various input states, providing a nuanced understanding of our quantum system's behavior. We used a nested loop to iterate through the specified parameters and used the Perceval library to configure the quantum processing unit (QPU) with different multiphoton components. The entanglement parameter ‘E’ was determined through a different combination of input states and the entanglement parameter ‘S’ was computed from ‘E’ with respect to the ‘g2’ value. THe process was visualized with a progressed bar and the results were printed for analysis for further insight.



## Instructions


## Dependencies
* Python >=3.8, <=3.12
* perceval-quandela==0.10.3
* numpy
* matplotlib
* tqdm

## Installation
pip install perceval-quandela

## References
[1] A. P. Lund and T. C. Ralph, “Non-deterministic Gates for Photonic Single Rail Quantum Logic,” Phys. Rev. A, vol. 66, no. 3, p. 032307, Sep. 2002, doi: 10.1103/PhysRevA.66.032307.

[2] T. C. Ralph, K. J. Resch, and A. Gilchrist, “Efficient Toffoli gates using qudits,” Phys. Rev. A, vol. 75, no. 2, p. 022313, Feb. 2007, doi: 10.1103/PhysRevA.75.022313.

[3] E. Knill, “Quantum gates using linear optics and postselection,” Phys. Rev. A, vol. 66, no. 5, p. 052306, Nov. 2002, doi: 10.1103/PhysRevA.66.052306.

[4] E. Knill, R. Laflamme, and G. Milburn, “Efficient Linear Optics Quantum Computation.” arXiv, Jun. 20, 2000. doi: 10.48550/arXiv.quant-ph/0006088.

[5] E. Knill, R. Laflamme, and G. J. Milburn, “A scheme for efficient quantum computation with linear optics,” Nature, vol. 409, no. 6816, Art. no. 6816, Jan. 2001, doi: 10.1038/35051009.

[6] N. Maring et al., “A general-purpose single-photon-based quantum computing platform.” arXiv, Jun. 01, 2023. doi: 10.48550/arXiv.2306.00874.

[7] Y. Wang et al., “Quantum generative adversarial learning in photonics,” Opt. Lett., OL, vol. 48, no. 20, pp. 5197–5200, Oct. 2023, doi: 10.1364/OL.505084.

[8] D. B. Uskov, L. Kaplan, A. M. Smith, S. D. Huver, and J. P. Dowling, “Maximal Success Probabilities of Linear-Optical Quantum Gates,” Phys. Rev. A, vol. 79, no. 4, p. 042326, Apr. 2009, doi: 10.1103/PhysRevA.79.042326.

