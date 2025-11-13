from shapes import Cylinder, Cone, Cube, Cuboid, Sphere

class MenuProgram:
    def start(self):
        while True:
            print("\n===== SHAPE MENU =====")
            print("1. Cylinder")
            print("2. Cone")
            print("3. Cube")
            print("4. Cuboid")
            print("5. Sphere")
            print("6. Exit")

            choice = int(input("Select a shape: "))

            if choice == 6:
                print("Exiting Program...")
                break

            print("\n--- Choose Operation ---")
            print("1. Curved Surface Area (CSA)")
            print("2. Total Surface Area (TSA)")
            print("3. Volume")

            op = int(input("Enter choice: "))

            if choice == 1:
                r = float(input("Enter radius: "))
                h = float(input("Enter height: "))
                obj = Cylinder(r, h)

            elif choice == 2:
                r = float(input("Enter radius: "))
                h = float(input("Enter height: "))
                obj = Cone(r, h)

            elif choice == 3:
                a = float(input("Enter side: "))
                obj = Cube(a)

            elif choice == 4:
                l = float(input("Enter length: "))
                b = float(input("Enter breadth: "))
                h = float(input("Enter height: "))
                obj = Cuboid(l, b, h)

            elif choice == 5:
                r = float(input("Enter radius: "))
                obj = Sphere(r)

            else:
                print("Invalid shape!")
                continue


            if op == 1:
                print("CSA =", obj.csa())
            elif op == 2:
                print("TSA =", obj.tsa())
            elif op == 3:
                print("Volume =", obj.volume())
            else:
                print("Invalid operation!")

app = MenuProgram()
app.start()
