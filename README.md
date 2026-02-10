# SentinelPulse-LAR: Identity-Preserving Activation with Learnable Localized Corrections


SentinelPulse-LAR: Identity-Preserving Activation with Learnable Localized Corrections

SentinelPulse-LAR (SpLR) is a mechanism-focused activation function that treats nonlinearity as a learnable, localized perturbation of the identity mapping. Developed by independent researcher Mohammad AL-Biltaji, this project introduces the SpLR (New name for SPv5) architecture to solve the "blindness" of fixed-shape nonlinearities

Key Innovation
Unlike standard activations (ReLU, GELU, Mish) that apply global transformations, SpLR reframes the activation as a micro-residual operation. It preserves the identity mapping by default and "pulses" a signed correction only where it improves representational capacity.

Dataset: CIFAR-100

Model: CNN (same architecture for all runs)

Optimizer: Adam

Learning rate: 0.001

Seeds: 3

Epochs: 50

Activations compared: Mish vs SpLR

Activation,     | Epochs|,  Dropout,|      Val Acc (%)     |,Test Acc (%)

Mish (Baseline),   |50,    |0.10,         |56.26±0.32,      | 57.90±0.30

SpLR (Mine),      | 50,    |0.10,         |59.02±0.22,      | 61.75±0.32

this result and many more are found in the benchmarks file
Why it works (Ablation Evidence)
My ablation studies prove that Claim 3—the learnability of the residual amplitude—is a necessary condition for gains. When amplitude learning was disabled, performance dropped significantly by 6.22%.

amplitude learning disabled  
Test accuracy dropped from 61.75% → 55.53%


Al-Biltaji, Mohammad. 2026.
SentinelPulse-LAR: Identity-Preserving Activation with Learnable Localized Corrections.
Preprint.

