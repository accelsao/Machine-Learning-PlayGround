import torch
import math
import torch.nn as nn
from torch.nn.parameter import Parameter

# Dynamic Few-Shot Visual Learning without Forgetting: https://arxiv.org/abs/1804.09458
# Large-Scale Long-Tailed Recognition in an Open World: https://arxiv.org/abs/1904.05160

class Cosine_Norm_Classifier(nn.Module):
    def __init__(self, in_ch, out_ch, scale=16):
        super(Cosine_Norm_Classifier, self).__init__()
        self.scale = scale
        self.out_ch = out_ch
        self.in_ch = in_ch
        self.weight = Parameter(torch.Tensor(out_ch, in_ch))
        self.reset_parameters()
        # Why weight classifer is uniform[std], and why cos_classifier works ?

    def reset_parameters(self):
        stdv = 1. / math.sqrt(self.weight.size(1))
        self.weight.data.uniform_(-stdv, stdv)



