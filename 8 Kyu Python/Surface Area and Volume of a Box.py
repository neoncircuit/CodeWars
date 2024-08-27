def get_size(w,h,d):
    #your code here
    area = 2 * ((w*h)+(h*d)+(d*w))
    volume = w * h * d
    return [area, volume]
