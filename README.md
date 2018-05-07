# 使用 TensorFlow 识别教学一体化服务平台图像验证码

> 实验性demo，使用 TensorFlow 识别教学一体化服务平台图像验证码


## 使用

```bash
python prepare.py # 生成测试数据
python train.py # 训练
python work.py < test.jpg # 识别 test.jpg
```




如果不喜欢我提供的实验数据（我提供的完全够用了），想自动获取训练数据:
```bash
php getCaptcha.php
```
注：[请申请开发者权限填写getCaptcha中的role和hash，如果没有权限，请乖乖手动更新或服用原有数据](https://dev.sky31.com/api-idcode.html)

