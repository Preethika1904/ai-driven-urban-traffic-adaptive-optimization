def optimize_signal(congestion):

    if congestion > 70:
        return "Increase Green Signal Time"

    elif congestion > 50:
        return "Maintain Normal Signal"

    return "Traffic is Smooth"
