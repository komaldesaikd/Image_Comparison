import os
from PIL import Image, ImageChops
import pytest
import logging

class Test_Chaos_Image_Task:
    
    def test_image_import_export(self,image_path=os.getcwd()+"\\Images\\IMAGE_1.png",export_path=os.getcwd()+"\\Images\\IMAGE_EXPORT.jpg"):
        """
        This method takes self and two paths for local images , verifies existance of and opening of correct image and export it to jpg format

        Parameters:
            image_path (local image file path for IMAGE1.png): The image to verify after opening on desktop application.
            export_path (local image file path with jpg extension): The path to save on local with jpg extension.

        This method 1st check correct opened image from local device (compares opened image with local device image) 
        and then saves it to jpg format   
        """

        logging.info("test_image_import_export: started")
        self.image_path=image_path
        try:
            self.image1 = Image.open(self.image_path).convert('RGB')
            self.image1.show()
        except Exception as e:
            logging.error("test_image_import_export: Image open exception")
            assert False
        self.test_compare_images(self.image1,self.image_path)
        self.image1.save(export_path)
        logging.info("test_image_import_export: done")
        
    @pytest.mark.depends(on=['test_image_import_export'])
    def test_verify_exported_image(self, export_path=os.getcwd()+"\\Images\\IMAGE_EXPORT.jpg"):
        """
        This method takes self and path of exported image and verifies existance of file on device location.

        Parameters:
            export_path (local image file path with jpg extension): The image file path with jpg extension.

        This method is dependent on test_image_import_export method and it verifies existance of exported file on device location. 
        """

        logging.info("test_verify_exported_image: started")
        self.export_path=export_path
        if os.path.exists(self.export_path):
            logging.info(f"test_verify_exported_image: The file at {self.export_path} exists")
            assert True
        else:
            logging.info(f"test_verify_exported_image: The file at {self.export_path} does not exist")
            assert False
        logging.info("test_verify_exported_image: done")

    def test_compare_images(self,image_1=os.getcwd()+"\\Images\\IMAGE_EXPORT.jpg",image_2=os.getcwd()+"\\Images\\IMAGE_2.png",image_difference_path=os.getcwd()+"\\Results\\IMAGE_DIFFERENCE.png"):        
        """
        This method takes self and three images paths and compares 2 images and if they are different then create new image with difference between them.

        Parameters:
            image_1 (local image file path with jpg extension): The image file path with jpg extension to compare.
            image_2 (local image file path with png extension): The image file path with for IMAGE_2.png to compare.
            image_difference_path (IMAGE with highlighted difference): This file contains difference image .

        This method compares image_1 and image_2 and if they are different then creates new image(image_difference_path) with gighlighted difference . 
        """
        logging.info("test_compare_images: started")
        self.image_1=image_1
        self.image_2=image_2
        self.image_difference_path=image_difference_path
        if(isinstance(self.image_1, str) ):
                self.img1=Image.open(self.image_1).convert('RGB')
        else:
            self.img1=self.image_1
        if(isinstance(self.image_2, str) ):
                self.img2=Image.open(self.image_2).convert('RGB')
        else:
            self.img2=self.image_2
        self.diff = ImageChops.difference(self.img1,self.img2)
        self.difference_values=self.diff.getbbox()         
        if self.difference_values is not None:
            self.diff.save(self.image_difference_path)
            logging.error("test_compare_images: The provided images are different")
            assert False
        else:
            logging.info("test_compare_images: The provided images are same")
            assert True
        logging.info("test_compare_images: done")