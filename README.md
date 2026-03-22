
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
pip install -r requirements.txt  # 需配置好模型图片路径
python inference.py


### 创建虚拟环境（推荐）

python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

### 安装依赖
pip install -r requirements.txt


### 获取模型文件
模型文件（TorchScript 格式）已包含在仓库的 models/ 目录中，文件名为 tooth_segmentation_model.pt。
你也可以从 Releases 页面下载最新版本。

⚠️ 注意：模型文件为基础版本，仅供演示和测试使用。如需商用或定制训练，请联系作者。

### 使用方法
## 基础用法
- 修改 inference.py 中的文件路径
- 设置 model_path 为模型文件的实际路径。
- 设置 image_path 为待分割的 X 光图片路径。

### 运行推理
python inference.py

命令行参数（可选）
你可以将 inference.py 改造为支持命令行参数，例如：

python inference.py --model models/tooth_segmentation_model.pt --image test.png --threshold 0.5



