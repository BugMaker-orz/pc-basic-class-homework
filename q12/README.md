# 第12题：PyTorch 线性回归训练

**主题**：PyTorch 基础训练循环

## 题目要求

在 `q12` 中补全线性回归训练：

- 固定随机种子，构造 `y = 3x - 1` 的线性数据
- 补全训练循环：`zero_grad` 清梯度、`backward` 反向传播、`step` 更新参数
- 训练后进入评估模式，用 `no_grad` 计算最终损失，要求损失小于 0.001
- 禁止直接给 weight / bias 赋值

## 训练脚本要点（train.py）

```python
torch.manual_seed(20260907)
x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 3 * x - 1

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for _ in range(200):
    pred = model(x)
    loss = loss_fn(pred, y)
    opt.zero_grad()   # 清空梯度（PyTorch 默认累加）
    loss.backward()   # 反向传播
    opt.step()        # 更新参数

model.eval()          # 评估模式
with torch.no_grad():
    print(f"final loss: {loss_fn(model(x), y).item():.6f}")
    print(f"weight: {model.weight.item():.4f}")
    print(f"bias: {model.bias.item():.4f}")
```

## 运行结果

```
final loss: 0.000000
weight: 3.0000
bias: -1.0000
```

## 关键技术点

- **梯度清零**：PyTorch 梯度默认累加，每个 batch 前必须 `zero_grad()`
- **训练/评估模式**：`model.eval()` 关闭训练期行为，`no_grad()` 关闭梯度追踪、节省内存
- **收敛验证**：损失低于阈值且参数收敛到真值（3, -1），说明训练循环本身正确
