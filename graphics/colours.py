class Colours:

    def yellow(self, value, min_val, max_val):
        try: 
            t = (value - min_val) / (max_val - min_val)
            t = max(0, min(1, t))
        except ZeroDivisionError:
            t = 1

        r = int(100 + 155 * t)
        g = int(80 + 175 * t)
        b = int(0)

        return (r, g, b)
    
    def orange(self, value, min_val, max_val):
        try: 
            t = (value - min_val) / (max_val - min_val)
            t = max(0, min(1, t))
        except ZeroDivisionError:
            t = 1

        r = 255
        g = int(120 + 100 * t)
        b = int(0)

        return (r, g, b)
    
    def red(self, value, min_val, max_val):
        try: 
            t = (value - min_val) / (max_val - min_val)
            t = max(0, min(1, t))
        except ZeroDivisionError:
            t = 1
            
        r = int(150 + 105*t)
        g = int(30*(1-t))
        b = int(30*(1-t))

        return (r, g, b)
    
    def purple(self, value, min_val, max_val):
        if max_val == min_val:
            return (180,0,255)
        t = (value - min_val) / (max_val - min_val)
        t = max(0, min(1, t))

        r = int(120 + 100*t)
        g = 0
        b = int(150+105*t)

        return (r, g, b)
        
    def cyan(self, value, min_val, max_val):
        if max_val == min_val:
            return (0,255,200)
        t = (value - min_val) / (max_val - min_val)
        t = max(0, min(1, t))

        r = 0
        g = int(150 + 105*t)
        b = int(170+85*t)

        return (r, g, b)
    
    def magenta(self, value, min_val, max_val):
        if max_val == min_val:
            return (255,0,150)
        t = (value - min_val) / (max_val - min_val)
        t = max(0, min(1, t))

        r = 255
        g = int(40 * (1-t))
        b = int(120+100*t)

        return (r, g, b)
    
