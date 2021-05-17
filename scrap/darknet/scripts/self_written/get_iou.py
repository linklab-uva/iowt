def adjust_coordinates(center_x, center_y, width, height):
	scale_width = width / 2
	scale_height = height / 2
	return [center_x - scale_width, center_y - scale_height, center_x + scale_width, center_y + scale_height]

def iou(box1, box2):
    (box1_x1, box1_y1, box1_x2, box1_y2) = box1
    (box2_x1, box2_y1, box2_x2, box2_y2) = box2
    
    # Calculate the (yi1, xi1, yi2, xi2) coordinates of the intersection of box1 and box2. Calculate its Area.
    xi1 = max(box1_x1, box2_x1)
    yi1 = max(box1_y1, box2_y1)
    xi2 = min(box1_x2, box2_x2)
    yi2 = min(box1_y2, box2_y2)
    inter_width = max(xi2 - xi1, 0)
    inter_height = max(yi2 - yi1, 0)
    inter_area = inter_width * inter_height

    # Calculate the Union area by using Formula: Union(A,B) = A + B - Inter(A,B)
    box1_area = (box1_y2 - box1_y1) * (box1_x2 - box1_x1)
    box2_area = (box2_y2 - box2_y1) * (box2_x2 - box2_x1)
    union_area = (box1_area + box2_area) - inter_area
    
    # compute the IoU
    iou = inter_area / union_area
    
    return iou

bottle_model1_iou = iou(adjust_coordinates(0.417355, 0.402060, 0.035918, 0.126983), adjust_coordinates(0.411490, 0.403715, 0.050857, 0.181157))
cup_model1_iou = iou(adjust_coordinates(0.446469, 0.704031, 0.049834, 0.076369), adjust_coordinates(0.443043, 0.700387, 0.033602, 0.067991))
paper_model1_iou = iou(adjust_coordinates(0.470100, 0.393174, 0.056266, 0.157473), adjust_coordinates(0.464922, 0.404130, 0.040065, 0.113696))

bottle_model2_iou = iou(adjust_coordinates(0.413684, 0.391464, 0.045635, 0.150140), adjust_coordinates(0.411490, 0.403715, 0.050857, 0.181157))
cup_model2_iou = iou(adjust_coordinates(0.445430, 0.701755, 0.039439, 0.078838), adjust_coordinates(0.443043, 0.700387, 0.033602, 0.067991))
paper_model2_iou = iou(adjust_coordinates(0.465155, 0.398555, 0.052507, 0.091961), adjust_coordinates(0.464922, 0.404130, 0.040065, 0.113696))

print(bottle_model1_iou, cup_model1_iou, paper_model1_iou)
print(bottle_model2_iou, cup_model2_iou, paper_model2_iou)
