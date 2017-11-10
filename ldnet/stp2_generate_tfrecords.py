import os
import tensorflow as tf
from PIL import Image

cwd = os.getcwd()


def generate_tfrecords(labeled_merged_cells_dir, generated_records_name):
    """
    Generate tfrecords file.
    :param labeled_merged_cells_dir: labeled and merged cells dir.
    :param generated_records_name: the neme of tfrecords file.
    :return: no return. but generate tfrecords in current dir.
    """
    classes = ["lane_cells", "road_surface_cells", "cluttered_cells"]
    writer = tf.python_io.TFRecordWriter(generated_records_name)

    for class_index, class_name in enumerate(classes):
        class_path = cwd + "/" + labeled_merged_cells_dir + "/" + class_name
        for cell_name in os.listdir(class_path):
            cell_path = class_path + "/" + cell_name
            cell = Image.open(cell_path)
            cell = cell.resize((32, 32))
            cell_raw = cell.tobytes()
            example = tf.train.Example(features=tf.train.Features(feature={
                "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[class_index])),
                'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[cell_raw]))
            }))
            writer.write(example.SerializeToString())
    writer.close()


def main(_):
    generate_tfrecords(labeled_merged_cells_dir="dir1_merged_cells", generated_records_name="ldnet_train.tfrecords")
    print("generated tfrecord.")


if __name__ == '__main__':
    tf.app.run()
