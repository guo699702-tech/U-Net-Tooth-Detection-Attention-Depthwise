import torch
import numpy as np
import cv2
from PIL import Image
import torchvision.transforms as transforms
import matplotlib.pyplot as plt  
import os                        
class ToothSegmentor:
    def __init__(self, model_path="tooth_segmentation_model.pt", device="cuda"):
        self.device = torch.device(device if torch.cuda.is_available() else "cpu")
        self.model = torch.jit.load(model_path, map_location=self.device)
        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor()
        ])

    @torch.no_grad()
    def predict(self, image_path, threshold=0.5):
        """单张图像推理"""
        img = Image.open(image_path).convert("RGB")
        orig_size = img.size

        # 预处理
        tensor = self.transform(img).unsqueeze(0).to(self.device)

        # 推理
        prob = torch.sigmoid(self.model(tensor))
        prob = prob.squeeze().cpu().numpy()

        # 后处理
        prob_resized = cv2.resize(prob, orig_size, interpolation=cv2.INTER_LINEAR)
        mask = (prob_resized > threshold).astype(np.uint8) * 255

        return mask


# 使用示例
if __name__ == "__main__":
    # 请使用人员配置路径
    model_path = "model.pt" # 模型路径
    image_path = "image.png" # 图片路径
    save_dir = "results"  # 结果保存目录

    # 初始化分割器
    segmentor = ToothSegmentor(model_path)

    # 预测掩码
    mask = segmentor.predict(image_path)
    print(f"分割完成，掩码尺寸: {mask.shape}")

    os.makedirs(save_dir, exist_ok=True)
    img_pil = Image.open(image_path).convert("RGB")
    img_np = np.array(img_pil)
    overlay = img_np.copy()
    overlay[mask > 127] = [255, 0, 0]  
    blended = cv2.addWeighted(img_np, 0.7, overlay, 0.3, 0)

    # 绘制三联图
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(img_np)
    axes[0].set_title("image")
    axes[0].axis("off")

    axes[1].imshow(mask, cmap="gray")
    axes[1].set_title("mask")
    axes[1].axis("off")

    axes[2].imshow(blended)
    axes[2].set_title("overlay")
    axes[2].axis("off")

    plt.tight_layout()

    save_path = os.path.join(save_dir, f"{os.path.splitext(os.path.basename(image_path))[0]}_viz.png")
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"可视化结果已保存至: {save_path}")