import tensorflow as tf

print(str(99))

factor_for_h = 24  # 图片height方向上的划分因子
factor_for_w = 12  # 图片width方向上的划分因子
factor_unused = 3  # 不使用图片的上面 1/factor_unused 部分
print(range(factor_for_h // factor_unused - 1, factor_for_h))

from PIL import Image, ImageDraw

im01 = Image.open("emgs/f00003.png")
draw = ImageDraw.Draw(im01)
# draw.line([(0, 0), (100, 300), (200, 500)], fill=(255, 0, 0), width=5)
# draw.line([50, 10, 100, 200, 400, 300], fill=(0, 255, 0), width=10)
# im01.show()

draw.rectangle((0, 0, 40, 20), outline="green")
draw.text([0, 0], "0_0", "red")
draw.rectangle((40, 0, 80, 20), outline="green")
draw.text([40, 0], "0_1", "red")
im01.show()

re = tf.contrib.layers.l2_regularizer(0.0001)