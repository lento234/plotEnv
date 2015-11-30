"""
Custom colormaps
"""
import numpy as _np

# Planck cosmic microwave background (CMB) colormap
# More info: http://zonca.github.io/2013/09/Planck-CMB-map-at-high-resolution.html
_cmb_data = _np.array(  [[ 0.      ,  0.025737,  0.541892],
                         [ 0.      ,  0.047366,  0.709536],
                         [ 0.      ,  0.067675,  0.714596],
                         [ 0.      ,  0.087171,  0.719641],
                         [ 0.      ,  0.106085,  0.724671],
                         [ 0.      ,  0.124547,  0.729686],
                         [ 0.      ,  0.142642,  0.734687],
                         [ 0.      ,  0.160428,  0.739672],
                         [ 0.      ,  0.177949,  0.744644],
                         [ 0.      ,  0.195237,  0.749601],
                         [ 0.      ,  0.212318,  0.754544],
                         [ 0.      ,  0.229214,  0.759474],
                         [ 0.      ,  0.245941,  0.764389],
                         [ 0.      ,  0.262515,  0.769291],
                         [ 0.      ,  0.278947,  0.77418 ],
                         [ 0.      ,  0.295248,  0.779056],
                         [ 0.      ,  0.311427,  0.783919],
                         [ 0.      ,  0.327493,  0.788768],
                         [ 0.      ,  0.343451,  0.793605],
                         [ 0.      ,  0.359309,  0.79843 ],
                         [ 0.      ,  0.375072,  0.803241],
                         [ 0.      ,  0.390745,  0.808041],
                         [ 0.      ,  0.406333,  0.812828],
                         [ 0.      ,  0.42184 ,  0.817604],
                         [ 0.      ,  0.437269,  0.822367],
                         [ 0.      ,  0.452625,  0.827119],
                         [ 0.      ,  0.467909,  0.831859],
                         [ 0.      ,  0.483126,  0.836587],
                         [ 0.      ,  0.498278,  0.841304],
                         [ 0.      ,  0.513367,  0.84601 ],
                         [ 0.      ,  0.528396,  0.850704],
                         [ 0.      ,  0.543367,  0.855388],
                         [ 0.      ,  0.558282,  0.86006 ],
                         [ 0.      ,  0.573143,  0.864722],
                         [ 0.      ,  0.587951,  0.869373],
                         [ 0.      ,  0.602709,  0.874013],
                         [ 0.      ,  0.617418,  0.878642],
                         [ 0.      ,  0.632079,  0.883262],
                         [ 0.      ,  0.646693,  0.887871],
                         [ 0.      ,  0.661263,  0.892469],
                         [ 0.      ,  0.675789,  0.897058],
                         [ 0.      ,  0.690273,  0.901636],
                         [ 0.      ,  0.704716,  0.906205],
                         [ 0.      ,  0.719118,  0.910764],
                         [ 0.      ,  0.733481,  0.915312],
                         [ 0.      ,  0.747805,  0.919852],
                         [ 0.      ,  0.762093,  0.924381],
                         [ 0.      ,  0.776343,  0.928902],
                         [ 0.0625  ,  0.790559,  0.933413],
                         [ 0.125   ,  0.804739,  0.937914],
                         [ 0.1875  ,  0.818886,  0.942406],
                         [ 0.25    ,  0.832999,  0.946889],
                         [ 0.3125  ,  0.84708 ,  0.951363],
                         [ 0.375   ,  0.861129,  0.955828],
                         [ 0.4375  ,  0.875147,  0.960284],
                         [ 0.5     ,  0.889134,  0.964732],
                         [ 0.5625  ,  0.903091,  0.96917 ],
                         [ 0.625   ,  0.917019,  0.9736  ],
                         [ 0.6875  ,  0.930918,  0.978021],
                         [ 0.75    ,  0.944789,  0.982434],
                         [ 0.8125  ,  0.958632,  0.986838],
                         [ 0.875   ,  0.972448,  0.991234],
                         [ 0.9375  ,  0.986237,  0.995621],
                         [ 1.      ,  1.      ,  1.      ],
                         [ 1.      ,  1.      ,  1.      ],
                         [ 0.995621,  0.982826,  0.9375  ],
                         [ 0.991234,  0.965679,  0.875   ],
                         [ 0.986838,  0.94856 ,  0.8125  ],
                         [ 0.982434,  0.931469,  0.75    ],
                         [ 0.978021,  0.914406,  0.6875  ],
                         [ 0.9736  ,  0.897373,  0.625   ],
                         [ 0.96917 ,  0.880368,  0.5625  ],
                         [ 0.964732,  0.863394,  0.5     ],
                         [ 0.960284,  0.846449,  0.4375  ],
                         [ 0.955828,  0.829536,  0.375   ],
                         [ 0.951363,  0.812654,  0.3125  ],
                         [ 0.946889,  0.795803,  0.25    ],
                         [ 0.942406,  0.778985,  0.1875  ],
                         [ 0.937914,  0.7622  ,  0.125   ],
                         [ 0.933413,  0.745449,  0.0625  ],
                         [ 0.928902,  0.728731,  0.      ],
                         [ 0.924381,  0.712049,  0.      ],
                         [ 0.919852,  0.695402,  0.      ],
                         [ 0.915312,  0.678791,  0.      ],
                         [ 0.910764,  0.662216,  0.      ],
                         [ 0.906205,  0.64568 ,  0.      ],
                         [ 0.901636,  0.629182,  0.      ],
                         [ 0.897058,  0.612723,  0.      ],
                         [ 0.892469,  0.596304,  0.      ],
                         [ 0.887871,  0.579927,  0.      ],
                         [ 0.883262,  0.563591,  0.      ],
                         [ 0.878642,  0.547298,  0.      ],
                         [ 0.874013,  0.531049,  0.      ],
                         [ 0.869373,  0.514845,  0.      ],
                         [ 0.864722,  0.498688,  0.      ],
                         [ 0.86006 ,  0.482578,  0.      ],
                         [ 0.855388,  0.466516,  0.      ],
                         [ 0.850704,  0.450505,  0.      ],
                         [ 0.84601 ,  0.434546,  0.      ],
                         [ 0.841304,  0.418639,  0.      ],
                         [ 0.836587,  0.402787,  0.      ],
                         [ 0.831859,  0.386992,  0.      ],
                         [ 0.827119,  0.371255,  0.      ],
                         [ 0.822367,  0.355579,  0.      ],
                         [ 0.817604,  0.339965,  0.      ],
                         [ 0.812828,  0.324416,  0.      ],
                         [ 0.808041,  0.308935,  0.      ],
                         [ 0.803241,  0.293524,  0.      ],
                         [ 0.79843 ,  0.278186,  0.      ],
                         [ 0.793605,  0.262924,  0.      ],
                         [ 0.788768,  0.247743,  0.      ],
                         [ 0.783919,  0.232646,  0.      ],
                         [ 0.779056,  0.217638,  0.      ],
                         [ 0.77418 ,  0.202723,  0.      ],
                         [ 0.769291,  0.187907,  0.      ],
                         [ 0.764389,  0.173197,  0.      ],
                         [ 0.759474,  0.158599,  0.      ],
                         [ 0.754544,  0.144123,  0.      ],
                         [ 0.749601,  0.129778,  0.      ],
                         [ 0.744644,  0.115576,  0.      ],
                         [ 0.739672,  0.101532,  0.      ],
                         [ 0.734687,  0.087662,  0.      ],
                         [ 0.729686,  0.073989,  0.      ],
                         [ 0.724671,  0.060544,  0.      ],
                         [ 0.719641,  0.047366,  0.      ],
                         [ 0.714596,  0.034517,  0.      ],
                         [ 0.709536,  0.022097,  0.      ],
                         [ 0.541892,  0.010309,  0.      ]])