
# 医学牙齿分割演示（Attention + Depthwise U-Net）

### 项目简介
本项目是一个商业化项目
基于注意力机制与深度可分离卷积等方法改进的 U-Net 模型，实现牙齿 X 光图像自动分割。  
已应用于辅助手段，旨在提升医生诊断效率。

### 性能指标（测试集）
- Dice 系数：0.91+
- IoU：0.93+
- Sensitivity：0.92+
- Specificity：0.96+
- Accuracy：0.9645

### 快速使用（演示版）
```bash
pip install -r requirements.txt  # 需配置好模型图片路径
python inference.py




