    # Imports 
from rectangle import Rectangle

    # main console
def main():
    fill_choice = input("Do you want your shape to be filled (F) or hollow (H)?: ").upper()
    shape_choice = input("Do you want a square or a rectangle? (s/r): ").upper()

    if shape_choice == "S":

        width_height = int(input("Enter the side length: "))
        width = width_height 
        height = width_height

    else:
        width = int(input("Enter the width: "))
        height = int (input("Enter the height: "))
        
    symbol = (input ("Enter a symbol you want to use: ")) 

    rectangle = Rectangle(width, height, symbol)

    if fill_choice == "F":
        rectangle.draw_filled()
    else:
        rectangle.draw_hollow()

    print(f"\nArea: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")

    while True:
        resize = input("\nResize rectangle? (Y/N): ").upper()
        if resize != "Y":
            break

        new_width = int (input("New width:  "))
        new_height = int (input("New height: "))
        rectangle.resize(new_width, new_height)
            
        if fill_choice == "F":
            rectangle.draw_filled()
        else:
            rectangle.draw_hollow()

        print(f"\nArea: {rectangle.area()}")
        print(f"Perimeter: {rectangle.perimeter()}")

if __name__ == "__main__":
    main()
