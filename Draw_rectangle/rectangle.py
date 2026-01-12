
class Rectangle ():

    def __init__(self, width: int, height: int, symbol: str):
        self.width = width
        self.height = height
        self.symbol = symbol

    def area (self) -> int :
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter (self) -> int :
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def is_square (self) -> bool :
        """Checks if the rectangle is a square."""
        return self.width == self.height
    
    def resize (self, new_width: int, new_height: int):
        """Resizes the rectangle."""
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Width and height must be positive integers.")
        self.width = new_width
        self.height = new_height

    def draw_hollow (self):
        """Draws a hollow rectangle."""
        if self.width < 2 or self.height < 2:
            print("Rectangle is too small to draw hollow.")
            return
        
        print ( self.symbol * self.width )
        for i in range( self.height - 2 ):
            print ( self.symbol + " " * ( self.width - 2 ) + self.symbol )
        print ( self.symbol * self.width ) 
    
    def draw_filled (self):
        """Draws a filled rectangle."""
        for i in range( self.height ):
            print ( self.symbol * self.width ) 
