class SPv5_2d(nn.Module):
    """
    SPv5 activation for Conv2d outputs.

    Formula:
        y = x + α * x * exp(-β * x^2)

    Golden Init:
        α_raw init = 0.182  → α = 2 * tanh(α_raw)  ≈ 0.36 at start
            - shape: (1, C, 1, 1)  [per-channel, broadcasts over H,W]
            - trainable, not stage-shared

        β_raw init = -1.35 → β = 0.01 + softplus(β_raw) ≈ 0.24 at start
            - scalar (one per activation block)
            - trainable, stage-shared, positive-only
    """
    def __init__(self, num_channels: int):
        super().__init__()
        # α_raw: one parameter per channel
        self.alpha_raw = nn.Parameter(torch.full((1, num_channels, 1, 1), 0.182))
        # β_raw: single scalar for the whole block
        self.beta_raw  = nn.Parameter(torch.tensor(-1.35))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        alpha = 2.0 * torch.tanh(self.alpha_raw)          # local amplitude
        beta  = 0.01 + F.softplus(self.beta_raw)          # positive width
        return x + alpha * x * torch.exp(-beta * x * x)   # identity + localized bump


class SPv5_1d(nn.Module):
    """
    SPv5 activation for Linear (fully-connected) outputs.

    Same formula as SPv5_2d, but α_raw has shape (1, F)
    so it broadcasts over the batch dimension.
    """
    def __init__(self, num_features: int):
        super().__init__()
        # α_raw: one parameter per feature
        self.alpha_raw = nn.Parameter(torch.full((1, num_features), 0.182))
        # β_raw: scalar shared for this block
        self.beta_raw  = nn.Parameter(torch.tensor(-1.35))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        alpha = 2.0 * torch.tanh(self.alpha_raw)
        beta  = 0.01 + F.softplus(self.beta_raw)
        return x + alpha * x * torch.exp(-beta * x * x)
