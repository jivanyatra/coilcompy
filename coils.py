import constants
from math import pi

class EffectiveResistivity(self, target_r, config_factor):
    '''Class for each coil configuration and target resistance'''
    def __init__:
        self.target_r = target_r
        self.config_factor = config_factor
        etr = 0
    def RtoER:
        '''Convert target resistance to the effective target
            resistance based on the configuration (parallel,
            dual, triple, etc)'''
        etr = target_r * config_factor
        return etr

class GetCoilBuild(self, etr, material_r, surface_area, inner_diameter):
    '''Class for each coil's calculated length of wire.'''
    def __init__:
        self.etf = etr
        self.material_r = material_r
        self.surface_area = surface_area
        wire_length = 0
        wraps = 0
    def GetWireLength:
        '''Get wire length for each coil'''
        # length (mm) = etr (ohms) * surface_area (mm^2) * 1000(mm/m)
        # all over material's resistivity ((ohm mm^2)/m)
        wire_length = (etr * surface_area * 1000)/material_r
        return wire_length
    def GetWraps:
        '''Get the number of wraps for the coil'''
        # wraps = length (mm)/(2 * pi * inner diameter of coil(mm)
        wraps = wire_length / (2 * pi * inner_diameter)
        return wraps
