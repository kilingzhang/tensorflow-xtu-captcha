# 使用 TensorFlow 识别教学一体化服务平台图像验证码

## 使用
```bash
如果想自动获取新的验证码：
php getCaptcha.php
（[请自行申请开发者权限](https://dev.sky31.com/api-idcode.html)）

python prepare.py # 生成测试数据
python train.py # 训练
python work.py < test.jpg # 识别 test.jpg
```
