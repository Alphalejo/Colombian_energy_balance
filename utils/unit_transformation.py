def bcf_to_twh(bcf, conversion_factor=0.293):
    """
    Converts natural gas volume from BCF to TWh.
    
    Parameters:
    - bcf (float): volume in billion cubic feet
    - conversion_factor (float): standard conversion factor (default: 0.293 TWh/BCF)
    
    Returns:
    - float: energy in TWh
    """
    return round(bcf * conversion_factor, 4)