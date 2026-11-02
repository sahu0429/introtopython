seconds = int(input("Enter seconds: "))
hours = seconds // 3600
rest = seconds % 3600
minutes = rest // 60
seconds = rest %  60
print(f"{hours}hr {minutes}min {seconds}sec")