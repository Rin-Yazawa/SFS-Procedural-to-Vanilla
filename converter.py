import time

list_line = []

print("Enter your blueprint text (double enter to end):")

while True:
    enter_check = input()
    if enter_check == "":
        break
    list_line.append(enter_check)

file = "\n".join(list_line)

filter = 0

print("------------------------")

while True:
    filter = file.find("Procedural Fuel Tank New", filter + 1)
    x_pos = file.find("x", filter) + 4
    end_x_pos = file.find(",", x_pos)
    x_pos_float = float((file[x_pos:end_x_pos]))
    x_pos_proc = file.find("x_position_target", filter) + 20
    end_x_pos_proc = file.find(",", x_pos_proc)
    x_pos_float_proc = float((file[x_pos_proc:end_x_pos_proc]))
    x_pos_conv = (x_pos_float + x_pos_float_proc)
    y_pos = file.find("y", filter) + 4
    end_y_pos = file.find(" ", y_pos + 1)
    y_pos_string = file[y_pos:end_y_pos]
    y_pos_string = y_pos_string[:-1]
    y_pos_float = float(y_pos_string)
    y_pos_proc = file.find("y_position_target", filter) + 20
    end_y_pos_proc = file.find(",", y_pos_proc)
    y_pos_float_proc = float((file[y_pos_proc:end_y_pos_proc]))
    y_pos_conv = (y_pos_float + y_pos_float_proc)
    width_a = file.find("width_a", filter) + 10
    end_width_a = file.find(",", width_a)
    width_a_float = float((file[width_a:end_width_a]))
    width_a_smooth = file.find("width_a_smooth", filter) + 17
    end_width_a_smooth = file.find(",", width_a_smooth)
    width_a_smooth_float = float((file[width_a_smooth:end_width_a_smooth]))
    width_a_conv = width_a_float + (width_a_smooth_float - 1)
    width_b = file.find("width_b", filter) + 10
    end_width_b = file.find(",", width_b)
    width_b_float = float((file[width_b:end_width_b]))
    width_b_smooth = file.find("width_d_smooth", filter) + 17
    end_width_b_smooth = file.find(",", width_b_smooth)
    width_b_smooth_float = float((file[width_b_smooth:end_width_b_smooth]))
    width_b_conv = width_b_float + (width_b_smooth_float - 1)
    height = file.find("height", filter) + 9
    end_height = file.find(",", height)
    height_float = float((file[height:end_height]))
    height_smooth = file.find("height_smooth", filter) + 16
    end_height_smooth = file.find(",", height_smooth)
    height_smooth_float = float((file[height_smooth:end_height_smooth]))
    height_conv = height_float + (height_smooth_float - 1)
    rot = file.find("z", filter) + 4
    end_rot = file.find(" ", rot + 1)
    rot_string = file[rot:end_rot]
    rot_string = rot_string[:-1]
    rot_float = float(rot_string)
    rot_proc = file.find("angle_z_target", filter) + 17
    end_rot_proc = file.find(",", rot_proc)
    rot_proc_float = float((file[rot_proc:end_rot_proc]))
    rot_smooth = file.find("angle_z_soomth_target", filter) + 24
    end_rot_smooth = file.find(",", rot_smooth)
    rot_smooth_float = float((file[rot_smooth:end_rot_smooth]))
    rot_conv = (rot_float + rot_proc_float + rot_smooth_float)
    x_size = file.find("x_size_time", filter) + 14
    end_x_size = file.find(",", x_size)
    x_size_float = float((file[x_size:end_x_size]))
    x_size_smooth = file.find("x_soomth_size_time", filter) + 21
    end_x_size_smooth = file.find(",", x_size_smooth)
    x_size_smooth_float = float((file[x_size_smooth:end_x_size_smooth]))
    x_size_conv = x_size_float * x_size_smooth_float
    y_size = file.find("y_size_time", filter) + 14
    end_y_size = file.find(",", y_size)
    y_size_float = float((file[y_size:end_y_size]))
    y_size_smooth = file.find("y_soomth_size_time", filter) + 21
    end_y_size_smooth = file.find(",", y_size_smooth)
    y_size_smooth_float = float((file[y_size_smooth:end_y_size_smooth]))
    y_size_conv = y_size_float * y_size_smooth_float
    burn_mark = file.find("depth_target", filter) + 15
    end_burn_mark = file.find(",", burn_mark)
    burn_mark_float = float((file[burn_mark:end_burn_mark]))
    burn_mark_conv = burn_mark_float / 4
    fuel = file.find("fuel_percent", filter) + 14
    end_fuel = file.find(" ", fuel + 1)
    fuel_string= file[fuel:end_fuel]
    fuel_string = fuel_string[:-1]
    fuel_string_float = float(fuel_string)
    width_fix = max(width_a_conv, width_b_conv)
    print(f'''    {{
      "n": "Fuel Tank",
      "p": {{
        "x": {x_pos_conv},
        "y": {y_pos_conv}
      }},
      "o": {{
        "x": {x_size_conv},
        "y": {y_size_conv},
        "z": {rot_conv}
      }},
      "t": "-Infinity",
      "N": {{
        "width_original": {width_fix},
        "width_a": {width_a_conv},
        "width_b": {width_b_conv},
        "height": {height_conv},
        "fuel_percent": {fuel_string_float}
      }},
      "burns": {{
        "angle": -90.58417,
        "intensity": {burn_mark_conv},
        "x": -0.0509633645,
        "top": "",
        "bottom": ""
}},
      "T": {{
        "color_tex": "_",
        "shape_tex": "_"
      }}
    }},''')

print(fuel_string_float)
print(burn_mark_conv)
print(y_size_conv)
print(x_size_conv)
print(rot_conv)
print(height_conv)
print(width_a_conv)
print(width_b_conv)
print(x_pos_conv)
print(y_pos_conv)