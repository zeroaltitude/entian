import math
import sys

from PIL import Image, ImageDraw


MODE = "RGBA"
BGCOLOR = "#FFFFFF"
DOTCOLOR = "#ddd"
CAPDOTCOLOR = "#f00"
LINECOLOR = "#111111"
DARK = "#000000"
NEGABET = "jkhinolmbcafgdezxyrspqvwtu"
# rotations
# scorpio   Fixed water 4 * 5       20
# sagittar  Mutable fire 2 * 6      12
# capricor  Cardinal earth 1 * 3    3
# aquarius  Fixed air 3 * 5         15
# pisces    Mutable water 4 * 6     24
# aries     cardinal fire 1 * 2     2
# taurus    Fixed earth 3 * 2       6
# gemini    Mutable air 5 * 6       30
# cander    Cardinal water 1 * 4    4
# leo       Fixed fire 2 * 4        8
# virgo     Mutable earth 6 * 3     18
# libra     Cardinal air 1 * 5      5
ROTS = [20, 12, 3, 15,
        24, 2, 6, 30,
        4, 8, 18, 5]

CHARS_ARS = {
    '0': [
        [[1, 0], [3, 0]],
        [[3, 0], [4, 1]],
        [[4, 1], [4, 3]],
        [[4, 3], [3, 4]],
        [[3, 4], [1, 4]],
        [[1, 4], [0, 3]],
        [[0, 3], [0, 1]],
        [[0, 1], [1, 0]],
    ],
    '1': [
        [[3, 0], [3, 4]],
    ],
    '2': [
        [[1, 0], [3, 0]],
        [[3, 0], [4, 1]],
        [[4, 1], [4, 3]],
        [[4, 3], [0, 4]],
        [[0, 4], [4, 4]],
    ],
    '3': [
        [[0, 0], [0, 4]],
        [[0, 2], [4, 2]],
        [[0, 4], [4, 4]],
        [[4, 0], [4, 4]],
    ],
    '4': [
        [[3, 0], [3, 4]],
        [[3, 0], [0, 2]],
        [[0, 2], [4, 2]],
    ],
    '5': [
        [[0, 0], [4, 0]],
        [[0, 0], [0, 2]],
        [[0, 2], [2, 2]],
        [[2, 2], [4, 4]],
        [[4, 4], [0, 4]]
    ],
    '6': [

    ],
    '7': [

    ],
    '8': [
        [[0, 0], [4, 0]],
        [[0, 0], [0, 4]],
        [[4, 0], [4, 4]],
        [[0, 4], [4, 4]],
        [[0, 2], [4, 2]],
    ],
    '9': [
        [[0, 0], [4, 0]],
        [[4, 0], [4, 4]],
        [[0, 0], [0, 2]],
        [[0, 2], [4, 2]],
        [[2, 4], [4, 4]],
    ],
    'a': [
        [[4, 0], [4, 4]],
        [[0, 4], [4, 4]],
    ],
    'b': [
        [[0, 0], [2, 4]],
        [[4, 0], [2, 4]],
    ],
    'c': [
        [[0, 0], [4, 0]],
        [[0, 2], [4, 2]],
        [[0, 4], [4, 4]],
        [[4, 0], [4, 4]],
    ],
    'd': [
        [[0, 0], [4, 0]],
        [[0, 2], [4, 2]],
        [[4, 0], [4, 4]],
    ],
    'e': [
        [[2, 0], [2, 4]],
        [[0, 2], [4, 2]],
    ],
    'f': [
        [[1, 0], [3, 0]],
        [[3, 0], [4, 1]],
        [[4, 1], [4, 3]],
        [[4, 3], [3, 4]],
        [[3, 4], [1, 4]],
        [[1, 4], [0, 3]],
        [[0, 3], [0, 1]],
        [[0, 1], [1, 0]],
        [[0, 0], [4, 4]],
    ],
    'g': [
        [[0, 0], [0, 4]],
        [[0, 0], [2, 0]],
        [[2, 0], [2, 2]],
        [[2, 2], [0, 2]],
        [[2, 2], [4, 4]],
    ],
    'h': [
        [[1, 0], [3, 0]],
        [[3, 0], [4, 1]],
        [[4, 1], [4, 3]],
        [[4, 3], [3, 4]],
        [[3, 4], [1, 4]],
        [[1, 4], [0, 3]],
        [[0, 3], [0, 1]],
        [[0, 1], [1, 0]],
        [[0, 2], [4, 2]],
    ],
    'i': [
        [[2, 0], [0, 4]],
        [[0, 4], [4, 4]],
        [[4, 4], [2, 0]],
    ],
    'j': [
        [[0, 0], [4, 0]],
        [[2, 0], [2, 3]],
        [[2, 3], [1, 4]],
        [[1, 4], [0, 4]],
    ],
    'k': [
        [[0, 0], [4, 4]],
    ],
    'l': [
        [[0, 0], [4, 0]],
        [[4, 0], [4, 4]],
        [[4, 4], [0, 4]],
        [[0, 4], [0, 0]],
        [[4, 0], [0, 4]],
    ],
    'm': [
        [[1, 0], [3, 0]],
        [[3, 0], [4, 1]],
        [[4, 1], [4, 3]],
        [[4, 3], [3, 4]],
        [[3, 4], [1, 4]],
        [[1, 4], [0, 3]],
        [[0, 3], [0, 1]],
        [[0, 1], [1, 0]],
        [[2, 2], [0, 4]],
    ],
    'n': [
        [[1, 0], [3, 0]],
        [[3, 0], [4, 1]],
        [[4, 1], [4, 3]],
        [[4, 3], [3, 4]],
        [[3, 4], [1, 4]],
        [[1, 4], [0, 3]],
        [[0, 3], [0, 1]],
        [[0, 1], [1, 0]],
        [[2, 0], [2, 4]],
    ],
    'o': [
        [[0, 0], [4, 0]],
        [[2, 0], [2, 4]],
    ],
    'p': [
        [[0, 0], [4, 0]],
        [[0, 4], [2, 2]],
        [[2, 2], [4, 4]],
    ],
    'q': [
        [[1, 0], [3, 0]],
        [[3, 0], [4, 1]],
        [[4, 1], [4, 3]],
        [[4, 3], [3, 4]],
        [[3, 4], [1, 4]],
        [[1, 4], [0, 3]],
        [[0, 3], [0, 1]],
        [[0, 1], [1, 0]],
        [[2, 2], [4, 4]],
    ],
    'r': [
        [[2, 0], [2, 4]],
        [[0, 4], [4, 4]],
    ],
    's': [
        [[0, 0], [4, 0]],
        [[0, 2], [4, 2]],
        [[0, 0], [0, 4]],
    ],
    't': [
        [[0, 0], [0, 4]],
        [[0, 2], [4, 2]],
        [[4, 0], [4, 4]],
    ],
    'u': [
        [[1, 0], [2, 2]],
        [[4, 0], [2, 2]],
        [[2, 2], [2, 4]],
    ],
    'v': [
        [[0, 0], [4, 0]],
        [[4, 0], [4, 4]],
        [[4, 4], [0, 4]],
    ],
    'w': [
        [[2, 0], [0, 4]],
        [[2, 0], [4, 4]],
        [[1, 2], [3, 2]],
    ],
    'x': [
        [[0, 0], [4, 0]],
        [[2, 0], [2, 3]],
        [[2, 3], [3, 4]],
        [[3, 4], [4, 4]],
    ],
    'y': [
        [[0, 0], [4, 0]],
        [[4, 0], [4, 4]],
        [[4, 4], [0, 4]],
        [[0, 4], [0, 0]],
    ],
    'z': [
        [[0, 0], [4, 0]],
        [[4, 0], [0, 4]],
        [[0, 4], [4, 4]],
    ],
}


def char_to_negabet(char_):
    capitalize = False
    if char_.upper() == char_:
        capitalize = True
    print("char is %s (%s)" % (char_, capitalize))
    ordin = ord(char_.upper()) - 65
    print("ord %s" % ordin)
    negord = NEGABET[ordin]
    print("char %s capitalize? %s now translated to %s (%s)" % (char_, capitalize, negord, ordin))
    return ordin, negord, capitalize


def card_tate(ordin, card):
    newordin = (ordin + ROTS[card]) % 26
    char_ = NEGABET[newordin]
    print("%s (%s) using %s (%s) now %s" % (ordin, NEGABET[ordin], card, newordin, char_))
    return char_


def char_to_tuple_rotated(char_, card):
    ordin, newchar, capitalize = char_to_negabet(char_)
    print("%s translated to %s, %s" % (char_, newchar, capitalize))
    newerchar = card_tate(ordin, card)
    print("%s translated to %s" % (newchar, newerchar))
    return newerchar, capitalize


def draw_dots(draw, offset_x=0, offset_y=0):
    DOTS.clear()
    for y in range(GRID):
        for x in range(GRID):
            distance = (SIZE - 1) / (GRID - 1)
            gridx = (x * distance) + offset_x
            gridy = (y * distance) + offset_y
            draw.point((gridx, gridy), fill=DOTCOLOR)
            DOTS.append([gridx, gridy])


def draw_line(draw, character_arr):
    point_idx_a = character_arr[0][0] + character_arr[0][1] * GRID
    point_idx_b = character_arr[1][0] + character_arr[1][1] * GRID
    gridax = DOTS[point_idx_a][0]
    griday = DOTS[point_idx_a][1]
    gridbx = DOTS[point_idx_b][0]
    gridby = DOTS[point_idx_b][1]
    xy = (gridax, griday, gridbx, gridby)
    # print("guessing coords %s, %s, %s, %s\n" % xy)
    draw.line(xy, fill=LINECOLOR, width=1, joint=None)


def char_capitalize(canvas_draw):
    canvas_draw.point((DOTS[8][0], DOTS[8][1]), fill=CAPDOTCOLOR)


def append_output(character_arr, offset_x, offset_y, canvas_draw, should_capitalize=False):
    draw_dots(canvas_draw, offset_x, offset_y)
    if should_capitalize:
        char_capitalize(canvas_draw)
    # print("snake chars to draw is: %s" % snake_chars)
    draw_line(canvas_draw, character_arr)


def loop_glyphs(word, card, canvas_draw=None, offset_y_index=0):
    page_margin_x = 2
    page_margin_y = 22
    vertical_line_margin = 10
    horizontal_char_margin = 20
    horizontal_glyph_part_margin = 10
    offset_x = page_margin_x
    offset_y = page_margin_y + (offset_y_index * (SIZE + vertical_line_margin))
    for i, char_ in enumerate(word):
        print("rotate %s with card %s" % (char_, card))
        if char_.isalpha():
            newchar, capitalize = char_to_tuple_rotated(char_, card)
        else:
            newchar, capitalize = char_, False
        print("printing character (%s) %s" % (i, newchar))
        if newchar not in CHARS_ARS:
            print("just dots")
            draw_dots(canvas_draw, offset_x, offset_y)
        else:
            for character_arr in CHARS_ARS[newchar]:
                print("printing glyph")
                append_output(character_arr, offset_x, offset_y, canvas_draw, should_capitalize=capitalize)
                offset_x += page_margin_x + (SIZE + horizontal_glyph_part_margin)
        offset_x += horizontal_char_margin


def draw_main(sentence, card, can_x=0, can_y=0):
    can_im = init_image(MODE, [can_x, can_y], BGCOLOR)
    canvas_draw = get_draw(can_im)
    for i, word in enumerate(sentence.split()):
        print("drawing word (%s) %s" % (i, word))
        loop_glyphs(word, card, canvas_draw=canvas_draw, offset_y_index=i)
    can_im.save("canvas.png", "PNG")


def init_image(mode, size, bgcolor, trans=False):
    im = Image.new(mode, size, bgcolor)
    if trans:
        trans = [(255, 255, 255, 0) for _ in range(size[0] * size[1])]
        im.putdata(trans)
    return im


def get_draw(im):
    return ImageDraw.Draw(im)


def main(sentence, card, can_x, can_y):
    draw_main(sentence, card, can_x=can_x, can_y=can_y)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("draw.py word card(0|11) can_x(0|255) can_y(0|255)")

    sentence, card, can_x, can_y = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    GRID = 5
    DISTANCE = 3
    SIZE = (GRID - 1) * (DISTANCE) + 1
    DOTS = []
    main(sentence, card, can_x, can_y)
