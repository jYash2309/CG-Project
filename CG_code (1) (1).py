import turtle as te
from typing import Tuple

Step_write = 500        # Sampling times of Bezier function
Speed = 1
W = 600             # Interface Width
H = 500            # Interface Height
HX, YH = 0, 0           # Record the handle of the previous Bessel function


te.tracer(10)
te.setup(W, H, 0, 0)
te.setworldcoordinates(0, H, W, 0)
te.pensize(1)
te.speed(Speed)
te.penup()

def smooth_bzc(pts, rel: bool = False):   # Smooth Bezier curve
    global HX
    global YH
    pts = list(pts)
    pts.insert(0, (HX + te.position()[0], YH + te.position()[1]))
    if(rel):
        pts[0] = (pts[0][0] - te.position()[0],
                     pts[0][1] - te.position()[1])
    bzc_through(tuple(pts), rel)

def bzc_through(pts, rel: bool = False):  # Bezier Through
    global HX
    global YH
    curr = te.position()
    pts = list(pts)
    if(rel):
        for i in range(len(pts)):
            pts[i] = tuple([c1 + c2 for c1, c2 in zip(pts[i], curr)])
    pts.insert(0, curr)
    bzc(tuple(pts))
    HX = pts[-1][0] - pts[-2][0]
    YH = pts[-1][1] - pts[-2][1]

def m_t(point):    
    te.penup()
    te.goto(point)

def bzc(pts, dim=None):    # Bezier Curve
    if(dim is None):
        dim = len(pts[0])

    m_t(pts[0])
    te.pendown()
    for time in range(0, Step_write + 1):
        p = bzp(pts, time / Step_write, dim)
        te.goto(p)
    te.penup()


def bzp(pts, time, dim=2):  # Bezier Point
    deg = len(pts) - 1
    if(deg == 0):
        return pts[0]
    else:
        n_p = []
        for idx in range(deg):
            temp = []
            for d in range(dim):
                temp.append(pts[idx][d] * (1.0 - time) +
                            pts[idx + 1][d] * time)
            n_p.append(tuple(temp))
        return bzp(tuple(n_p), time, dim)



def poly_l(pts):
    total = len(pts)
    for idx in range(total - 1):
        l_b(pts[idx], pts[idx + 1])


def hz_t(dst_x):
    l_b(te.position(), (dst_x, te.ycor()))


def hz_d(dx):
    l_b(te.position(), te.position() + (dx, 0))

def l_b(src, dst):
    m_t(src)
    te.pendown()
    te.goto(dst)


def l_d(disp):
    l_b(te.position(), te.position() + disp)


def l_t(dst):
    l_b(te.position(), dst)


def vrt_d(dy):
    l_b(te.position(), te.position() + (0, dy))




def main():
    """
    Layer 1
    """

    # Coat
    te.color("black", "#005B96")
    m_t((61, 462))
    te.begin_fill()
    smooth_bzc(((12, -41), (27, -58)), rel=True)
    bzc_through(((-6, -36), (6, -118), (9, -132)), rel=True)
    bzc_through(((-15, -27), (-23, -51), (-26, -74)), rel=True)
    bzc_through(((4, -66), (38, -105), (65, -149)), rel=True)
    hz_t(486)
    bzc_through(((12, 24), (40, 99), (33, 114)), rel=True)
    bzc_through(((39, 82), (55, 129), (39, 144)), rel=True)
    smooth_bzc(((-31, 23), (-39, 28)), rel=True)
    smooth_bzc(((-12, 37), (-12, 37)), rel=True)
    l_d((50, 92))
    hz_t(445)
    smooth_bzc(((-29, -38), (-31, -46)), rel=True)
    smooth_bzc(((78, -107), (72, -119)), rel=True)
    smooth_bzc(((355, 178), (340, 176)))
    smooth_bzc(((272, 63), (264, 64)))
    smooth_bzc(((-29, 67), (-27, 73)), rel=True)
    smooth_bzc(((99, 292), (174, 428), (173, 439)))
    smooth_bzc(((-8, 23), (-8, 23)), rel=True)
    l_t((61, 462))
    te.end_fill()

    # Shadow
    m_t((60.5, 461.5))
    te.color("black", "#EF6727")
    te.begin_fill()
    bzc_through(((0, 0), (17, -42), (27, -59)), rel=True)
    bzc_through(((-6, -33), (6, -128), (10, -133)), rel=True)
    bzc_through(
        ((-15, -10), (-27, -66), (-27.285, -75)), rel=True)
    te.pencolor("#EED8AE")
    bzc_through(((12.285, 11), (82.963, 156),
                         (82.963, 156)), rel=True)
    te.pencolor("black")
    smooth_bzc(((12.322, 75), (19.322, 86)), rel=True)
    bzc_through(((-1, 11), (-8, 25), (-8, 25)), rel=True)
    hz_t(60.5)
    te.end_fill()

    m_t((444.5, 464))
    te.begin_fill()
    bzc_through(((0, 0), (-29, -36), (-31, -46)), rel=True)
    smooth_bzc(((53.59, -82.337), (53.59, -82.337)), rel=True)
    te.pencolor("#DAE397")
    smooth_bzc(((86.41, -47.663), (96.072, -54.85)), rel=True)
    smooth_bzc(((563.5, 297.5), (570.5, 299.5), (518.5, 334)))
    te.pencolor("black")
    bzc_through(((-2, 16), (-12, 33), (-12, 37)), rel=True)
    smooth_bzc(((50, 92), (50, 93)), rel=True)
    hz_t(444.5)
    te.end_fill()

    m_t((195, 49))
    te.begin_fill()
    te.pencolor("#D3DFF0")
    poly_l(((195, 49), (175.5, 106.5), (202.522, 49)))
    te.pencolor("black")
    hz_t(195)
    te.pencolor("#D3DFF0")
    te.end_fill()

    m_t((327.997, 49))
    te.begin_fill()
    te.pencolor("#D3DFF0")
    bzc_through(
        ((0, 0), (11.503, 121.087), (13.503, 128.087)), rel=True)
    bzc_through(((11, 2), (54, 37), (54, 37)), rel=True)
    l_d((-40, - 165.087))
    te.pencolor("black")
    hz_t(327.997)
    te.pencolor("#D3DFF0")
    te.end_fill()

    # Wrinkles
    te.pencolor("black")
    l_b((94.5, 397.5), (107.5, 373.5))
    l_b((122.5, 317.5), (95.875, 274.699))
    l_b((122.5, 341.5), (141.5, 402.5))
    l_b((141.5, 409.5), (153.5, 431.5))
    l_b((340.023, 49), (360.5, 144))
    l_b((478.5, 95.5), (518.5, 161.5))
    l_b((518.5, 332.5), (460.5, 359.5))
    poly_l(((506.5, 369.5), (493.5, 402.5), (502.5, 443.5)))
    m_t((530, 429))
    bzc_through(((4, 16), (-5, 33), (-5, 33)), rel=True)

    """
    Layer 2
    """

    # Inside of jacket
    te.color("black", "#822963")
    m_t((225, 462))
    te.begin_fill()
    hz_t(165)
    smooth_bzc(((9, -15), (8, -25)), rel=True)
    bzc_through(((-47, -126), (6, -212), (12, -225)), rel=True)
    smooth_bzc(((185, 305), (202, 428), (225, 462)))
    l_t((225, 462))
    te.end_fill()

    m_t((390, 462))
    te.begin_fill()
    bzc_through(
        ((10, -23), (34, -180), (35, -222)), rel=True)
    bzc_through(((7, 4), (54, 45), (61, 61)), rel=True)
    smooth_bzc(((-73, 101), (-72, 118)), rel=True)
    bzc_through(((5, 15), (31, 46), (31, 45)), rel=True)
    l_t((390, 462))
    te.end_fill()

    """
    Layer 3
    """

    # Inside of jacket
    te.color("black", "#FF7373")
    m_t((225, 462))
    te.begin_fill()
    bzc_through(((-28, -50), (-40, -166), (-40, -250)), rel=True)
    bzc_through(((6, 51), (-6, 87), (45, 106)), rel=True)
    smooth_bzc(((64, 27), (89, 24)), rel=True)
    smooth_bzc(((49, -18), (56, -20)), rel=True)
    smooth_bzc(((50, -10), (51, -85)), rel=True)
    bzc_through(((0, 29), (-25, 201), (-36, 225)), rel=True)
    l_t((225, 462))
    te.end_fill()

    """
    Layer 4
    """

    # Clothes
    te.color("black", "#003366")
    m_t((225, 462))
    te.begin_fill()
    bzc_through(((-5, -5), (-22, -53), (-23, -70)), rel=True)
    l_d((32, -13))
    bzc_through(((3, -25), (6, -28), (12, -36)), rel=True)
    smooth_bzc(((13, -12), (16, -12)), rel=True)
    vrt_d(-2)
    bzc_through(((45, 20), (64, 14), (94, 1)), rel=True)
    vrt_d(2)
    bzc_through(((8, -2), (15, 2), (17, 4)), rel=True)
    smooth_bzc(((0, 6), (-2, 9)), rel=True)
    bzc_through(((10, 10), (10, 29), (11, 33)), rel=True)
    smooth_bzc(((23, 4), (25, 6)), rel=True)
    smooth_bzc(((-17, 83), (-17, 78)), rel=True)
    l_t((225, 462))
    te.end_fill()

    """
    Layer 5
    """

    # Neck
    te.color("black", "#F5DCD2")
    m_t((262, 329))
    te.begin_fill()
    vrt_d(17)
    bzc_through(((1, 2), (44, 14), (45, 15)), rel=True)
    smooth_bzc(((3, 12), (3, 12)), rel=True)
    hz_d(3)
    vrt_d(-5)
    bzc_through(((1, -3), (4, -6), (5, -7)), rel=True)
    l_d((36, -14))
    bzc_through(((1, -1), (3, -16), (2, -17)), rel=True)
    smooth_bzc(((318, 348), (296, 344), (262, 329)))
    te.end_fill()

    """
    Layer 6
    """

    # White folds
    te.color("black", "#E7F1FF")
    m_t((225, 462))
    te.begin_fill()
    l_d((-3, - 5))
    bzc_through(((0, -2), (4, -4), (5, -6)), rel=True)
    smooth_bzc(((16, 3), (19, -8)), rel=True)
    smooth_bzc(((0, -7), (0, -11)), rel=True)
    smooth_bzc(((5, -8), (9, -5)), rel=True)
    smooth_bzc(((19, -8), (19, -11)), rel=True)
    smooth_bzc(((6, -7), (6, -7)), rel=True)
    smooth_bzc(((7, -2), (9, -4)), rel=True)
    l_d((41, -2))
    l_d((12, 9))
    smooth_bzc(((3, 15), (7, 18)), rel=True)
    smooth_bzc(((15, 4), (17, 4)), rel=True)
    smooth_bzc(((4, -4), (6, -4)), rel=True)
    smooth_bzc(((6, 4), (5, 9)), rel=True)
    smooth_bzc(((0, 9), (0, 9)), rel=True)
    smooth_bzc(((1, 7), (7, 6)), rel=True)
    smooth_bzc(((8, 0), (8, 0)), rel=True)
    l_d((-2, 8))
    l_t((225, 462))
    te.end_fill()

    te.pensize(2)
    m_t((240, 450))
    smooth_bzc(((0, 9), (3, 12)), rel=True)
    m_t((372, 462))
    bzc_through(((-2, -4), (-5, -29), (-7, -28)), rel=True)
    te.pensize(1)

    """
    Layer 7
    """

    # Collar
    te.color("black", "#00FFFF")
    m_t((262, 331))
    te.begin_fill()
    bzc_through(((0, 8), (-1, 13), (0, 15)), rel=True)
    smooth_bzc(((43, 14), (45, 15)), rel=True)
    l_d((3, 12))
    hz_d(3)
    smooth_bzc(((-1, -3), (0, -5)), rel=True)
    l_d((5, -7))
    l_d((36, -14))
    bzc_through(((1, -1), (2, -12), (2, -15)), rel=True)
    smooth_bzc(((25, -2), (15, 13)), rel=True)
    bzc_through(((-2, 4), (-7, 29), (-7, 32)), rel=True)
    smooth_bzc(((-35, 19), (-41, 22)), rel=True)
    smooth_bzc(((-9, 14), (-12, 14)), rel=True)
    smooth_bzc(((-7, -12), (-14, -15)), rel=True)
    bzc_through(((-19, -2), (-41, -25), (-41, -25)), rel=True)
    smooth_bzc(((-10, -26), (-10, -30)), rel=True)
    smooth_bzc(((255, 332), (262, 331)))
    te.end_fill()

    m_t((262, 346))
    l_d((-12, -6))
    m_t((369, 333))
    bzc_through(((2, 4), (-6, 10), (-15, 14)), rel=True)

    """
    Layer 8
    """

    # Tie
    te.color("black", "#151515")
    m_t((247, 358))
    te.begin_fill()
    bzc_through(((-5, 3), (-8, 20), (-6, 23)), rel=True)
    bzc_through(((25, 21), (50, 17), (50, 17)), rel=True)
    l_d((-23, 64))
    hz_d(22)
    smooth_bzc(((1, -13), (2, -16)), rel=True)
    l_d((13, -50))
    bzc_through(((2, 2), (7, 3), (10, 1)), rel=True)
    smooth_bzc(((18, 65), (18, 65)), rel=True)
    hz_d(19)
    l_d((-24, -65))
    bzc_through(((21, 5), (39, -10), (44, -13)), rel=True)
    bzc_through(((5, -20), (1, -21), (0, -24)), rel=True)
    bzc_through(((-18, -2), (-49, 15), (-52, 17)), rel=True)
    smooth_bzc(((-11, -3), (-15, -1)), rel=True)
    smooth_bzc(((252, 356), (247, 358)))
    te.end_fill()

    """
    Layer 9
    """

    # Collar visible through tie
    te.color("black", "#A2B8D6")
    m_t((297, 387))
    te.begin_fill()
    l_d((-11, 6))
    bzc_through(((-1, 0), (-20, -7), (-30, -19)), rel=True)
    smooth_bzc(((259, 373), (297, 385), (297, 387)))
    te.end_fill()

    m_t((323, 384))
    te.begin_fill()
    l_d((8, 7))
    l_d((30, -14))
    bzc_through(((1, -1), (5, -6), (4, -7)), rel=True)
    smooth_bzc(((329, 379), (323, 384)))
    te.end_fill()

    """
    Layer 10
    """

    # Face
    te.color("black", "#F3EEEB")
    m_t((185, 212))
    te.begin_fill()
    bzc_through(((4, -9), (46, -77), (52, -75)), rel=True)
    bzc_through(((-2, -17), (19, -68), (27, -73)), rel=True)
    bzc_through(((16, 15), (71, 108), (76, 112)), rel=True)
    smooth_bzc(((76, 53), (86, 60)), rel=True)
    bzc_through(((0, 65), (-27, 75), (-31, 76)), rel=True)
    bzc_through(((-50, 28), (-70, 30), (-85, 30)), rel=True)
    smooth_bzc(((-77, -22), (-86, -26)), rel=True)
    smooth_bzc(((180, 302), (186, 228), (185, 212)))
    te.end_fill()

    """
    Layer 11
    """

    # Hair
    te.color("black", "#822963")
    m_t((189, 202))
    te.begin_fill()
    bzc_through(((-1, 22), (19, 51), (19, 51)), rel=True)
    smooth_bzc(((-10, -42), (7, -92)), rel=True)
    smooth_bzc(((212, 168), (196, 189), (189, 202)))
    te.end_fill()

    m_t((221, 155))
    te.begin_fill()
    bzc_through(((-2, 6), (5, 48), (5, 48)), rel=True)
    smooth_bzc(((18, -28), (20, -48)), rel=True)
    bzc_through(((-5, 24), (4, 43), (7, 50)), rel=True)
    bzc_through(((-10, -49), (3, -72), (13, -106)), rel=True)
    bzc_through(((-2, -7), (-3, -32), (-3, -35)), rel=True)
    bzc_through(((-17, 18), (-27, 71), (-27, 71)), rel=True)
    l_t((221, 155))
    te.end_fill()

    m_t((264, 64))
    te.begin_fill()
    bzc_through(((-4, 5), (14, 100), (14, 100)), rel=True)
    smooth_bzc(((-6, -79), (-5, -85)), rel=True)
    bzc_through(((0, 98), (49, 139), (49, 139)), rel=True)
    smooth_bzc(((8, -50), (3, -65)), rel=True)
    smooth_bzc(((272, 64), (264, 64)))
    te.end_fill()

    m_t((342, 176))
    te.begin_fill()
    bzc_through(((-1, 27), (-10, 57), (-10, 57)), rel=True)
    smooth_bzc(((20, -33), (17, -54)), rel=True)
    l_t((342, 176))
    te.end_fill()

    te.penup()
    te.begin_fill()
    poly_l(((349, 180), (353, 203), (361, 203)))
    poly_l(((361, 203), (362, 188), (349, 180)))
    te.end_fill()

    """
    Layer 12
    """

    # Eyerbrows
    te.pensize(2)
    m_t((210, 180))
    bzc_through(((5, -4), (63, 9), (63, 14)), rel=True)
    m_t((338, 193))
    bzc_through(((0, -3), (18, -6), (18, -6)), rel=True)
    te.pensize(1)

    """
    Layer 13
    """

    # Eye 1
    te.color("black", "#FCFBF9")
    te.pensize(2)
    m_t((206, 212))
    te.begin_fill()
    l_d((15, -7))
    bzc_through(((4, -1), (26, -2), (30, 0)), rel=True)
    smooth_bzc(((10, 3), (12, 7)), rel=True)
    te.pencolor("#000000")
    te.pensize(1)
    smooth_bzc(((2, 27), (-1, 30)), rel=True)
    smooth_bzc(((-39, 5), (-44, 1)), rel=True)
    smooth_bzc(((206, 212), (206, 212)))
    te.end_fill()

    m_t((384, 204))
    te.begin_fill()
    te.pencolor("black")
    te.pensize(2)
    bzc_through(((-3, -1), (-18, -1), (-28, 1)), rel=True)
    smooth_bzc(((-9, 6), (-10, 9)), rel=True)
    te.pencolor("#000000")
    te.pensize(1)
    smooth_bzc(((3, 18), (6, 23)), rel=True)
    smooth_bzc(((38, 6), (40, 4)), rel=True)
    smooth_bzc(((10, -9), (13, -22)), rel=True)
    te.pencolor("black")
    te.pensize(2)
    l_t((384, 204))
    te.end_fill()

    """
    Layer 14
    """

    # Eye 2
    te.color("#000000", "#000000")
    te.pensize(1)
    m_t((216, 206))
    te.begin_fill()
    bzc_through(((-1, 5), (0, 26), (7, 35)), rel=True)
    smooth_bzc(((30, 2), (33, 0)), rel=True)
    smooth_bzc(((5, -31), (2, -34)), rel=True)
    smooth_bzc(((219, 203), (216, 206)))
    te.end_fill()

    m_t((354, 207))
    te.begin_fill()
    bzc_through(((-2, 1), (2, 29), (4, 31)), rel=True)
    smooth_bzc(((30, 3), (33, 1)), rel=True)
    smooth_bzc(((6, -24), (4, -27)), rel=True)
    l_d((-11, -8))
    smooth_bzc(((382, 204), (357, 206), (354, 207)))
    te.end_fill()

    """
    Layer 15
    """

    # Eye 3
    te.color("#FCFBF9", "#FCFBF9")
    m_t((253, 211))
    te.begin_fill()
    bzc_through(((-3, 0), (-8, 8), (1, 10)), rel=True)
    smooth_bzc(((258, 210), (253, 211)))
    te.end_fill()

    m_t((392, 209))
    te.begin_fill()
    l_d((4, 3))
    vrt_d(4)
    l_d((-4, 2))
    smooth_bzc(((386, 214), (392, 209), (392, 209)))
    te.end_fill()

    """
    Layer 16
    """

    # Eye 4
    te.color("#352F53", "#12374C")
    m_t((219, 229))
    te.begin_fill()
    smooth_bzc(((2, -5), (6, -4)), rel=True)
    smooth_bzc(((18, 13), (27, 1)), rel=True)
    bzc_through(((3, 0), (5, 3), (5, 3)), rel=True)
    vrt_d(13)
    hz_t(224)
    l_t((219, 229))
    te.end_fill()

    m_t((357, 227))
    te.begin_fill()
    smooth_bzc(((4, -6), (10, -2)), rel=True)
    smooth_bzc(((10, 13), (19, 1)), rel=True)
    bzc_through(((6, 0), (8, 6), (8, 6)), rel=True)
    l_d((-2, 9))
    bzc_through(((-12, 3), (-29, 0), (-32, -2)), rel=True)
    smooth_bzc(((357, 227), (357, 227)))
    te.end_fill()

    """
    Layer 17
    """

    # Eye 5
    te.color("#9A90CB", "#79192B")
    m_t((227, 231))
    te.begin_fill()
    bzc_through(((-6, 0), (-5, 5), (-3, 8)), rel=True)
    smooth_bzc(((24, 2), (27, 0)), rel=True)
    smooth_bzc(((0, -8), (-1, -8)), rel=True)
    smooth_bzc(((234, 231), (227, 231)))
    te.end_fill()

    m_t((361, 227))
    te.begin_fill()
    bzc_through(((2, 18), (26, 14), (30, 6)), rel=True)
    smooth_bzc(((-1, -3), (-2, -4)), rel=True)
    smooth_bzc(((-15, 9), (-24, -4)), rel=True)
    smooth_bzc(((363, 224), (361, 225), (361, 227)))
    te.end_fill()

    """
    Layer 18
    """

    # Eye line
    te.pencolor("black")
    te.pensize(3)
    m_t((225, 215))
    bzc_through(((10, 28), (22, 16), (24, 6)), rel=True)
    m_t((365, 219))
    bzc_through(((4, 14), (18, 24), (22, -3)), rel=True)
    te.pensize(2)
    l_b((240.5, 207.5), (227.5, 211.5))
    l_b((245.5, 209.5), (227.5, 214.5))
    l_b((247.5, 211.5), (227.5, 217.5))
    l_b((247.5, 214.5), (229.5, 220.5))
    l_b((247.5, 218.5), (230.5, 223.5))
    l_b((246.5, 222.5), (232.5, 226.5))
    l_b((244.5, 225.5), (234.5, 228.5))
    l_b((377.5, 207.5), (367.5, 210.5))
    l_b((384.5, 207.5), (366.5, 212.5))
    l_b((385.5, 210.5), (366.5, 215.5))
    l_b((384.5, 213.5), (366.5, 218.5))
    l_b((384.5, 215.5), (367.5, 220.5))
    l_b((384.5, 218.5), (368.5, 223.5))
    l_b((382.5, 223.5), (370.5, 227.5))

    """
    Layer 19
    """

    # Nose and mouth
    te.pencolor("black")
    m_t((309, 270))
    bzc_through(((0, 0), (4, 7), (1, 9)), rel=True)
    l_b((296.5, 307.5), (303.5, 307.5))
    m_t((315, 307))
    smooth_bzc(((10, -1), (10, 2)), rel=True)

    # Wait for the user to click to exit
    te.exitonclick()


if __name__ == '__main__':
    main()
