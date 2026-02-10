# SentinelPulse-LAR: Identity-Preserving Activation with Learnable Localized Corrections


SentinelPulse-LAR (SpLR) is a mechanism-focused activation function that treats nonlinearity as a learnable, localized perturbation of the identity mapping. Developed by independent researcher Mohammad Al-Biltaji, this project introduces the SpLR architecture to address limitations of fixed-shape nonlinearities, which cannot adapt their response to local feature structure.

# Key Idea

Unlike standard activations such as ReLU (Rectified Linear Unit), GELU (Gaussian Error Linear Unit), and Mish, which apply global nonlinear transformations, SpLR reframes the activation as a micro-residual operation. It preserves the identity mapping by default and applies a signed corrective pulse only where it improves representational capacity.

# Experimental Setup

Dataset: CIFAR-100
Model: Convolutional Neural Network (same architecture for all runs)
Optimizer: Adam (Adaptive Moment Estimation)
Learning rate: 0.001
Seeds: 3
Epochs: 50
Activations compared: Mish vs SpLR

Activation,     | Epochs|,  Dropout,|      Val Acc (%)     |,Test Acc (%)

Mish (Baseline),   |50,    |0.10,         |56.26±0.32,      | 57.90±0.30

SpLR (Mine),      | 50,    |0.10,         |59.02±0.22,      | 61.75±0.32

Additional experiments and raw results are available in the Benchmarks directory.

SpLR consistently improved performance across tested settings while maintaining low variance across seeds.

# Ablation Study

Ablation experiments indicate that the learnability of the residual amplitude is a necessary condition for the observed gains.

When amplitude learning was disabled:

Test accuracy decreased from 61.75% to 55.53%, a drop of 6.22 percentage points.

This result suggests that adaptive control of localized residual strength plays a critical role in the effectiveness of the activation mechanism.

Al-Biltaji, Mohammad. 2026.
SentinelPulse-LAR: Identity-Preserving Activation with Learnable Localized Corrections.
Preprint.

