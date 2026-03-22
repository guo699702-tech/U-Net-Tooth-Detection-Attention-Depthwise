
# 医学牙齿分割演示（Attention + Depthwise U-Net）

### 项目简介
本项目是一个商业化项目
基于注意力机制与深度可分离卷积等方法改进的 U-Net 模型，实现牙齿 X 光图像自动分割。  
已应用于辅助手段，旨在提升医生诊断效率。

### 数据说明
- 本模型使用**完全自建的私有临床数据集**进行训练和验证。
- 数据覆盖**儿童 → 青少年 → 成人 → 中老年**全年龄段。
- 包含多种临床场景：正常牙列、缺牙/种植、拥挤重叠、金属修复体伪影、低对比度/模糊片等。
- 所有数据均为真实口腔全景X光片（panoramic radiograph），经过专业医生标注，确保高质量。
- 为保护隐私与数据安全，数据集不公开，仅用于模型内部训练。
  
### 获取模型文件
模型文件（TorchScript 格式）已包含在仓库的 models/ 目录中，文件名为 tooth_segmentation_model.pt。
⚠️ 注意：模型文件**仅为基础版本，供演示和测试使用**。如需商用或定制训练，请联系作者。


### 性能指标（测试集）
- Dice 系数：0.91+
- IoU：0.93+
- Sensitivity：0.92+
- Specificity：0.96+
- Accuracy：0.9645

### 性能指标（独立测试集）

| 指标       | 值       | 说明                          |
|------------|----------|-------------------------------|
| Dice系数   | 0.91+   | 平均Dice分数（分割重叠度）    |
| IoU        | 0.93+   | 平均交并比                    |
| 敏感性     | 0.92+   | 对牙齿区域的召回率            |
| 特异性     | 0.96+   | 对背景区域的正确拒绝率        |
| 像素准确率 | 0.9645  | 整体像素级分类准确率          |

以上指标基于内部未参与训练的独立测试集获得。

### 使用方法
#### 基础用法
- 修改 inference.py 中的文件路径
- 设置 model_path 为模型文件的实际路径。
- 设置 image_path 为待分割的 X 光图片路径。

### 创建虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```
### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行推理
```bash
python inference.py
```
命令行参数（可选）
你可以将 inference.py 改造为支持命令行参数，例如：
```bash
python inference.py --model models/tooth_segmentation_model.pt --image test.png --threshold 0.5
```

### 图片实例展示
<img width="1470" height="244" alt="4d5e08f9-957d-416b-85c7-976522cf2749" src="https://github.com/user-attachments/assets/49f667cd-d2d8-4ad2-8f59-b886bb476b18" />


