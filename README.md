# Image_Association_Prediction

	Solution 1 :- 
	
		In this approach, I have taken two sample images from the cropped and original. By applying TM_CCOEFF_NORMED technique , which simply slides the cropped image over the original image (as in 2D convolution) and compares the cropped and patch of original image under the cropped image. If original image is of size (WxH) and cropped image is of size (wxh), output image will have a size of (W-w+1, H-h+1). Once you got the result, you can use cv2.minMaxLoc() function to find where is the maximum/minimum value.
The coordinates of the cropped image associated with the original image yields the output in JSON.
Disadvantage of this approach, there is no adjustment of multi-image scaling. For that we will refer to solution 2.
	
	To Run:- 
		Python New_Testing.py

		
	Solution 2 :-
	
	In this case, all we need to do is apply a little trick:

1.	Loop over the input image at multiple scales (i.e. make the input image progressively smaller and smaller).
2.	Apply template matching using cv2.matchTemplate  and keep track of the match with the largest correlation coefficient (along with the x, y-coordinates of the region with the largest correlation coefficient).

3.	After looping over all scales, take the region with the largest correlation coefficient and use that as your “matched” region.

Finally we will get a bounding box on detected area, where we can see the associated crop image marked on the original image


	To Run:
		python match.py --template image_107.png --images images_1
