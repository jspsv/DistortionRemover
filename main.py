# pip install tqdm
from tqdm import tqdm

# local modules
from remove_distortion import DistortionRemover
from utils import read_image_file, write_image_file, create_output_folder


def main():
    working_dir, output_path = create_output_folder()
    img_file_list = list(working_dir.glob('**/*.bmp'))

    for i, img_file in enumerate(tqdm(img_file_list)):
        src = read_image_file(img_file)
        dst = DistortionRemover(src).barrel_undist()
        out_file = str(output_path / (img_file.stem + "_undist.bmp"))
        write_image_file(dst, out_file)

    return True


if __name__ == "__main__":
    main()
